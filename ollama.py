

from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.1', messages=[
  {
    'role': 'user',
    'content': input('Prompt: /n'),
  },
])
print(response['message']['content'], end='\n')

