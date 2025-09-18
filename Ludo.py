import turtle

t=turtle.Turtle()
blue=t.fillcolor("blue")
green=t.fillcolor("green")
red=t.fillcolor("red")
yellow=t.fillcolor("yellow")

t.speed(0)
t.penup()
t.goto(225,225)
t.pendown()
t.right(90)

#boundary
for i in range(4):
    t.forward(450)
    t.right(90)

###right square
t.fillcolor("blue")
t.begin_fill()
t.penup()
t.goto(45,225)
t.pendown()
for i in range(4):
    t.forward(180)
    t.left(90)
t.end_fill()


###bottom right square
t.fillcolor("yellow")
t.begin_fill()
t.penup()
t.goto(45,-225)
t.pendown()
for i in range(4):
    t.left(90)
    t.forward(180)
t.end_fill()


###left square
t.fillcolor("red")
t.begin_fill()
t.penup()
t.goto(-225,45)
t.pendown()
t.left(90)
for i in range(4):
    t.forward(180)
    t.left(90)
t.end_fill()


#bottom left square
t.fillcolor("green")
t.begin_fill()
t.penup()
t.goto(-225,-45)
t.pendown()
for i in range(4):
    t.forward(180)
    t.right(90)
t.end_fill()

    


#center square
t.penup()
t.goto(45,45)
t.pendown()
for i in range(4):
    t.right(90)
    t.forward(90)



#center triangles top
t.fillcolor("blue")
t.begin_fill()
t.right(120)
t.goto(0,0)
t.goto(-45,45)
t.end_fill()

#center triangles left
t.fillcolor("red")
t.begin_fill()
t.left(90)
t.goto(0,0)
t.goto(-45,-45)
t.end_fill()


#center triangles bottom
t.fillcolor("green")
t.begin_fill()
t.right(90)
t.goto(0,0)
t.goto(45,-45)
t.end_fill()


#center triangles right
t.fillcolor("yellow")
t.begin_fill()
t.right(90)
t.goto(0,0)
t.goto(45,45)
t.end_fill()

t.left(30)


#grid right hori color
t.penup()
t.goto(45,-15)
t.pendown()
t.right(180)
t.goto(225,-15)
t.goto(225,15)
t.goto(45,15)
t.fillcolor("yellow")
t.begin_fill()
t.forward(150)
t.right(90)
t.forward(60)
t.right(90)
t.forward(30)
t.right(90)
t.forward(30)
t.left(90)
t.forward(120)
t.end_fill()

#grid right 
t.penup()
t.goto(225,45)
t.pendown()
for _ in range(3):   # repeat 3 times
    t.forward(30)
    t.left(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(90)
    t.left(90)

#a line missed in color so added a line in it
t.penup()
t.goto(195,-15)
t.pendown()
t.goto(165,-15)

#grid left hori color
t.penup()
t.goto(-45,-15)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.forward(150)
t.right(90)
t.forward(60)
t.right(90)
t.forward(30)
t.right(90)
t.forward(30)
t.left(90)
t.forward(120)
t.end_fill()
t.goto(-225,15)
t.goto(-225,-15)
t.goto(-45,-15)


##grid left 
t.penup()
t.goto(-45,45)
t.pendown()
t.right(180)
for _ in range(3):   # repeat 3 times
    t.forward(30)
    t.left(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(90)
    t.left(90)


#grid bottom verti color
t.penup()
t.goto(15,-45)
t.pendown()
t.left(90)
t.fillcolor("green")
t.begin_fill()
t.forward(150)
t.right(90)
t.forward(60)
t.right(90)
t.forward(30)
t.right(90)
t.forward(30)
t.left(90)
t.forward(120)
t.end_fill()
t.goto(-15,-225)
t.goto(15,-225)
t.goto(15,-45)


#grid bottom 
t.penup()
t.goto(45,-225)
t.pendown()

for _ in range(3):   # repeat 3 times
    t.forward(30)
    t.left(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(90)
    t.left(90)


#grid top verti color
t.penup()
t.goto(-15,45)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.forward(150)
t.right(90)
t.forward(60)
t.right(90)
t.forward(30)
t.right(90)
t.forward(30)
t.left(90)
t.forward(120)
t.end_fill()
t.goto(15,225)
t.goto(-15,225)
t.goto(-15,45)


###grid top 
t.penup()
t.goto(-45,225)
t.pendown()

for _ in range(3):   # repeat 3 times
    t.forward(30)
    t.left(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(90)
    t.left(90)


 #white square left top
t.penup()
t.goto(-195,195)
t.pendown()
t.fillcolor("white")
t.begin_fill()
for _ in range(4):
    t.forward(120)
    t.left(90)
t.end_fill()

 #white square right top
t.penup()
t.goto(75,195)
t.pendown()
t.fillcolor("white")
t.begin_fill()
for _ in range(4):
    t.forward(120)
    t.left(90)
t.end_fill()

 #white square left bottom
t.penup()
t.goto(-195,-75)
t.pendown()
t.fillcolor("white")
t.begin_fill()
for _ in range(4):
    t.forward(120)
    t.left(90)
t.end_fill()

 #white square right bottom
t.penup()
t.goto(75,-75)
t.pendown()
t.fillcolor("white")
t.begin_fill()
for _ in range(4):
    t.forward(120)
    t.left(90)
t.end_fill()

##small circles

def circle_rg():
    t.fillcolor("red")
    t.begin_fill()
    t.circle(10)
    t.penup()
    t.forward(60)
    t.pendown()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.forward(210)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.circle(10)
    t.penup()
    t.forward(60)
    t.pendown()
    t.circle(10)
    t.end_fill()

def circle_by():
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10)
    t.penup()
    t.forward(60)
    t.pendown()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.forward(210)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(10)
    t.penup()
    t.forward(60)
    t.pendown()
    t.circle(10)
    t.end_fill()

    
def circle_positioning(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()


circle_positioning(-175,165)
circle_rg()
circle_positioning(-115,165)
circle_rg()
circle_positioning(95,165)
circle_by()
circle_positioning(155,165)
circle_by()

t.done()
