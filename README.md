# LangChain Development Suite: From Prompts to Production 🦜🔗

This repository is a structured exploration of the **LangChain** ecosystem. It demonstrates the transition from basic LLM calls to complex, stateful applications including automated prompt serialization, chat memory management, and interactive web interfaces.

## 🏗️ Architecture Overview

The project is organized into modular components that showcase specific LangChain primitives:
* [cite_start]**Models**: Interaction with OpenAI and Groq (Llama) models[cite: 1].
* **Prompts**: Use of `PromptTemplate`, `ChatPromptTemplate`, and `MessagesPlaceholder` for dynamic input.
* **Memory**: Implementation of chat history using `HumanMessage`, `AIMessage`, and `SystemMessage`.
* **UI/UX**: Web-based research tools built with **Streamlit**.

---

## 📂 Detailed File Manifest

### 1. Core LLM Interactions
* **`1_llm_demo.py`**: A foundational script that initializes `ChatOpenAI` with specific parameters like `temperature=0.2` to demonstrate deterministic responses.
* **`messages.py`**: Illustrates the structure of a conversation using a list of message objects, showing how to append an `AIMessage` to the state after a model invocation.

### 2. Advanced Prompt Engineering
* **`prompt_generator.py`**: Creates a complex, multi-variable template for research paper analysis and serializes it into a reusable `template.json` file.
* [cite_start]**`template.json`**: A configuration file containing input variables (`paper_input`, `style_input`, `length_input`) and specialized instructions for mathematical explanations[cite: 1].
* **`chat_prompt_template.py`**: Demonstrates the use of tuple-based roles (`system`, `human`) to define persona-driven prompts, such as a "Cricket Expert".

### 3. Stateful Conversational AI
* **`chatbot.py`**: A continuous loop application that maintains a `chat_history` list, allowing the AI to remember previous context within a session until the user types "exit".
* **`messages_placeholder.py`**: Shows how to integrate external historical data (from `chat_history.txt`) into a prompt template using `MessagesPlaceholder` for context-aware customer support.

### 4. Interactive Web Applications
* **`prompt_ui.py`**: A full-stack demo utilizing **Streamlit**. It allows users to:
    * Select from pre-defined research papers.
    * Choose explanation styles (Technical, Beginner-Friendly, etc.).
    * Execute a LangChain **LCEL (LangChain Expression Language)** chain: `template | model`.

---

## 🛠️ Technical Implementation Details

### **Mathematical & Code Logic**
The system is designed to handle technical summaries. The `template.json` specifically instructs the model to:
* [cite_start]Include relevant mathematical equations[cite: 1].
* [cite_start]Explain concepts via simple code snippets[cite: 1].
* [cite_start]Use analogies to simplify complexity[cite: 1].

### **Data Persistence**
The repository handles data in various formats:
* [cite_start]**JSON**: For structured prompt storage[cite: 1].
* **TXT**: For raw chat logs used in support agent simulations.

---

## ⚙️ Setup & Installation

### **Prerequisites**
* Python 3.9+
* API Keys for OpenAI and Groq.

### **Installation**
1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/LangChain-DeepDive.git](https://github.com/YOUR_USERNAME/LangChain-DeepDive.git)
    cd LangChain-DeepDive
    ```
2.  **Install requirements:**
    ```bash
    pip install langchain-openai langchain-groq streamlit python-dotenv langchain-core
    ```
3.  **Environment Setup:**
    Create a `.env` file and populate it:
    ```env
    OPENAI_API_KEY=your_key_here
    GROQ_API_KEY=your_key_here
    ```

## 🚀 Running the Project

* **Launch the UI**: `streamlit run prompt_ui.py`
* **Start the Chatbot**: `python chatbot.py`
* **Generate Prompts**: `python prompt_generator.py`

---

## 📄 License
This project is open-source under the MIT License.
