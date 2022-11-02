import turtle as tl


class shape:
    def __init__(self, radius, tsides):
        self.radius = radius
        self.tsides = tsides
        self.tintangle = (tsides - 2) * 180


newshape = shape(int(input("What is the radius?")), int(input("What is the total amount of sides?")))

if newshape.tsides < 3:
    print("This can't construct a closed polygon")
else:
    wn = tl.Screen()
    pen = tl.Turtle()

    for i in range(newshape.tsides):
        pen.forward(2 * newshape.radius)
        pen.left(180 - (newshape.tintangle / newshape.tsides))

    wn.mainloop()

# as newshape.tsides tends to infinity, the shape constructed looks more like a circle
