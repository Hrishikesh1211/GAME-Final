def room_prompt(state):
    return f"""
You are a horror narrator. The player enters a haunted room.
Their sanity is {state.sanity}.
Describe the room in 2–3 eerie sentences.
Include one disturbing detail or ghostly presence.
Keep the tone chilling and concise.
"""
