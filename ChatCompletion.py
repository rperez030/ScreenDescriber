from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-1106-preview",
  messages=[],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)