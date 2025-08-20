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


print("This is a test message to check the functionality of the code.")
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y = np.sin(x) 
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
