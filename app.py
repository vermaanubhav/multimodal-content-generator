import openai
from PIL import Image, UnidentifiedImageError
import os
import logging
import sys
import argparse
from dotenv import load_dotenv

from utils.image_utils import get_image_description
from utils.text_utils import generate_story

def setup_logging(log_file="app.log"):
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_file, mode="a", encoding="utf-8")
        ]
    )

def load_env():
    """Load environment variables from .env file."""
    load_dotenv()
    logging.info(".env file loaded (if present).")

def validate_env():
    """Ensure required environment variables are set."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logging.error("OPENAI_API_KEY environment variable is not set.")
        raise EnvironmentError("OPENAI_API_KEY environment variable is missing.")
    openai.api_key = api_key

def validate_image_path(image_path):
    """Check if the image path exists and is a valid image."""
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"The image file '{image_path}' does not exist.")
    try:
        with Image.open(image_path) as img:
            img.verify()
    except UnidentifiedImageError:
        raise ValueError(f"The file '{image_path}' is not a valid image.")
    except Exception as e:
        raise ValueError(f"Failed to open image '{image_path}': {e}")

def get_args():
    """Parse CLI arguments for non-interactive use."""
    parser = argparse.ArgumentParser(description="Multimodal Content Generator")
    parser.add_argument("--image", type=str, help="Path to the input image")
    parser.add_argument("--prompt", type=str, help="Short idea or theme for the story")
    return parser.parse_args()

def main():
    setup_logging()
    load_env()
    validate_env()
    logging.info("📷 Multimodal Content Generator started.")

    args = get_args()
    try:
        # User can supply arguments or be prompted interactively
        image_path = args.image or input("Enter the path to your image (e.g., static/sample.jpg): ").strip()
        validate_image_path(image_path)
        user_prompt = args.prompt or input("Enter a short idea or theme for the story: ").strip()
        if not user_prompt:
            raise ValueError("Story prompt cannot be empty.")

        image_description = get_image_description(image_path)
        logging.info(f"Image content detected: {image_description}")
        print("\n🔍 Detected image content:", image_description)

        story = generate_story(user_prompt, image_description)
        print("\n📝 Generated Story:\n", story)
        logging.info("Story generation completed successfully.")

    except Exception as e:
        logging.exception("An error occurred during execution.")
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
