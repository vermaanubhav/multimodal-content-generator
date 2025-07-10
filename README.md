# Multimodal Content Generator

A production-ready CLI tool to generate creative stories based on images and user prompts using OpenAI.

## Features

- Analyze an image and generate a description.
- Use OpenAI's language models to generate a story based on both the image and a user prompt.
- Robust error handling, logging, and environment variable management.
- Supports both interactive and command-line usage.

## Setup

1. Clone the repo.
2. Copy `.env.example` to `.env` and add your OpenAI API key:

   ```
   cp .env.example .env
   # Then edit .env and add your key
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

### Command-line

```bash
python app.py --image static/sample.jpg --prompt "A sunny day in the city"
```

### Interactive

```bash
python app.py
# Follow the prompts
```

## Logging

- Logs are written to both the console and `app.log`.

## Tests

- You are encouraged to add tests under a `tests/` directory for all major functions.

## Directory Structure

```
multimodal-content-generator/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── utils/
│   ├── __init__.py
│   ├── image_utils.py
│   └── text_utils.py
└── static/
    └── sample.jpg
```

## License

MIT
