import ollama

def chat(prompt):
    response = ollama.chat(model='llama3.2:1b', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    return response['message']['content']