import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv(r".env")

llm = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash-lite',
    temperature=0.7,
    max_output_tokens=512
)

# prompt template

template_str = """
please summarize the research paper titled "{paper_input}" with the following specifications:
explaination style: {style_input}
explanation length: {length_input}

1. mathematical details:
 - explain mathematical concepts using simple code snippets wherever applicable.

2. Analogies:
 - use real-world analogies to explain complex ideas.

"""

template_prompt = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template=template_str
)


# build the streamlit app ui

st.set_page_config(page_title="Research Paper Summarizer", page_icon=":books:", layout="centered")
st.title("📚 Research Paper Summarizer with gemini")


paper_input = st.selectbox(
    "Select a research paper to summarize:",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "GPT-3: Language Models are Few-Shot Learners",
        "ULMFiT: Universal Language Model Fine-tuning for Text Classification",
        "RoBERTa: A Robustly Optimized BERT Pretraining Approach"

    ])


style_input = st.selectbox(
    "Select the explanation style:",
    [
        "Simple and Clear",
        "Detailed and Technical",
        "Humorous and Light-hearted",
        "Concise and To the Point"
    ])

length_input = st.selectbox(
    "Select the explanation length:",
    [
        "Short (100-200 words)",
        "Medium (200-400 words)",
        "Long (400-500 words)"
        ])


# execution

if st.button("Generate Summary"):
    chain = template_prompt | llm
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input})
    
    st.markdown(result.content)