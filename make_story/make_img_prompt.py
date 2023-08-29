from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)

chat_llm = ChatOpenAI(model_name="gpt-4")

system_template="""
You're prompt engineer who make prompt for Image Generative AI.

[Rule]
- prompt should be English.
- Each paragraph in the story turns into its own prompt.
- The prompt must be cartoon style and color pencil scetch.
- The prompt describes the story as a scene, but in several very short sentences.

YOU MUST MAKE RESPONSE LIST TYPE.
output example:
[prompt1, prompt2, prompt3, prompt4]

prompt example:
- a man is doing a kickflip. pencil scatch.
- a robot wearing a flower lei surfing a huge wave. digital art. tube riding.
- a hamster superhero. black and white coloring book. city skyline in background.

story : {user_input}
"""

system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])

def imgPrompt_chain():
    chain = LLMChain(
        llm=chat_llm,
        prompt=chat_prompt,
    )
    return chain