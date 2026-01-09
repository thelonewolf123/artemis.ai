from langchain.tools import tool, ToolRuntime

@tool
def get_relevant_memories(query: str, runtime: ToolRuntime)->str:
    """
    Retrieve previously stored memories relevant to the given query.

    Args:
        query (str): Natural language query to search related memories.
        runtime (ToolRuntime): Execution context containing memory access.

    Returns:
        str: Relevant memory snippets, or an empty string if none are found.
    """
    pass
