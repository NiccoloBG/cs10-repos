from math import pi

astate = 'Area is equal to '

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def ReturnPA(self):
        print(astate+str(self.width*self.height))
        print('Perimeter is equal to '+str(2*self.width+2*self.height))

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def ReturnCA(self):
        print(astate+str(pi*self.radius**2))
        print('Circumference is equal to '+str(2*pi*self.radius))

shapeneeded = input('What shape do you need calculations for?\nValid Shapes: Circle, Rectangle')

if shapeneeded == 'Circle':
    circle = Circle(float(input('What is the radius of the circle?')))
    circle.ReturnCA()
elif shapeneeded == 'Rectangle':
    rectangle = Rectangle(float(input('What is the width of the rectangle?')), float(input('What is the height of the rectangle?')))
    rectangle.ReturnPA()
else:
    print('This is not a valid shape!')