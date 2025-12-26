import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# load the environment variables from a .env file
load_dotenv(r".env")

# Initialize the ChatGoogleGenerativeAI model

llm = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash-lite',
    temperature=0.7,
    max_output_tokens=512
)

question = "tell me the difference between communism and capitalism? give a funny sarcastic response."

result = llm.invoke(question)

print(result.content)