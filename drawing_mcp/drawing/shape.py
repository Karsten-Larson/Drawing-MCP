from abc import ABC, abstractmethod
from typing_extensions import Annotated, Literal
from pydantic import BaseModel, Field, RootModel
from PIL.ImageDraw import ImageDraw

from typing import Union, override

class Drawable(ABC):
    @abstractmethod
    def draw(self, image_draw: ImageDraw):
        """Draws the shape using the provided ImageDraw object."""
        pass

ColorType = tuple[int, int, int]

class Shape(BaseModel, Drawable):
    color: ColorType

class Point(BaseModel):
    x: int
    y: int
    
class Circle(Shape, Point):
    radius: int = Field(gt=0)
    type: Literal['circle'] = 'circle' # type: ignore

    @override
    def draw(self, image_draw: ImageDraw):
        image_draw.circle((self.x, self.y), self.radius, fill=self.color)

class Square(Shape, Point):
    side_length: int
    type: Literal['square'] = 'square' # type: ignore

    @override
    def draw(self, image_draw: ImageDraw):
        image_draw.rectangle((self.x, self.y, self.x + self.side_length, self.y + self.side_length), fill=self.color)

class Rectangle(Shape, Point):
    width: int
    height: int
    type: Literal['rectangle'] = 'rectangle' # type: ignore

    @override
    def draw(self, image_draw: ImageDraw):
        image_draw.rectangle((self.x, self.y, self.x + self.width, self.y + self.height), fill=self.color)

class Line(Shape):
    x1: int
    y1: int
    x2: int
    y2: int
    type: Literal['line'] = 'line' # type: ignore

    @override
    def draw(self, image_draw: ImageDraw):
        image_draw.line((self.x1, self.y1, self.x2, self.y2), fill=self.color)

class Arc(Line):
    start_angle: float
    end_angle: float
    type: Literal['arc'] = 'arc' # type: ignore

    @override
    def draw(self, image_draw: ImageDraw):
        image_draw.arc((self.x1, self.y1, self.x2, self.y2), self.start_angle, self.end_angle, fill=self.color)

class Polygon(Shape):
    points: list[tuple[int, int]]
    type: Literal['polygon'] = 'polygon' # type: ignore

    @override
    def draw(self, image_draw: ImageDraw):
        image_draw.polygon(self.points, fill=self.color)

type ShapeType = Annotated[
    Union[Circle, Square, Rectangle, Line, Arc, Polygon], 
    Field(discriminator='type')
]

class Shapes(RootModel[list[ShapeType]]):
    root: list[ShapeType] = []