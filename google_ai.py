
from google import genai

client = genai.Client(api_key="AIzaSyCLGTQ_Bf4jm-hjo13cnw-fd11HrObF0YA")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=input()
)
print(response.text)

