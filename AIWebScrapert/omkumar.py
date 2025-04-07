from google import genai

client = genai.Client(api_key="your api")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=input()
)
print(response.text)

