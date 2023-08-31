from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)

chat_llm = ChatOpenAI(model_name="gpt-4")

system_template="""
You're a writer who writes fairy tales to the level of 5-7 year olds.

[규칙]
- 동화는 키워드를 포함한다.
- 동화는 4개의 문단으로 이루어져있다.
- 동화의 한 문단은 2~3개의 문장으로 이루어져있다.
- 이야기 안에 인용구를 넣어야할 경우 쌍따옴표 안에 따옴표를 넣는다. 예시 : "엄마는 나에게 말했다. '밥 먹어' "

[응답 양식]은 아래 예시와 같은 list 형식으로 작성해야 합니다.
예시:
["제목", "문단1", "문단2", "문단3", "문단4"]

키워드 : {user_input}
"""

system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])

def story_chain():
    chain = LLMChain(
        llm=chat_llm,
        prompt=chat_prompt,
    )
    return chain