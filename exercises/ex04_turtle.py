"""Ex04: A Scene - Attempting beyond 85% with dot function and elaboration on use of dot at lines 137-142."""
__author__ = "730406845"

from turtle import Turtle, colormode, tracer, update, done 
colormode(255)


def main() -> None:
    """The entrypoint of my scene. Calls flower_top, flower_stem, and flower_head 3 times each to repeat the flower shape 3 times. Calls 3 other functions 1 time each."""
    tracer(0, 0)
    MAX_SPEED: int = 0

    circle: Turtle = Turtle()
    circle.speed(MAX_SPEED)
    circle.hideturtle()
    circle.fillcolor(235, 214, 15)
    circle.pencolor(196, 178, 8)

    sky: Turtle = Turtle()
    sky.speed(MAX_SPEED)
    sky.hideturtle()
    sky.color(172, 235, 249)
    
    grass: Turtle = Turtle()
    grass.speed(MAX_SPEED)
    grass.hideturtle()
    grass.color(130, 219, 149)
    
    petals: Turtle = Turtle()
    petals.speed(MAX_SPEED)
    petals.hideturtle()
    petals.color(238, 228, 20)

    middle: Turtle = Turtle()
    middle.speed(MAX_SPEED)
    middle.hideturtle()

    stem: Turtle = Turtle()
    stem.speed(MAX_SPEED)
    stem.hideturtle()
    stem.pencolor(5, 112, 43)
    stem.fillcolor(30, 160, 59)

    top(sky, -1000, 0)

    sun(circle, 150, 200)

    ground(grass, -1000, 0)

    flower_top(petals, 30, -100)
    flower_stem(stem, 50, -215)
    flower_head(middle, 55, -87)

    flower_top(petals, -75, -60)
    flower_stem(stem, -80, -215)
    flower_head(middle, -75, -89)

    flower_top(petals, 0, -100)
    flower_stem(stem, -30, -215)
    flower_head(middle, -25, -85)

    update()
    done()


def top(sky: Turtle, x: float, y: float) -> None:
    """Draws the sky of the scene."""
    sky.penup()
    sky.goto(x, y)
    sky.pendown()

    sky.begin_fill()
    sky.forward(2000)
    sky.left(90)
    sky.forward(1500)
    sky.left(90)
    sky.forward(2000)
    sky.left(90)
    sky.forward(1500)
    sky.left(90)
    sky.end_fill()


def sun(circle: Turtle, x: float, y: float) -> None: 
    """Draws the sun in the sky of the scene with a while loop and uses 2 different pen and fill colors other than black and white."""
    circle.penup()
    circle.goto(x, y)
    circle.pendown()
    side_length = 5

    circle.begin_fill()
    i: int = 0
    while (i < 215):
        circle.forward(side_length)
        circle.left(5)
        i = i + 1 
    circle.end_fill()


def ground(grass: Turtle, x: float, y: float) -> None: 
    """Draws the ground of the scene."""
    grass.penup()
    grass.goto(x, y)
    grass.pendown()

    grass.begin_fill()
    grass.forward(2000)
    grass.right(90)
    grass.forward(1500)
    grass.right(90)
    grass.forward(2000)
    grass.right(90)
    grass.forward(1500)
    grass.right(90)
    grass.end_fill()


def flower_top(petals: Turtle, x: float, y: float) -> None:
    """Draws the petals of a flower using a loop; a broken up part/helper function for the flower shape/function."""
    petals.penup()
    petals.goto(x, y)
    petals.pendown()

    side_length = 50

    petals.begin_fill()
    i: int = 0
    while (i < 40):
        petals.forward(side_length)
        petals.left(123)
        i = i + 1 
    petals.end_fill()


def flower_head(middle: Turtle, x: float, y: float) -> None: 
    """Draws the head of the flower using the dot function from the turtle directory. I referenced the turtle directory to find the dot function, defined the function flower_head to use the variable middle (lines 137-142), set the size/color of middle (line 142), established the variable middle in my main function (lines 36-38), and called flower_head to draw the brown dot as the middle of my flower (lines 54, 58, and 62). This is a broken up part/helper function for the flower shape/function."""
    middle.penup()
    middle.goto(x, y)
    middle.pendown()
    middle.dot(25, "brown")


def flower_stem(stem: Turtle, x: float, y: float) -> None:
    """Draws the stem of a flower using 2 different pen and fill colors other than black and white; a broken up part/helper function for the flower shape/function."""
    stem.penup()
    stem.goto(x, y)
    stem.pendown()

    stem.begin_fill()
    stem.forward(10)
    stem.left(90)
    stem.forward(100)
    stem.left(90)
    stem.forward(10)
    stem.left(90)
    stem.forward(100)
    stem.left(90)
    stem.end_fill()


if __name__ == "__main__":
    main()