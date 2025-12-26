import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(r".env")

llm = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash-lite',
    temperature=0.7,
    max_output_tokens=200
)

prompt = PromptTemplate(
    template="Explain the following concept in simple terms: {topic}",
    input_variables=["topic"]
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

result = chain.invoke({"topic": "quantum computing"})

print(result)

print("\n--- Chain Graph ---\n")
chain.get_graph().print_ascii()