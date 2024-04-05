import base64
import requests
import os

# OpenAI API Key
api_key = os.getenv('OPENAI_API_KEY')

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "SettingsWindow.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

# Global variable for the prompt
prompt_text = "You are a visual assistant integrated in the NVDA screen reader that helps blind users access visual information that may not be accessible otherwise. I'm hsaring an image which may be an entire window, a partial window or an individual control in an application. Generate a detailed but succinct visual description. If the image is a control, tell the user the type of control and its current state if applicable, the visible label if present, and how the control looks like. If it is a window or a partial window, include the window title if present, and describe the rest of the screen, listing all sections starting from the top, and explaining the content of each section separtely. For each control, inform the user about its name, value and current state when applicable, as well as which control has keyboard focus. Ensure to include all visible instructions and error messages. When telling the user about visible text, do not add additional explanations of the text unless the meanning of the visible text alone is not suficient to understand the context. Don't make comments about the aesthetics, cleanlinesss or overall organization of the UI. If the image does not correspond to a computer screen, just generate a detailed visual description."

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": prompt_text
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is the window title? Don't describe the image, just tell me the window title"
         },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 4096
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())