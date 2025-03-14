

from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='gemma3:4b', messages=[
  {
    'role': 'user',
    'content': input('Prompt: '),
  },
])
print(response['message']['content'], end='\n')

