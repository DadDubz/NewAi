from dotenv import load_dotenv

load_dotenv()

from flask import Flask, request, jsonify
from utils import generate_image, upload_image, create_product, create_wix_product

app = Flask(__name__)

@app.route('/designs/generate', methods=['POST'])
def generate_design():
    data = request.json
    prompt = data.get('prompt')
    size = data.get('size', '1024x1024')
    
    if not prompt:
        return jsonify({'message': 'Invalid input parameters'}), 400
    
    image_path, image_url = generate_image(prompt, size)
    if not image_path:
        return jsonify({'message': 'An error occurred while generating the design'}), 500

    print(f"Generated Image Path: {image_path}, Image URL: {image_url}")

    return jsonify({'message': 'Design generated successfully', 'designId': image_path, 'imageUrl': image_url})

if __name__ == '__main__':
    app.run(debug=True)
