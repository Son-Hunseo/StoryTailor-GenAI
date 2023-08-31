from langchain.memory import ConversationBufferWindowMemory

def build_memory(history):

    memory = ConversationBufferWindowMemory(k=5, memory_key="chat_history", return_messages=True)
    print(history)
    if history != None:
        for i in range(len(history['userChat'])):
            memory.save_context({"input": history['userChat'][i]}, {"output": history['aiChat'][i]})

    return memory
