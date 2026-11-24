import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

GEMINI_CHAT_LITE_MODEL = os.getenv("GEMINI_CHAT_LITE_MODEL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


llm = ChatGoogleGenerativeAI(
    model=GEMINI_CHAT_LITE_MODEL,
    google_api_key=GEMINI_API_KEY,
    tools=[{"type": "computer_use", "environment": "browser"}],
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert technical assistant helping a developer build a project.",
        ),
        ("human", "{user_query}"),
    ]
)

chain = prompt | llm | StrOutputParser()

result = chain.invoke({"user_query": "hi i am rolex"})

print("\nChain Response:\n", result)
