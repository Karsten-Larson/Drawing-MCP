# Drawing MCP

A drawing utility that uses the Multi-Command Protocol (MCP) to create images.

## Installation

It is recommended to use `uv` for installation.

```bash
uv sync
```

## Usage

To start the server, run:

```bash
uv run drawing-mcp
```

The server will start listening for commands over standard input/output. You can then send commands to the server to draw shapes, view the drawing, and save it.

## Available Tools

The following tools are available through the MCP server:

- `get_canvas_information()`: Returns the current canvas information.
- `set_canvas_size(width: int, height: int)`: Sets the canvas size to the specified width and height.
- `set_background_color(color: ColorType)`: Sets the background color of the canvas.
- `draw_circle(x: int, y: int, radius: int, color: ColorType)`: Draws a circle at the specified position with the given radius and color.
- `draw_rectangle(x: int, y: int, width: int, height: int, color: ColorType)`: Draws a rectangle at the specified position with the given width, height, and color.
- `draw_square(x: int, y: int, side_length: int, color: ColorType)`: Draws a square at the specified position with the given side length and color.
- `draw_arc(x1: int, y1: int, x2: int, y2: int, start_angle: float, end_angle: float, color: ColorType)`: Draws an arc defined by a bounding box and start/end angles with the given color.
- `draw_line(x1: int, y1: int, x2: int, y2: int, color: ColorType)`: Draws a line from (x1, y1) to (x2, y2) with the given color.
- `draw_polygon(points: list[tuple[int, int]], color: ColorType)`: Draws a polygon defined by a list of points with the given color.
- `view_drawing()`: Renders the current drawing and returns it as a FastMCP Image.
- `save_image(output: str = "drawing_output.png")`: Saves the current drawing.
- `clear_drawing()`: Clears all shapes from the drawing.
- `remove_last_shape()`: Removes the last added shape from the drawing.
- `view_json()`: Returns the JSON representation of the current drawing.
