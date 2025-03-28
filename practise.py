

try:
    from ollama import chat
    from ollama import ChatResponse

    response: ChatResponse = chat(model='gemma3:4b', messages=[
        {
            'role': 'user',
            'content': input('Prompt: '),
        },
    ])
    print(response['message']['content'], end='\n')
except ImportError as e:
    print(f"Error importing ollama: {e}")
    print("Please make sure ollama package is installed using 'pip install ollama'")
except Exception as e:
    print(f"An error occurred: {e}")