import openai
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config.ini')
key = cfg.get("config", "key")
openai.api_key = key

prompt = "fale sobre a inteligencia de dados"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt = prompt,
  temperature=0,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response["choices"][0]["text"])