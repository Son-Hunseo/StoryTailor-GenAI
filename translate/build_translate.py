from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

chat_llm = ChatOpenAI(model_name="gpt-4-0125-preview")

prompt_template="""
너는 여러 언어로 번역을 해주는 번역가이다.
너는 Input이 들어오면 번역을 해서 Output을 출력한다.
Input은 List 자료형으로 들어오며, Input List의 마지막 요소는 번역해야할 언어이다.
Input List의 마지막요소가 "ko"일 경우 한국어로 번역하고, "en"일 경우 영어로 번역하고, "ja"일 경 일본어로 번역하고, "zh"일 경우 중국어로 번역한다. 

Input 예시:
["사과", "사자", "고양이", "라면", "en"]

Output 예시:
["apple", "lion", "cat", "ramen"]


Input : {user_input}
"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["user_input"]
)

async def translate_chain():
    return PROMPT | chat_llm
