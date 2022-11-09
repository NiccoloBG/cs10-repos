import turtle as tl

sn = tl.Screen()
pen = tl.Turtle()

for i in range(5):
    for x in range(4):
        pen.forward(20)
        pen.left(90)
    pen.penup()
    pen.forward(40)
    pen.pendown()

sn.mainloop()
