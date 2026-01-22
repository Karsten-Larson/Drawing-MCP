from pydantic import BaseModel, Field
from .shape import Shapes, ShapeType, ColorType
from PIL import Image, ImageDraw

class Draw(BaseModel):
    width: int = Field(default=600, gt=0)
    height: int = Field(default=600, gt=0)
    background_color: ColorType = Field(default=(255, 255, 255))
    shapes: Shapes = Field(default_factory=Shapes)

    def add_shape(self, shape: ShapeType) -> None:
        """Adds a shape to the drawing queue."""
        self.shapes.root.append(shape)

    def remove_last_shape(self) -> None:
        """Removes the last added shape from the drawing queue."""
        if self.shapes.root:
            self.shapes.root.pop()

    def clear_shapes(self) -> None:
        """Clears all shapes from the drawing queue."""
        self.shapes.root.clear()

    def render(self) -> Image.Image:
        """Renders all added shapes onto the image."""

        # Create a new blank image
        image = Image.new('RGB', (self.width, self.height), color=self.background_color)
        image_draw = ImageDraw.Draw(image)

        # Draw all shapes
        for shape in self.shapes.root:
            shape.draw(image_draw)

        # Returns the created image
        return image