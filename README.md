# RAG Agent Project

This project demonstrates the creation of a Retrieval-Augmented Generation (RAG) agent using LangChain. The agent can dynamically determine which actions to take and in what order to achieve a desired outcome.

## Setup

1. Create and activate a virtual environment using Conda:
    ```sh
    conda create --name .venv python=3.10
    conda activate .venv
    ```

2. Install the necessary Python libraries:
    ```sh
    pip install -U langgraph langchain langchain-openai langchainhub langchain-community tavily-python faiss-cpu httpx python-dotenv streamlit
    ```

3. Set up API keys in a `.env` file:
    ```
    OPENAI_API_KEY=your_openai_api_key_here
    SERPAPI_API_KEY=your_serpapi_api_key_here
    ```

## Running the Streamlit App

To start the Streamlit application, run the following command:
```sh
streamlit run main.py
