from utils import load_image_as_base64


def test_load_image_as_base64(load_image_as_bytes: bytes):
    """Test the load_image_as_base64 function."""
    image_base64 = load_image_as_base64(load_image_as_bytes)
    assert isinstance(image_base64, str), "The output should be a string."
    assert image_base64.startswith("data:image/jpeg;base64,"), "The output should be a \
        base64 encoded string."
