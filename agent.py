from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

from langtools import VISAFXRate, WebBrowser


def main():
    load_dotenv()
    llm = ChatOpenAI(model_name="gpt-3.5-turbo-0613")
    tools = [
        WebBrowser(),
        VISAFXRate(),
    ]
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    agent = initialize_agent(tools=tools, llm=llm, agent=AgentType.OPENAI_FUNCTIONS, memory=memory, verbose=True)
    while True:
        try:
            question = input("User: ")
            resp = agent.run(question)
            print('Agent:', resp)
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()
