from fastmcp import FastMCP
from fastmcp.utilities.types import Image

from drawing_mcp import utilities
from drawing_mcp.drawing import Draw, ColorType, Circle, Rectangle, Line, Arc, Polygon

mcp = FastMCP(name="drawing-mcp", version="0.1.0")


@mcp.tool
async def create_drawing(width: int = 600, height: int = 600, background_color: ColorType = (255, 255, 255)) -> Draw:
    """Creates a new drawing and returns it."""
    return Draw(width=width, height=height, background_color=background_color)


@mcp.tool
async def set_canvas_size(drawing: Draw, width: int, height: int) -> Draw:
    """Sets the canvas size and returns the updated drawing."""
    drawing.width = width
    drawing.height = height
    return drawing


@mcp.tool
async def set_background_color(drawing: Draw, color: ColorType) -> Draw:
    """Sets the background color and returns the updated drawing."""
    drawing.background_color = color
    return drawing


@mcp.tool
async def draw_circle(drawing: Draw, x: int, y: int, radius: int, color: ColorType) -> Draw:
    """Draws a circle and returns the updated drawing."""
    drawing.add_shape(Circle(x=x, y=y, radius=radius, color=color))
    return drawing


@mcp.tool
async def draw_rectangle(drawing: Draw, x: int, y: int, width: int, height: int, color: ColorType) -> Draw:
    """Draws a rectangle and returns the updated drawing."""
    drawing.add_shape(Rectangle(x=x, y=y, width=width, height=height, color=color))
    return drawing


@mcp.tool
async def draw_square(drawing: Draw, x: int, y: int, side_length: int, color: ColorType) -> Draw:
    """Draws a square and returns the updated drawing."""
    drawing.add_shape(Rectangle(x=x, y=y, width=side_length, height=side_length, color=color))
    return drawing


@mcp.tool
async def draw_arc(
    drawing: Draw, 
    x1: int, 
    y1: int, 
    x2: int, 
    y2: int, 
    start_angle: float, 
    end_angle: float, 
    color: ColorType
) -> Draw:
    """Draws an arc and returns the updated drawing."""
    drawing.add_shape(Arc(x1=x1, y1=y1, x2=x2, y2=y2, start_angle=start_angle, end_angle=end_angle, color=color))
    return drawing


@mcp.tool
async def draw_line(
    drawing: Draw, 
    x1: int, 
    y1: int, 
    x2: int, 
    y2: int, 
    color: ColorType
) -> Draw:
    """Draws a line and returns the updated drawing."""
    drawing.add_shape(Line(x1=x1, y1=y1, x2=x2, y2=y2, color=color))
    return drawing


@mcp.tool
async def draw_polygon(drawing: Draw, points: list[tuple[int, int]], color: ColorType) -> Draw:
    """Draws a polygon and returns the updated drawing."""
    drawing.add_shape(Polygon(points=points, color=color))
    return drawing


@mcp.tool
async def view_drawing(drawing: Draw) -> Image:
    """Renders the current drawing and returns it as a FastMCP Image."""
    return utilities.pil_to_mcp(drawing.render())


@mcp.tool
async def save_image(drawing: Draw, output: str = "drawing_output.png") -> bool:
    """Saves the current drawing."""
    try:
        img = drawing.render()
        img.save(output)
        return True
    except Exception:
        return False


@mcp.tool
async def clear_drawing(drawing: Draw) -> Draw:
    """Clears all shapes from the drawing and returns the updated drawing."""
    drawing.clear_shapes()
    return drawing


@mcp.tool
async def remove_last_shape(drawing: Draw) -> Draw:
    """Removes the last added shape from the drawing and returns the updated drawing."""
    drawing.remove_last_shape()
    return drawing


def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
