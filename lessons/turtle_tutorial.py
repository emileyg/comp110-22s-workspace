from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.color(99, 204, 250)
# leo.color("blue")

leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")

leo.speed(50)

leo.penup()
leo.goto(0, 0)
leo.pendown()

side_length: float = 300.0

leo.begin_fill()
# Exercise One
i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.right(120)
    i += 1
leo.end_fill()

# leo.hideturtle()

bob: Turtle = Turtle()
bob.color("black", "black")
bob.penup()
bob.goto(0, 0)
bob.pendown()
bob.speed(80)

i: int = 0
while (i < 30):
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.right(123)
    i += 1


# # Exercise One
# i: int = 0
# while (i < 4):
#     leo.forward(100)
#     leo.left(90)
#     i += 1

# # Exercise Zero
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)


# # Square Attempt
# leo.forward(100)
# leo.left(90)
# leo.forward(100)
# leo.left(90)
# leo.forward(100)
# leo.left(90)
# leo.forward(100)

# leo.forward(50)
# leo.left(30)
# leo.right

done()