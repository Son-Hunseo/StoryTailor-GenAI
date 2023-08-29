from langchain.memory import ConversationBufferWindowMemory

def build_memory(history):

    memory = ConversationBufferWindowMemory(k=5, memory_key="chat_history", return_messages=True)

    if history != None:
        for i in range(len(history['UserChat'])):
            memory.save_context({"input": history['UserChat'][i]}, {"output": history['AIChat'][i]})

    return memory