print('Circle Base Shape Program')

import math as mt
pi = mt.pi

volstate = "Volume is approximately equal to "
sastate = "Surface Area is approximately equal to "


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def ReturnVSA(self):
        print(volstate+str(pi*(self.radius**2)*self.height))
        print(sastate+str(2*(pi*(self.radius**2))+(pi*2*self.radius)*self.height))

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def ReturnVSA(self):
        print(volstate+str((4/3)*pi*(self.radius**3)))
        print(sastate+str(4*pi*(self.radius**2)))

class Cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def ReturnVSA(self):
        print(volstate+str((1/3)*pi*(self.radius**2)*self.height))
        print(sastate+str((pi*(self.radius**2))+pi*self.radius*(mt.sqrt((self.height**2)+(self.radius**2)))))


shapechosen = (input('What type of shape do you need calculations for?\nValid Entries; Cylinder, Sphere or Cone: '))
if shapechosen  == 'Cylinder':
    cylinder = Cylinder(float(input('What is the radius of the Cylinder?')),float(input('What is the height of the Cylinder?')))
    cylinder.ReturnVSA()
elif shapechosen == 'Sphere':
    sphere = Sphere(float(input('What is the radius of the Sphere?')))
    sphere.ReturnVSA()
elif shapechosen == 'Cone':
    cone = Cone(float(input('What is the radius of the Cone?')), float(input('What is the height of the Cone?')))
    cone.ReturnVSA()
else:
    print('This is not a valid shape.')