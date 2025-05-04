"""
Utility functions for the project.
"""
import base64

def load_image_as_base64(image_bytes: bytes) -> str:
    """
    Return the base64 encoded string of the image. 
    
    Args:
        imageIO (BytesIO): The image file in BytesIO format.
        
    Returns:
        str: The base64 encoded string of the image.
    """
    # Encode the byte object to base64
    img_str = base64.b64encode(image_bytes).decode('utf-8')
    
    return f"data:image/jpeg;base64,{img_str}"