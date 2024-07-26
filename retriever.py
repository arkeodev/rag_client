"""
retriever.py

This module handles document retrieval and creation of retriever tools.
"""

import logging

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS


def create_retriever_from_pdf(pdf_file, embedder):
    """Creates a retriever tool from a PDF file uploaded by the user."""
    logging.info("Creating retriever tool from uploaded PDF file.")

    # Save the uploaded file to a temporary file
    with open("temp_uploaded_file.pdf", "wb") as f:
        f.write(pdf_file.getbuffer())

    # Load the PDF using the temporary file path
    loader = PyPDFLoader(file_path="temp_uploaded_file.pdf")
    paper = loader.load()
    logging.info("PDF file loaded successfully.")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks_paper = text_splitter.split_documents(paper)
    logging.info("PDF file split into smaller chunks.")

    faiss_db_paper = FAISS.from_documents(chunks_paper, embedder)
    retriever_paper = faiss_db_paper.as_retriever()
    logging.info("Embeddings created and stored in FAISS vector store.")

    retriever_tool = create_retriever_tool(
        retriever_paper, "RAG doc", "Search for info on RAG"
    )
    logging.info("Retriever tool created successfully.")
    return retriever_tool
