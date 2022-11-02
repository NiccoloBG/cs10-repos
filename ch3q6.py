import turtle

numsides = [3, 4, 6, 8]
screen = turtle.Screen()
pen = turtle.Turtle()

for i in numsides:
    for x in range(i):
        pen.forward(100)
        pen.left(360/i)


screen.mainloop()