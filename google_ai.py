from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='gemma3:latest', messages=[
  {
    'role': 'assistant',
    'content': input("Enter your message: "),
  },
])
print(response['message']['content'])




from scipy import stats

n = 0.95
result = stats.norm.ppf(n) * (3/4) + 9.5
print(result)