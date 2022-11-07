import turtle

sn = turtle.Screen()
pen = turtle.Turtle()

pen.left(180)
for i in range(5):
    pen.left(145)
    pen.forward(100)

sn.mainloop()