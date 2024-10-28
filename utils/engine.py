import ollama

def chat(prompt):
    """
    Function to chat with the Ollama model.
    
    Args:
        prompt (str): The prompt to send to the model.

    Returns:
        str: The content of the model's response.
    """
    
    # Prepare the message payload for the API call
    messages = [
        {
            'role': 'user',
            'content': prompt,
        },
    ]
    
    try:
        # Make a call to the Ollama chat API
        response = ollama.chat(model='llama3.2:1b', messages=messages)
        
        # Check if the response contains the expected structure
        if 'message' in response and 'content' in response['message']:
            return response['message']['content']
        else:
            # Log unexpected response structure
            print("Unexpected response structure:", response)
            return "Sorry, I couldn't generate a response."

    except Exception as e:
        # Log the error and provide feedback
        print(f"An error occurred: {str(e)}")
        return "Sorry, an error occurred while processing your request."

# Example usage
if __name__ == "__main__":
    user_prompt = "create database for hotel management system"
    response = chat(user_prompt)
    print("Response from model:", response)
