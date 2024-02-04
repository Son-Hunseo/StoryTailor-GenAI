from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from typing import List, Dict
from langchain_core.pydantic_v1 import BaseModel, Field

chat_llm = ChatOpenAI(model_name="gpt-4-0125-preview")

prompt_template="""
You're a writer who writes fairy tales to the level of 5-7 year olds.

[규칙]
- 동화는 키워드를 포함한다.
- 동화는 4개의 문단으로 이루어져있다.
- 아이가 지루해하거나 어려워하지 않게하기위해 동화의 각문단은 2~3개의 어렵지 않은 문장으로 이루어져있다.
- 아이에게 부정적인 영향을 끼치지 않기 위해서 동화에 폭력적인 내용, 선정적인 내용 등 아이에게 부적절한 내용은 작성하지 않는다.
- 이야기 안에 인용구를 넣어야할 경우 쌍따옴표 안에 따옴표를 넣는다. 예시 : "엄마는 나에게 말했다. '밥 먹어' "

[응답 양식]은 아래 예시와 같은 list 형식으로 작성해야 합니다.
예시:
["제목", "문단1", "문단2", "문단3", "문단4"]

키워드 : {user_input}
"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["user_input"]
)

class Story(BaseModel):
    story: List[str] = Field(description="스토리")

parser = JsonOutputParser(pydantic_object=Story)

async def story_chain():
    return PROMPT | chat_llm | parser