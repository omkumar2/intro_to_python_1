from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.2:latest', messages=[
  {
    'role': 'user',
    'content': input(),
  },
])
print(response['message']['content'])

 