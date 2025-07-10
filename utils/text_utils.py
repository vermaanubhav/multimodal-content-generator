import openai
import logging

def generate_story(prompt: str, image_description: str) -> str:
    """
    Generates a story based on the user's prompt and an image description.

    Args:
        prompt (str): The user's story prompt.
        image_description (str): Description of the image.

    Returns:
        str: Generated story.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative storyteller."},
                {"role": "user", "content": f"Write a short story based on this idea: '{prompt}' and this image description: '{image_description}'"}
            ],
            max_tokens=400
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        logging.error(f"Failed to generate story: {e}")
        raise
