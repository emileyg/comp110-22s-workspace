"""EX04_turtle - A lake scene with four evergreen trees."""

__author__ = "730388479"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    lake: Turtle = Turtle()
    lake_outline(lake, -640, -200, 1280, 140)
    grass: Turtle = Turtle()
    grass_outline(grass, -640, -140, 1280, 60)
    tree_stumps: Turtle = Turtle()
    tree_stumps_outline(tree_stumps, -550, -140, 50)
    tree_stumps_outline(tree_stumps, 75, -140, 50)
    tree_tops: Turtle = Turtle()
    tree_tops_outline(tree_tops, -625, -90, 200)
    tree_tops_outline(tree_tops, 0, -90, 200)
    done()


def lake_outline(lake: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Draw the lake outline (a rectangle), with a given width and length, whose top left corner is located at x, y."""
    lake.ht()
    lake.penup()
    lake.goto(x, y)
    lake.setheading(0.0)
    lake.pencolor(0, 0, 0)
    lake.fillcolor(46, 81, 235)
    lake.pendown()
    lake.begin_fill()
    i: int = 0
    while i < 4:
        if i == 0 or i == 2:
            lake.forward(length)
            lake.right(90)
        else:
            lake.forward(width)
            lake.right(90)
        i += 1
    lake.end_fill()


def grass_outline(grass: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Draw the grass outline (a rectangle), with a given width and length, whose top left corner is located at x, y."""
    grass.ht()
    grass.penup()
    grass.goto(x, y)
    grass.setheading(0.0)
    grass.pencolor(0, 0, 0)
    grass.fillcolor(27, 212, 40)
    grass.pendown()
    grass.begin_fill()
    i: int = 0
    while i < 4:
        if i == 0 or i == 2:
            grass.forward(length)
            grass.right(90)
        else:
            grass.forward(width)
            grass.right(90)
        i += 1
    grass.end_fill()


def tree_stumps_outline(tree_stumps: Turtle, x: float, y: float, width: float) -> None:
    """Draw the tree stumps outline (squares), with a given width, whose bottom left corner is located at x, y."""
    add_stump: int = 0
    z: int = 0
    while add_stump < 2:
        tree_stumps.ht()
        tree_stumps.penup()  
        tree_stumps.goto(x + z, y)
        tree_stumps.setheading(90.0)
        tree_stumps.pencolor(108, 48, 15)
        tree_stumps.fillcolor(108, 48, 15)
        tree_stumps.pendown()
        tree_stumps.begin_fill()
        i: int = 0
        while i < 4:
            tree_stumps.forward(width)
            tree_stumps.right(90)
            i += 1
        tree_stumps.end_fill()
        add_stump += 1 
        z += 250
    

def tree_tops_outline(tree_tops: Turtle, x: float, y: float, length: float) -> None:
    """Draw the tree tops outline (triangles), with a given length, whose bottom left corner is located at x, y."""
    add_top: int = 0
    z: int = 0
    while add_top < 2:
        tree_tops.ht()
        tree_tops.penup()
        tree_tops.goto(x + z, y)
        tree_tops.setheading(0.0)
        tree_tops.pencolor(42, 108, 5)
        tree_tops.fillcolor(42, 108, 5)
        tree_tops.pendown()
        tree_tops.begin_fill()
        i: int = 0
        while i < 3:    
            tree_tops.forward(length)
            tree_tops.left(120)
            i += 1
        tree_tops.end_fill()
        add_top += 1 
        z += 250


if __name__ == "__main__": 
    main()
