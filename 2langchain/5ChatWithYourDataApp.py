# upload pdf -> index with chromadb -> ask question -> get answer answer (gemini llm)

import os
import streamlit as st
from dotenv import load_dotenv
import PyPDF2
import chromadb
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate


load_dotenv(r".env")

# Configuration

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
CHROMA_PATH = "./chroma_db"
CHUNK_SIZE = 300
CHUNK_OVERLAP = 50
K_RETRIEVAL = 7


# streamlit setup

st.set_page_config(page_title="Chat with your DATA", page_icon=":books:", layout="wide")
st.title("Chat with your DATA :books:")

# initialize session state

if "rag_pipeline" not in st.session_state:
    os.makedirs(CHROMA_PATH, exist_ok=True)
    st.session_state.rag_pipeline = chromadb.PersistentClient(path=CHROMA_PATH)
    st.session_state.collection = st.session_state.rag_pipeline.get_or_create_collection(name="docs")
    st.session_state.llm = ChatGoogleGenerativeAI(
        model = "gemini-2.5-flash-lite",
        api_key = GOOGLE_API_KEY,
        temperature = 0.7
    )
    st.session_state.chat_history = []


# sidebar => upload and manage pdfs

with st.sidebar:
    st.header("Upload your PDFs")
    

    # show stats
    count = st.session_state.collection.count()
    st.metric("Total Documents in DB", count)

    st.divider()

    pdf_file = st.file_uploader("upload your pdf here", type = "pdf")

    if pdf_file and st.button("process the pdf"):
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # chunk the data
        splitter = RecursiveCharacterTextSplitter(
            chunk_size = CHUNK_SIZE,
            chunk_overlap = CHUNK_OVERLAP,
            separators= ["\n\n", "\n", " ", ""]
        )

        chunks = splitter.split_text(text)

        # add these chunks to chromadb
        for idx, chunk in enumerate(chunks):
            st.session_state.collection.add(
                documents = [chunk],
                metadatas = [{"source": pdf_file.name, "chunk_id": idx}],
                ids = [f"{pdf_file.name}_{idx}"]
            )

        st.success(f"Processed {pdf_file.name} and added {len(chunks)} chunks to the database.")

    # divider and then clear database option
    st.divider()

    if st.button("Clear Database", use_container_width=True):
        st.session_state.rag_pipeline.delete_collection(name="docs")
        st.session_state.collection = st.session_state.rag_pipeline.get_or_create_collection(name="docs")
        st.session_state.chat_history = []
        st.success("Cleared the database and chat history.")




# main chat interface

if st.session_state.collection.count() == 0:
    st.warning("No documents in the database. Please upload PDFs to proceed.")
else:
    # dispay chat history
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.chat_message("user").write(msg["content"])
        else:
            st.chat_message("assistant").write(msg["content"])

    st.divider()

    # user input
    user_query = st.chat_input("Ask a question about your documents")

    if user_query:
        st.session_state.chat_history.append({"role": "user", "content": user_query})
        st.chat_message("user").write(user_query)

        # retrieve relevant chunks from chromadb
        results = st.session_state.collection.query(
            query_texts= [user_query],
            n_results= K_RETRIEVAL
        )

        # format the text
        context = "\n\n".join([doc for doc in results['documents'][0]])

        # generate the answer using llm

        prompt = PromptTemplate(
            template = "Context: {context}\n\nQuestion: {query}\n\nAnswer the question based on only the context provided.",
            input_variables = ["context", "query"]
        )

        response = st.session_state.llm.invoke(
            prompt.format(context=context, query=user_query)
        )

        answer = response.content

        # add assistant message
        st.session_state.chat_history.append({"role": "assistant", "content": answer})
        st.chat_message("assistant").write(answer)