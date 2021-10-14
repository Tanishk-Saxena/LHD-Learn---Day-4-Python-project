from turtle import *

bgcolor("white")
area = Screen()
area.setup(width=1.0, height=1.0)
speed('fastest')

penup()
goto(-200, 100)
pendown()
pencolor("black")
def star(size):
    if size<=10:
        return
    else:
        begin_fill()
        for i in range(5):
            forward(size)
            star(size/3)
            left(216)
        end_fill()

star(360)
done()

