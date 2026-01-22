import io
from fastmcp.utilities.types import Image
from PIL.Image import Image as PILImage

def pil_to_mcp(image: PILImage) -> Image:
    """Converts a PIL Image to a FastMCP Image."""
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    img_bytes = buffer.getvalue()

    return Image(data=img_bytes, format="PNG")