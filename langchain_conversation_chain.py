from langchain.llms import openai
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from openapi_key import apiKey
import os
from langchain.llms import openai

os.environ["OPENAI_API_KEY"] = apiKey
# LIMIT CONVERSATION UPTO 5 to remember only
memory = ConversationBufferWindowMemory(k=5)
llm = openai.OpenAI(temperature=0.7)


def conversationChainDemo():
    chain = ConversationChain(llm=llm, memory=memory)

    response = chain.run("who was priminis in india in 2022?")
    return response


if __name__ == "__main__":
    # Call your method with a specific cuisine (e.g., "Indian")
    result = conversationChainDemo()
    print(result)
