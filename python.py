from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='dolphin-llama3:8b', messages=[
  {
    'role': 'user',
    'content': input('Prompt: '),
  },
])
print(response['message']['content'])


