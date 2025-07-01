# utils/text_utils.py

import openai

def generate_story(prompt, image_context):
    full_prompt = f"You are a creative writer. Write a short story based on the image context: '{image_context}' and user prompt: '{prompt}'. Make it imaginative, engaging, and under 250 words."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a story generator AI."},
            {"role": "user", "content": full_prompt}
        ],
        max_tokens=300,
        temperature=0.8
    )

    return response['choices'][0]['message']['content'].strip()
