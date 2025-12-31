from langgraph.checkpoint.memory import InMemorySaver


def get_memory_saver():
    return InMemorySaver()  # replace it with sqlite memory saver later
