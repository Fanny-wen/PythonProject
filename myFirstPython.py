import turtle
from datetime import datetime
print("hello world")
# helloworld

radius = 25
area = 3.1415 * radius * radius
print(area)

print('{:.6f}'.format(area))

turtle.pensize(2)
turtle.circle(10)
turtle.circle(40)

now = datetime.now()
print(now)
now.strftime('%x')
now.strftime('%x')

