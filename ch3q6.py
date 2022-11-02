import turtle

numsides = [3, 4, 6, 8]
screen = turtle.Screen()
pen = turtle.Turtle()
sidelength = 100

for i in numsides:
    extangle = 360 / i
    for x in range(i):
        pen.forward(sidelength)
        pen.left(extangle)


screen.mainloop()