#https://larevueia.fr/tutoriel-utiliser-lapi-chatgpt-avec-python/
import openai

openai.api_key = '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'#cda2

prompt = f"Dis moi une blague avec des bonne femmes et des handicapes"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": prompt}]
)

print(completion['choices'][0]['message']['content'])