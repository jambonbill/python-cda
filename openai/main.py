#https://larevueia.fr/tutoriel-utiliser-lapi-chatgpt-avec-python/
import openai

openai.api_key = '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'#test1

prompt = f"Dis moi une blague avec des bonne femmes et des handicapes"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": prompt}]
)

print(completion['choices'][0]['message']['content'])