import openai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def generate_story(prompt, image_context):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    client = openai.OpenAI()

    full_prompt = f"You are a creative writer. Write a short story based on the image context: '{image_context}' and user prompt: '{prompt}'. Make it imaginative, engaging, and under 250 words."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a story generator AI."},
            {"role": "user", "content": full_prompt}
        ],
        max_tokens=300,
        temperature=0.8
    )

    return response.choices[0].message.content.strip()
