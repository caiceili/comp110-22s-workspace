from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
bob: Turtle = Turtle()

leo.speed(25)
leo.hideturtle()

leo.color(70, 70, 70)

leo.penup()
leo.goto(30, 30)
leo.pendown()


leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1 
leo.end_fill()

bob.speed(100)
bob.hideturtle()

bob.color(20, 20, 20)

bob.penup()
bob.goto(30, 30)
bob.pendown()

side_length = 300 * 0.97

bob.begin_fill()
i: int = 0
while (i < 40):
    bob.forward(side_length)
    bob.left(123)
    i = i + 1 
bob.end_fill()

done()
