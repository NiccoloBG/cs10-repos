import turtle

sn = turtle.Screen()
pen = turtle.Pen()

for i in range(12):
    exec('turtle'+str(i)+' = turtle.Turtle()')
    exec('turtle'+str(i)+'.left('+str(i*30)+')')
    exec('turtle'+str(i)+'.penup()')
    exec('turtle'+str(i)+'.forward(100)')
    exec('turtle'+str(i)+'.pendown()')
    exec('turtle'+str(i)+'.forward(20)')
    exec('turtle'+str(i)+'.penup()')
    exec('turtle'+str(i)+'.forward(20)')
    exec('turtle'+str(i)+'.stamp()')

sn.mainloop()
