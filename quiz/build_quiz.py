from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from typing import List, Dict
from langchain_core.pydantic_v1 import BaseModel, Field

chat_llm = ChatOpenAI(model_name="gpt-4-0125-preview")

prompt_template="""
너는 빈칸을 추론하는 문제를 생성하는 문제 생성기야.
너는 Input이 들어오면 Input에 빈칸을 만들어서 Output을 출력한다.
빈칸은 ()로 나타낸다.
Output에는 반칸이 뚫린 원래의 Input과 해당 빈칸에 들어갈 후보들이 출력된다.
Input은 한국여, 영어, 중국어, 일본어 등 다양한 언어로 들어올 수 있으며, 각 언어에 맞게 출력한다.
Output은 예시와 같은 JSON형태로 출력한다.
 
Input 예시:
"티라노사우루스가 뛰고 있다."

Output 예시:
{{"sentence" : "티라노사우루스가 () 있다.", "options" : ["뛰고", "날고", "자고"], "answer" : "뛰고"}}

Input : {user_input}
"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["user_input"]
)

class Quiz(BaseModel):
    sentence: str = Field(description="문제")
    options: List[str] = Field(description="선지")
    answer: str = Field(description="정답")

parser = JsonOutputParser(pydantic_object=Quiz)

async def quiz_chain():
    return PROMPT | chat_llm | parser
