---

# 🚀 The GenAI Playbook

## From Prompting to Applications

**Faculty Development Program (FDP) on Generative AI**

---

## 📌 Overview

This repository contains the **official hands-on materials** for the **Faculty Development Program (FDP)** titled:

> **“The GenAI Playbook: From Prompting to Application”**

The FDP is designed to provide **educators, researchers, and academicians** with a **practical and conceptual understanding** of **Generative AI**, **Large Language Models (LLMs)**, **Prompt Engineering**, **Transformers**, **Hugging Face**, **LangChain**, **RAG (Retrieval-Augmented Generation)**, and **end-to-end AI application development**.

The content moves **progressively** from fundamentals to **real-world GenAI applications**, with extensive use of **Python**, **Jupyter Notebooks**, and **Streamlit-based UIs**.

---

## 🎯 Learning Objectives

By completing this FDP, participants will be able to:

* Understand the **foundations of Generative AI and LLMs**
* Explain **word embeddings, transformers, and attention mechanisms**
* Work with **Hugging Face models and tokenizers**
* Apply **sampling strategies** for controlled text generation
* Design **effective prompts** for different tasks
* Build **LangChain pipelines and chains**
* Implement **Retrieval-Augmented Generation (RAG)** using **ChromaDB**
* Develop **interactive GenAI applications** using **Streamlit & Gradio**
* Deploy **“Chat with Your Data”** systems

---

## 🧠 FDP Content Structure

The repository is organized in a **concept-to-application flow**.

```
.
├── notebooks/
│   ├── 1word_embeddings_fdp.ipynb
│   ├── 2transformers.ipynb
│   ├── 3huggingface.ipynb
│   ├── 4sampling_tech.ipynb
│   ├── 4chromadb_RAG.ipynb
│
├── applications/
│   ├── 1demo.py
│   ├── 2prompt_ui.py
│   ├── 3chains.py
│   ├── 5ChatWithYourDataApp.py
│
├── requirements.txt
├── .env.example
└── README.md
```

---

## 📘 Detailed Module Description

### 🔹 Module 1: Word Embeddings

**File:** `1word_embeddings_fdp.ipynb`

* One-hot encoding vs dense embeddings
* Distributional semantics
* Conceptual foundation of embeddings in NLP
* Role of embeddings in modern LLMs

---

### 🔹 Module 2: Transformers Architecture

**File:** `2transformers.ipynb`

* Limitations of RNNs and LSTMs
* Self-attention mechanism
* Multi-head attention
* Encoder–Decoder architecture
* Why “Attention Is All You Need”

---

### 🔹 Module 3: Hugging Face Ecosystem

**File:** `3huggingface.ipynb`

* Hugging Face Transformers library
* Tokenizers and pipelines
* Loading and using pretrained models
* Text generation, summarization, and QA

---

### 🔹 Module 4: Sampling Techniques in LLMs

**File:** `4sampling_tech.ipynb`

* Greedy decoding
* Beam search
* Top-K sampling
* Top-P (nucleus) sampling
* Temperature control
* Effect of sampling on creativity and determinism

---

### 🔹 Module 5: Prompt Engineering

**Files:**

* `1demo.py`

* `2prompt_ui.py`

* Zero-shot, few-shot prompting

* Prompt templates

* Role-based prompting

* Structured prompting using LangChain

* Streamlit-based UI for prompt interaction

---

### 🔹 Module 6: LangChain & Chains

**File:** `3chains.py`

* Introduction to LangChain
* Prompt → LLM → OutputParser pipeline
* Building reusable chains
* Visualizing chain execution graphs

---

### 🔹 Module 7: Retrieval-Augmented Generation (RAG)

**Files:**

* `4chromadb_RAG.ipynb`

* `5ChatWithYourDataApp.py`

* RAG architecture overview

* Document chunking strategies

* Vector databases with ChromaDB

* Embedding and indexing documents

* Query-time retrieval + LLM reasoning

* End-to-end **Chat with Your Data** application using Streamlit

---

## 🛠️ Tech Stack Used

* **Python 3.9+**
* **Jupyter Notebook**
* **Google Gemini (Generative AI models)**
* **LangChain**
* **Hugging Face Transformers**
* **ChromaDB**
* **Streamlit**
* **Gradio**
* **PyPDF2**
* **dotenv**

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/genai-fdp.git
cd genai-fdp
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv genai_env
source genai_env/bin/activate   # Linux/Mac
genai_env\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file based on `.env.example`:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Running Applications

### 🔹 Run Prompt Engineering Demo

```bash
python applications/1demo.py
```

### 🔹 Run Streamlit Prompt UI

```bash
streamlit run applications/2prompt_ui.py
```

### 🔹 Run Chat With Your Data App

```bash
streamlit run applications/5ChatWithYourDataApp.py
```

---

## 👨‍🏫 Target Audience

* Faculty members (Engineering, Science, Humanities)
* Academic researchers
* PhD scholars
* AI & Data Science trainers
* Curriculum designers

---

## 📜 Certification

Participants completing the FDP are awarded an **Industrial Training Certificate** acknowledging hands-on training in **Generative AI and Applied LLM Systems**.

---

## 🤝 Contribution Guidelines

Contributions are welcome in the form of:

* Improved notebooks
* Additional GenAI use cases
* New LangChain pipelines
* Optimization of RAG workflows

Please create a **pull request** with proper documentation.

---

## 📄 License

This repository is intended for **academic and educational use only**.
Commercial reuse requires prior permission from the organizers.

---

## 📞 Contact

For FDP collaborations, institutional training, or academic partnerships:

**MITU Skillologies**
📧 Email: *tppkar@gmail.com*
🌐 Website: *https://mitu.co.in*

---
