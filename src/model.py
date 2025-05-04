"""
LLM models that process the image input and generate structure resit output. 
"""
from pydantic import BaseModel
from typing import List
from utils import load_image_as_base64
from agents import Agent , Runner
from dotenv import load_dotenv  
import asyncio

load_dotenv()


class OrderItem(BaseModel):
    """Order Item Content."""
    item_name: str
    item_unit_price: float
    item_quantity: int
    item_total_price: float
    
class Receipt(BaseModel):
    """Recipt Content."""
    date_purchased: str
    store_name: str
    store_address: str
    item_list: List[OrderItem]
    subtotal: float
    service_tax: float
    total: float

def llm_resit_ocr(image: bytes) -> Receipt:
    """Return the rceipt content from the image.

    Args:
        image (bytes): The image file in bytes format.

    Returns:
        Receipt: The receipt content.
    """
    message = {
        "role": "user", 
        "content": [
            {
                "type": "input_image",
                "image_url": load_image_as_base64(image),
            }
        ]
    }

    agent = Agent(
        name="resit_analyzer", 
        model="gpt-4.1-mini",
        instructions="Generate a detailed receipt content from the image.", 
        output_type=Receipt,
    )

    # Create a new event loop if one doesn't exist
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    # Run the async function in the event loop
    result = loop.run_until_complete(Runner.run(
        starting_agent=agent, 
        input=[message],
    ))
    
    if not isinstance(result.final_output, Receipt):
        raise ValueError("Unable to parse the receipt content.")

    return result.final_output

__name__ = [
    "llm_resit_ocr",
]