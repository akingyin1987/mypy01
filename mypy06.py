import turtle

turtle.pen()
turtle.width = 10
turtle.color("red")
for x in range(0, 100, 5):
    turtle.goto(0, x)
    turtle.circle(100 + x)
turtle.done()
