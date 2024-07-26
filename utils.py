"""
config.py

This module handles the configuration and environment setup for the project.
"""

import logging
import os
from pathlib import Path

from dotenv import load_dotenv


def set_api_keys():
    """Sets the necessary API keys for OpenAI and SerpAPI."""
    logging.info("Loading API keys from .env file.")
    load_dotenv()

    openai_api_key = os.getenv("OPENAI_API_KEY")
    serpapi_api_key = os.getenv("SERPAPI_API_KEY")

    if not openai_api_key or not serpapi_api_key:
        logging.error("API keys for OpenAI and SerpAPI must be set in the .env file.")
        raise ValueError(
            "API keys for OpenAI and SerpAPI must be set in the .env file."
        )

    os.environ["OPENAI_API_KEY"] = openai_api_key
    os.environ["SERPAPI_API_KEY"] = serpapi_api_key
    logging.info("API keys loaded successfully.")


def setup_logging():
    """Sets up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,  # Set the default logging level to INFO.
        format="%(asctime)s - %(levelname)s - %(message)s",  # Define the log message format.
        handlers=[logging.StreamHandler()],
    )


def save_uploaded_file(uploaded_file, save_dir="/tmp"):
    """
    Saves an uploaded file to the specified directory and returns the path.
    Works across Unix, macOS, and Windows.

    Args:
    uploaded_file: The uploaded file object from Streamlit.
    save_dir: The directory to save the file. Defaults to '/tmp'.

    Returns:
    The path of the saved file as a pathlib.Path object.
    """
    save_directory = Path(save_dir)
    save_directory.mkdir(parents=True, exist_ok=True)
    file_path = save_directory / uploaded_file.name

    # Write the file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    return file_path
