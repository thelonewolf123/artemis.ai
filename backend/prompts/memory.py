MEMORY_SELECTION_PROMPT = """
You are an expert extraction algorithm.

Your task is to decide whether a given piece of information should be stored for future conversations (long-term memory) or not.

Analyze the user's message carefully.

If the message contains personal context, preferences, ongoing goals, recurring work topics, or other information useful in future interactions, set:
"store_info": true

Otherwise, if the information is temporary, generic, or unrelated to the user’s context, set:
"store_info": false
"""