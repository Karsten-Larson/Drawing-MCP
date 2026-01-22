import shape
from draw import Draw

def main():
    # drawer = Draw()

    with open('drawing.json', 'r') as f:
        drawer = Draw.model_validate_json(f.read())

    # drawer.add_shape(shape.Circle(x=50, y=50, radius=40, color='blue'))
    # drawer.add_shape(shape.Rectangle(x=100, y=50, width=80, height=40, color='red'))
    # drawer.add_shape(shape.Line(x1=200, y1=50, x2=300, y2=100, color='green'))
    # drawer.add_shape(shape.Arc(x1=150, y1=150, x2=250, y2=200, start_angle=0, end_angle=180, color='purple'))

    img = drawer.render()
    img.save('output.png')

    drawer.remove_last_shape()
    img2 = drawer.render()
    img2.save('output_no_arc.png')

    # with open('drawing.json', 'w') as f:
    #     f.write(drawer.model_dump_json(indent=4))

if __name__ == "__main__":
    main()
