# app.py

import openai
from PIL import Image
import os
from utils.image_utils import get_image_description
from utils.text_utils import generate_story

# Set your OpenAI API key as an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    print("📷 Multimodal Content Generator")
    image_path = input("Enter the path to your image (e.g., static/sample.jpg): ").strip()
    user_prompt = input("Enter a short idea or theme for the story: ").strip()

    try:
        image_description = get_image_description(image_path)
        print("\n🔍 Detected image content:", image_description)

        story = generate_story(user_prompt, image_description)
        print("\n📝 Generated Story:\n", story)

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
