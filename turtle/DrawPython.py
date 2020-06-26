import turtle  # 引入turtle函数库

def drawsnake(radius, angle, length):
    turtle.seth(-40)
    for i in range(length):
        turtle.circle(radius, angle)
        turtle.circle(-radius, angle)
    turtle.circle(radius, angle / 2)
    turtle.forward(40)
    turtle.circle(16, 180)
    turtle.forward(40)
turtle.setup(1000, 500)
turtle.penup()
turtle.forward(-400)
turtle.pendown()
turtle.pensize(20)
turtle.pencolor('gold')
drawsnake(40, 80, 6)
turtle.done()