import turtle as tl

sn = tl.Screen()

class Square:
    def __init__(self, slength, blcornerpos):
        self.slength = slength
        self.blcornerpos = blcornerpos #xy coords in list

    def Construct(self):
        self.newturtle = tl.Turtle()
        self.newturtle.penup()
        self.newturtle.setx(self.blcornerpos[0])
        self.newturtle.sety(self.blcornerpos[1])
        self.newturtle.pendown()
        for i in range(4):
            self.newturtle.forward(self.slength)
            self.newturtle.left(90)

squarelist = []
cartpos = [-200,0]
for i in range(5):
    squarelist.append(Square(20,cartpos))
    cartpos[0] = cartpos[0]+40

    squarelist[i].Construct()

sn.mainloop()
