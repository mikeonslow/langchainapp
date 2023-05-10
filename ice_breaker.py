from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

def main():
    print("starting application...")
    with open('/app/output/ice_breaker.txt', 'w') as f:
        f.write('Hello LangChain!')

if __name__ == "__main__":
    main()





