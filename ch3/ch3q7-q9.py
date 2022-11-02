import random
import turtle as tl

screen = tl.Screen()
pen = tl.Turtle()

testset = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for i in testset:
    pen.forward(100) #with the assumption units = steps
    pen.right(i)

for i in range(int(input('How many more steps forward do you want to predict?'))):
    pen.forward(100)
    pen.right(random.randint(-360, 360))

screen.mainloop()

# q9: 360/18
