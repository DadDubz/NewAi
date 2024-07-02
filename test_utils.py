# test_utils.py

def test_example():
    assert True

def test_generate_image():
    from utils import generate_image
    prompt = "example prompt"
    image_path, image_url = generate_image(prompt)
    assert image_path is not None
    assert image_url is not None

