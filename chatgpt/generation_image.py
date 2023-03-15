import openai
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config.ini')
key = cfg.get("config", "key")
openai.api_key = key

response = openai.Image.create(
  prompt="image the child see horizonte into glass",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)