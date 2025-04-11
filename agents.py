import os
from scrapper import get_text_from_url 
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor
from langchain.tools import tool
from dotenv import load_dotenv
from together import Together

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# Custom LLM wrapper
class ChatTogether:
    def __init__(self, model: str):
        self.model = model
        self.client = Together(api_key=TOGETHER_API_KEY)

    def invoke(self, messages):
        # Formata as mensagens no formato compatível com Together
        formatted = []
        for msg in messages:
            if isinstance(msg, HumanMessage):
                role = "user"
            elif isinstance(msg, SystemMessage):
                role = "system"
            else:
                role = "assistant"
            formatted.append({"role": role, "content": msg.content})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=formatted,
        )
        return response.choices[0].message.content


def get_response_from_llm(message):
    llm = ChatTogether(model="meta-llama/Llama-4-Scout-17B-16E-Instruct")
    return llm.invoke(message)


@tool
def documentation_tool(url: str, question: str) -> str:
    """
    Fetches and simplifies programming documentation from a given URL to answer a specific question.
    """
    context = get_text_from_url(url)

    messages = [
        SystemMessage(content="You're a helpful programming assistant that must explain programming library documentations to users as simple as possible"),
        HumanMessage(content=f"Documentation: {context} \n\n {question}")
    ]

    response = get_response_from_llm(messages)
    return response


@tool
def black_formatter_tool(path: str) -> str:
    """
    Formats Python code in the given file path using Black.
    """
    try:
        os.system(f"poetry run black {path}")
        return "Done"
    except:
        return "Did not work!"


toolkit = [documentation_tool, black_formatter_tool]

# Prompt manual para simular a lógica do agente
def ask_agent(user_input):
    system_msg = SystemMessage(content="""
    You are a programming assistant. Use your tools to answer questions.
    If you do not have a tool to answer the question, say no.

    return only the answers.
    """)

    messages = [system_msg, HumanMessage(content=user_input)]
    response = get_response_from_llm(messages)
    return response

# Exemplo de execução
if __name__ == "__main__":
    result = ask_agent("Quais as metricas padrao que o MLFLOW fornece para avaliar um modelo de texto baseado na documentacao dessa url aqui: https://mlflow.org/docs/latest/model-evaluation/index.html")
    print(result)
