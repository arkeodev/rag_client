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

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action

    (If you have used the PDF tool and did not find the relevant information, then you can use other tools)

    Final Answer: the final answer to the original input question

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
    Final Answer:
    {agent_scratchpad}
    """
    return PromptTemplate(
        input_variables=["input", "tool_names", "tools", "agent_scratchpad"],
        template=template,
    )
