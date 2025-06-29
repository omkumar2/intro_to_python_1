from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='gemma3:latest', messages=[
  {
    'role': 'assistant',
    'content': input("Enter your message: "),
  },
])
print(response['message']['content'])


