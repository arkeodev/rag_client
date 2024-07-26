"""
models.py

This module handles loading the language models and embedding models.
"""

import logging

from langchain_openai import ChatOpenAI, OpenAIEmbeddings


def load_models():
    """Loads the GPT-4o model and the OpenAI embedding model."""
    logging.info("Loading GPT-4o model and OpenAI embedding model.")
    model = ChatOpenAI(model="gpt-4o")
    embedder = OpenAIEmbeddings()
    logging.info("Models loaded successfully.")
    return model, embedder
