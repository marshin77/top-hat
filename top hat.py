import turtle
wn= turtle.Screen()
def hattoppeice():
    
    top= turtle.Turtle()
    top.color("red")
    top.begin_fill()
    for i in range(4):
        top.forward(150)
        top.left(90)
    top.end_fill()
    

def brimofthehat(coordx,coordy):
    front=turtle.Turtle()
    front.penup()
    front.goto(coordx,coordy)
    front.pendown()
    front.color("blue")
    front.begin_fill()
    front.forward(250)
    front.right(90)
    front.forward(50)
    front.right(90)
    front.forward(250)
    front.right(50)
    front.end_fill()
    

def beltbuckleonhat(coordx,coordy):
    belt=turtle.Turtle()
    belt.penup()
    belt.goto(coordx,coordy)
    belt.pendown()
    belt.color("yellow")
    belt.begin_fill()
    belt.forward(150)
    belt.left(90)
    belt.forward(50)
    belt.left(90)
    belt.forward(150)
    belt.right(90)
    belt.end_fill()
    

def cliponhat(coordx,coordy):
    hat=turtle.Turtle()
    hat.penup()
    hat.goto(coordx,coordy)
    hat.pendown()
    hat.color("red")
    hat.begin_fill()
    hat.forward(50)
    hat.left(90)
    hat.forward(150)
    hat.right(90)
    hat.end_fill()
    

def peiceofthehat(coordx,coordy):
    peice=turtle.Turtle()
    peice.penup()
    peice.goto(coordx,coordy)
    peice.pendown()
    peice.color("red")
    peice.begin_fill()
    for i in range(4):
        peice.forward(20)
        peice.left(90)
    peice.end_fill()
    
def length(coordx,coordy):
    length=turtle.Turtle()
    length.penup()
    length.goto(coordx,coordy)
    length.pendown()
    length.color("yellow")
    length.begin_fill()
    length.forward(30)
    length.left(90)
    length.forward(5)
    length.left(90)
    length.forward(30)
    length.right(90)
    length.end_fill()
    

def main():
    hattoppeice()
    brimofthehat(-65,0)
    beltbuckleonhat(0,0)
    cliponhat(50,0)
    peiceofthehat(55,10)
    length(55,20)
main()
wn.exitonclick()

    
