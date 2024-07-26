"""
retriever.py

This module handles document retrieval and creation of retriever tools.
"""

import logging
import os

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS

from src.utils import save_uploaded_file


def create_retriever_from_pdf(pdf_file, embedder):
    """Creates a retriever tool from a PDF file uploaded by the user."""
    logging.info("Creating retriever tool from uploaded PDF file.")

    # Load the PDF using the temporary file path
    file_path = str(save_uploaded_file(pdf_file))
    loader = PyPDFLoader(file_path=file_path)
    docs = loader.load()
    logging.info("PDF file loaded successfully.")
    os.remove(file_path)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(docs)

    faiss_db = FAISS.from_documents(chunks, embedder)
    retriever = faiss_db.as_retriever()
    logging.info("Embeddings created and stored in FAISS vector store.")

    retriever_tool = create_retriever_tool(
        retriever, "RAG doc", "Search the query in the loaded document."
    )
    logging.info("Retriever tool created successfully.")
    return retriever_tool
