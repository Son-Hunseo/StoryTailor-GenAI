from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)

# chat_llm = ChatOpenAI(model_name="gpt-4")
chat_llm = ChatOpenAI(model_name="gpt-4-1106-preview")

system_template="""
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

Input : {input}
"""

system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])

def make_quiz_chain():
    build_chain = LLMChain(
        llm=chat_llm,
        prompt=chat_prompt,
    )
    return build_chain
