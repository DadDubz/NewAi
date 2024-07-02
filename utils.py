import openai
import requests
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Correctly retrieve the environment variable values
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PRINTFUL_API_KEY = os.getenv('PRINTFUL_API_KEY')
WIX_API_KEY = os.getenv('WIX_API_KEY')
WIX_ACCOUNT_ID = os.getenv('WIX_ACCOUNT_ID')

openai.api_key = OPENAI_API_KEY

# Map product types to Printful variant IDs (example values)
PRODUCT_TYPE_MAP = {
    "t-shirt": 4011,
    "hat": 4012,
    "shoes": 4013,
    "shorts": 4014,
    "swim_tank": 4015,
    "one_piece_swimsuit": 4016
}

def generate_image(prompt, size='1024x1024'):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size=size
        )
        image_url = response['data'][0]['url']
        image_data = requests.get(image_url).content
        with open('generated_image.png', 'wb') as handler:
            handler.write(image_data)
        return 'generated_image.png', image_url
    except Exception as e:
        print(f"Error generating image: {e}")
        return None, None

def upload_image(image_path):
    try:
        with open(image_path, 'rb') as image_file:
            response = requests.post(
                'https://api.printful.com/mockup-generator/create-task/12',
                headers={'Authorization': f'Bearer {PRINTFUL_API_KEY}'},
                files={'file': image_file}
            )
        response.raise_for_status()
        return response.json()['result']
    except requests.exceptions.RequestException as e:
        print(f"Error uploading image: {e}")
        return None

def create_product(printfile_url, name, price, product_type):
    try:
        variant_id = PRODUCT_TYPE_MAP.get(product_type)
        if not variant_id:
            raise ValueError(f"Invalid product type: {product_type}")

        product_data = {
            'sync_product': {
                'name': name,
                'thumbnail': printfile_url,
                'variants': []
            },
            'sync_variants': [{
                'variant_id': variant_id,
                'retail_price': price,
                'is_ignored': False
            }]
        }
        response = requests.post(
            'https://api.printful.com/store/products',
            headers={
                'Authorization': f'Bearer {PRINTFUL_API_KEY}',
                'Content-Type': 'application/json'
            },
            data=json.dumps(product_data)
        )
        response.raise_for_status()
        return response.json()['result']
    except requests.exceptions.RequestException as e:
        print(f"Error creating product on Printful: {e}")
        return None

def create_wix_product(product_id, name,
