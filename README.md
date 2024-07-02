# NewAi

This project is a web application that uses OpenAI's DALL-E to generate images, integrates with Printful for creating canvas prints, and posts products to a Wix store.

## Requirements

- Python 3.9
- Flask
- Requests
- OpenAI
- Printful API
- Wix API

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/DadDubz/NewAi.git
    cd NewAi
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    - Create a `.env` file in the root directory and add your API keys and other environment variables as shown in the `.env` section.

## Usage

1. Run the Flask app:
    ```bash
    python app.py
    ```

2. Access the application at `http://127.0.0.1:5000`.

## Deployment

The application is deployed using GitHub Actions. On push to the `main` branch, the CI/CD pipeline will:
- Checkout the code
- Set up Python
- Install dependencies
- Run tests
- Deploy to the server

## Security

Ensure that your Flask application is not running in debug mode in a production environment. The `FLASK_DEBUG` environment variable should be set to `False` in production.
