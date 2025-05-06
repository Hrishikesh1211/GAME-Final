import ollama

def generate_ai_response(prompt, model="mistral", system_prompt=None):
    messages = []

    if system_prompt:
        messages.append({ "role": "system", "content": system_prompt })

    messages.append({ "role": "user", "content": prompt })

    response = ollama.chat(
        model=model,
        messages=messages,
        options={"temperature": 0.85, "top_p": 0.9}
    )

    return response['message']['content']
