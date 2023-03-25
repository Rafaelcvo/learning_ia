import openai
import os

with open("config\\pass.txt", "r") as key:
    sk = key.read()

openai.api_key = sk


response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Brainstorm some ideas combining VR and fitness:",
  temperature=0.6,
  max_tokens=150,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)

