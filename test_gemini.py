import google.generativeai as genai

genai.configure(api_key="AIzaSyA6oDRRYcI7Rz8b_tiHADzPWqjH-kX64TE")  

model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("Say hello in Python.")
print(response.text)
