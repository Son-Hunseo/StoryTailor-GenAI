from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict
import json

from chat.build_keyword import keyword_chain
from quiz.build_quiz import quiz_chain
from story.build_img_prompt import imgPrompt_chain
from story.build_story import story_chain
from memory.build_memory import memory_chain
from translate.build_translate import translate_chain

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    msgNum: int
    msgType: str
    sessionId: int
    history: Dict[str, List[str]]
    text: str

class ChatResponse(BaseModel):
    msgNum: int
    sessionId: int
    msgType: str
    text: str
    status: str
    keyword: List[str]
    recoKeyword: List[str]

class StoryRequest(BaseModel):
    keyword: List[str]

class StoryResponse(BaseModel):
    story: List[str]
    imgPrompt: List[str]

class TranslateRequest(BaseModel):
    story: List[str]
    lang: str

class TranslateResponse(BaseModel):
    story: List[str]
    lang: str

class QuizRequest(BaseModel):
    sentence: str

class QuizResponse(BaseModel):
    sentence: str
    options: List[str]
    answer: str

@app.post("/tailor/chat")
async def chat(request_data: ChatRequest):
    msgNum = request_data.msgNum
    msgType = request_data.msgType
    sessionId = request_data.sessionId
    history = request_data.history
    text = request_data.text

    memory = await memory_chain(history)
    chain = await keyword_chain(memory)
    response = await chain.ainvoke({"user_input":text})
    response = response["text"]
    print("response : " + response)
    response = json.loads(response)

    AItext = response['text']
    status = response['status']
    keyword = response['keyword']
    recoKeyword = response['recoKeyword']

    result = ChatResponse(
        msgNum=msgNum + 1,
        sessionId=sessionId,
        msgType="AI",
        text=AItext,
        status=status,
        keyword=keyword,
        recoKeyword=recoKeyword
    )
    return result

@app.post('/tailor/makeStory')
async def make_story(request_data: StoryRequest):
    keyword = request_data.keyword

    chain_1 = await story_chain()
    story = await chain_1.ainvoke({"user_input": keyword})

    chain_2 = await imgPrompt_chain()
    imgPrompt = await chain_2.ainvoke({"user_input": story[1:]})

    result = StoryResponse(
        story = story,
        imgPrompt = imgPrompt
    )
    return result

@app.post('/tailor/translate')
async def translate(request_data: TranslateRequest):
    story = request_data.story
    obj_lang = request_data.lang
    story.append(obj_lang)

    chain = await translate_chain()
    trans = await chain.ainvoke({"user_input": story})
    trans = trans.content

    # 자꾸 앞에 'Output : ' 이 붙어서 나와서 이를 제거했다
    cut_off_index = trans.find('[')
    if cut_off_index != -1:
        trans = trans[cut_off_index:]
    else:
        trans = trans

    if obj_lang == 'zh':
        result = TranslateResponse(
            story = eval(trans.encode('utf-8')),
            lang = obj_lang
        )
    else:
        result = TranslateResponse(
            story = eval(trans),
            lang = obj_lang
        )
    return result

@app.post('/tailor/quiz')
async def quiz(request_data: QuizRequest):
    sentence = request_data.sentence
    chain = await quiz_chain()
    quiz = await chain.ainvoke({"user_input": sentence})

    result = QuizResponse(
        sentence = quiz["sentence"],
        options = quiz["options"],
        answer = quiz["answer"]
    )
    return result