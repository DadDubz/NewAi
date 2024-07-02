from unittest.mock import patch, Mock
from utils import upload_image

@patch('utils.requests.post')
def test_upload_image(mock_post):
    mock_response = Mock()
    mock_response.json.return_value = {
        'result': {
            'mockup_file_url': 'http://example.com/mockup.png'
        }
    }
    mock_response.raise_for_status = Mock()
    mock_post.return_value = mock_response

    image_path = 'sample_image.png'
    
    result = upload_image(image_path)
    
    assert result is not None
    assert 'mockup_file_url' in result
