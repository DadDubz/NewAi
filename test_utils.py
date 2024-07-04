import pytest
from unittest.mock import patch, Mock
from utils import upload_image

def test_example():
    assert True

@patch('utils.requests.post')
def test_upload_image(mock_post):
    mock_response = Mock()
    mock_response.json.return_value = {
        'result': {
            'mockup_file_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/PNG_Test.png/715px-PNG_Test.png?20240527104658'
        }
    }
    mock_response.raise_for_status = Mock()
    mock_post.return_value = mock_response

    image_path = 'sample_image.png'
    
    result = upload_image(image_path)
    
    assert result is not None
    assert 'mockup_file_url' in result
    assert result['mockup_file_url'] == 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/PNG_Test.png/715px-PNG_Test.png?20240527104658'
