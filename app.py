"""
app.py

Main module to set up the environment, load models, tools, create an agent, and execute queries.
"""

import logging

from agent import create_agent, run_agent
from custom_prompt import get_custom_prompt
from models import load_models
from retriever import create_retriever_from_pdf
from tools import load_tools
from utils import set_api_keys, setup_logging


def process_query(pdf_file, query):
    """Process the query using the RAG agent, considering the uploaded PDF file."""

    setup_logging()
    logging.info("Starting process_query function.")

    # Set API keys
    set_api_keys()

    # Load models
    model, embedder = load_models()

    # Load other tools
    tools = load_tools()

    if pdf_file:
        # Create retriever tool from PDF
        retriever_tool = create_retriever_from_pdf(pdf_file, embedder)
        tools.insert(0, retriever_tool)
        logging.info("PDF file added to the tool list")

    # Get the custom prompt template
    prompt = get_custom_prompt()

    # Create ReAct agent
    agent_executor = create_agent(model, tools, prompt)

    # Initialize agent_scratchpad
    agent_scratchpad = ""

    # Run agent with the query
    response = run_agent(agent_executor, query, agent_scratchpad)
    logging.info("process_query function completed.")
    return response
