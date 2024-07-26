"""
custom_prompt.py

This module contains the custom prompt for the ReAct agent to prioritize the PDF retriever tool.
"""

from langchain.prompts import PromptTemplate


def get_custom_prompt():
    """Returns the custom prompt template for the ReAct agent."""
    template = """
        Answer the following questions as best you can. You have access to the following tools:

        {tools}

        Use the following format:

        Question: {input}
        Thought: Consider what information is needed and how to obtain it.
        Action: Choose one of the following actions [{tool_names}]
        Action Input: Provide the necessary input for the chosen action
        Observation: Record the result of the action

        (If the relevant information is not found using the PDF tool, use other available tools.)

        Final Answer: Provide a comprehensive answer to the original question

        Begin!

        Question: {input}
        Thought: Let's first check the PDF document to see if it contains the information.
        Action: RAG doc
        Action Input: {input}
        Observation:

        Thought: If the information was not found in the PDF, let's try other tools.
        Action: [tool_names]
        Action Input: {input}
        Observation:

        Thought: I have now gathered all the necessary information.
        Final Answer: {agent_scratchpad}
    """
    return PromptTemplate(
        input_variables=["input", "tool_names", "tools", "agent_scratchpad"],
        template=template,
    )
