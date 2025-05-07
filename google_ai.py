
from google import genai

client = genai.Client(api_key="AIzaSyDOjRDvAfF_QWKMppG3pWdqIcTJPGdTeKw")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=input()
)
print(response.text)

