import pytest 

@pytest.fixture()
def load_image_as_bytes():
    """Load image in bytes."""
    with open("images/resit_sample.jpeg" , 'rb') as image_file:
        image = image_file.read()
        return image
        