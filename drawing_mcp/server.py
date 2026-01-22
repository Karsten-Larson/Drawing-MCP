from fastmcp import FastMCP
from fastmcp.utilities.types import Image

from drawing_mcp import utilities
from drawing_mcp.drawing import Draw, ColorType, Circle, Rectangle, Line, Arc, Polygon

mcp = FastMCP(name="drawing-mcp", version="0.1.0")

drawer = Draw(width=600, height=600, background_color=(255, 255, 255))

@mcp.tool
async def get_canvas_information() -> dict:
    """Returns the current canvas information."""
    return {
        "width": drawer.width,
        "height": drawer.height,
        "background_color": drawer.background_color,
        "number_of_shapes": len(drawer.shapes.root),
    }

@mcp.tool
async def set_canvas_size(width: int, height: int) -> None:
    """Sets the canvas size to the specified width and height."""
    drawer.width = width
    drawer.height = height

@mcp.tool
async def set_background_color(color: ColorType) -> None:
    """Sets the background color of the canvas."""
    drawer.background_color = color

@mcp.tool
async def draw_circle(x: int, y: int, radius: int, color: ColorType) -> None:
    """Draws a circle at the specified position with the given radius and color."""
    drawer.add_shape(Circle(x=x, y=y, radius=radius, color=color))

@mcp.tool
async def draw_rectangle(x: int, y: int, width: int, height: int, color: ColorType) -> None:
    """Draws a rectangle at the specified position with the given width, height, and color."""
    drawer.add_shape(Rectangle(x=x, y=y, width=width, height=height, color=color))

@mcp.tool
async def draw_square(x: int, y: int, side_length: int, color: ColorType) -> None:
    """Draws a square at the specified position with the given side length and color."""
    drawer.add_shape(Rectangle(x=x, y=y, width=side_length, height=side_length, color=color))

@mcp.tool
async def draw_arc(x1: int, y1: int, x2: int, y2: int, start_angle: float, end_angle: float, color: ColorType) -> None:
    """Draws an arc defined by a bounding box and start/end angles with the given color."""
    drawer.add_shape(Arc(x1=x1, y1=y1, x2=x2, y2=y2, start_angle=start_angle, end_angle=end_angle, color=color))

@mcp.tool
async def draw_line(x1: int, y1: int, x2: int, y2: int, color: ColorType) -> None:
    """Draws a line from (x1, y1) to (x2, y2) with the given color."""
    drawer.add_shape(Line(x1=x1, y1=y1, x2=x2, y2=y2, color=color))

@mcp.tool
async def draw_polygon(points: list[tuple[int, int]], color: ColorType) -> None:
    """Draws a polygon defined by a list of points with the given color."""
    drawer.add_shape(Polygon(points=points, color=color))

@mcp.tool
async def view_drawing() -> Image:
    """Renders the current drawing and returns it as a FastMCP Image."""
    return utilities.pil_to_mcp(drawer.render())

@mcp.tool
async def save_image(output: str = "drawing_output.png") -> bool:
    """Saves the current drawing."""
    try:
        img = drawer.render()
        img.save(output)
        return True
    except Exception:
        return False

@mcp.tool
async def clear_drawing() -> Image:
    """Clears all shapes from the drawing."""
    drawer.clear_shapes()
    return utilities.pil_to_mcp(drawer.render())

@mcp.tool
async def remove_last_shape() -> None:
    """Removes the last added shape from the drawing."""
    drawer.remove_last_shape()

@mcp.tool
async def view_json() -> str:
    """Returns the JSON representation of the current drawing."""
    return drawer.model_dump_json(indent=2)

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
