import openai
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config.ini')
key = cfg.get("config", "key")
openai.api_key = key

prompt = "iphone 11 com um cachorro atendendo"

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=100
)

print(response["choices"][0]["text"])
