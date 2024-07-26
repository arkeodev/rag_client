"""
agent.py

This module handles the creation and execution of the ReAct agent.
"""

import logging

from langchain.agents import AgentExecutor, create_react_agent


def create_agent(model, tools, prompt):
    """Creates a ReAct agent using the provided model, tools, and prompt."""
    logging.info("Creating ReAct agent with provided model, tools, and prompt.")
    agent = create_react_agent(model, tools, prompt)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=3,
        return_intermediate_steps=True,
        early_stopping_method="force",
    )
    logging.info("ReAct agent created successfully.")
    return agent_executor


def run_agent(agent_executor, query, agent_scratchpad):
    """Runs the agent with the given query, deciding which tool to use."""
    logging.info(f"Running agent with query: {query}")
    response = agent_executor.invoke(
        {"input": query, "chat_history": [], "agent_scratchpad": agent_scratchpad}
    )
    logging.info(f"Agent response: {response}")
    return response
