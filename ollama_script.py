from ollama_script import chat
from ollama_script import ChatResponse

response: ChatResponse = chat(model='llama3.1', messages=[
  {
    'role': 'user',
    'content': input('Prompt: '),
  },
])
print(response['message']['content'])


