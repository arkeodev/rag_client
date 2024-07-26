"""
tools.py

This module handles loading and configuration of various tools used by the agent.
"""

import logging

from langchain.tools import Tool
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities import (
    ArxivAPIWrapper,
    SerpAPIWrapper,
    WikipediaAPIWrapper,
)


def load_tools():
    """Loads the various tools used by the agent."""
    logging.info("Loading tools for the agent.")

    arxiv = ArxivAPIWrapper()
    logging.info("Arxiv tool loaded.")

    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    logging.info("Wikipedia tool loaded.")

    serpapi = SerpAPIWrapper()
    logging.info("SerpAPI tool loaded.")

    wiki_tool = Tool.from_function(
        func=wikipedia.run,
        name="wiki",
        description="Useful for searching topics on Wikipedia.",
    )

    arxiv_tool = Tool.from_function(
        func=arxiv.run,
        name="arxiv",
        description="Useful for querying the arxiv repository.",
    )

    serpapi_tool = Tool.from_function(
        func=serpapi.run, name="serpapi", description="Search Engine"
    )

    tools = [wiki_tool, arxiv_tool, serpapi_tool]
    logging.info("All tools loaded successfully.")
    return tools
