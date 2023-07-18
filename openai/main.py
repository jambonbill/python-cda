#https://larevueia.fr/tutoriel-utiliser-lapi-chatgpt-avec-python/
import openai
from dotenv import dotenv_values

config = dotenv_values(".env")

print(config['api_key'])
#exit(0)

openai.api_key = config['api_key']

prompt = f"Dis moi une blague avec des bonne femmes et des handicapes"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": prompt}]
)

print(completion['choices'][0]['message']['content'])