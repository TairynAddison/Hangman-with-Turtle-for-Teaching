#Created by Tairyn Addison for CodeFu

import turtle

screen = turtle.Screen().bgcolor("light blue")

pen = turtle.Turtle() 


#Remember the capital T
#pen.speed(0) #A speed of 0 makes him go as fast as possible

pen.pu() #pu is short for penup. Either work, you can use them interchangeably
#pen.setpos(0,0)
pen.pd() #pd is short for pendown

#if finished, add win to turtle.write and main
def hangman(num):
    if num == 6:
        #Do Nothing
        pass
    if num == 5:  #Head        
        # start the filling color
        pen.begin_fill()
        pen.width(5)
        pen.color("blue", "pink")
        pen.circle(25)
        #add colors to parts if waiting

        #DONT do:
        # set the fillcolor
        #t.fillcolor("pink")    
                
        # ending the filling of the color
        pen.end_fill()
    if num == 4:
        #Body
        #color here #if waiting add thickness pen.width()
        pen.goto(0,0)
        pen.seth(270)
        pen.forward(50)
        
    if num == 3:
        # Left Arm
        pen.setpos(0,-10)
        pen.goto(-20,-20)
        pen.up()

    if num == 2:
        # Right Arm
        pen.down()
        pen.setpos(0,-10)
        pen.goto(20, -20)
        pen.up()

    if num == 1:
        # Left Leg
        pen.setpos(0,-50)
        pen.down()
        pen.goto(-20,-70)
        pen.up()

    if num == 0:
        # Right Leg
        pen.setpos(0,-50)
        pen.down()
        pen.goto(20,-70)
        pen.up()

    else:
        pass
     
     

def hello():
    print("hello")

def head():
    #pen.seth(90) #seth is short for set_heading, and it changes the direction pen is facing.
    
    # start the filling color
    pen.begin_fill()
    pen.color("orange", "pink")
    pen.circle(25)
    #add colors to parts if waiting

    #DONT do:
    # set the fillcolor
    #t.fillcolor("pink")    
    
    #circle
    # ending the filling of the color
    pen.end_fill()
    

def body():
    #color here
    pen.seth(270)
    pen.forward(50)

def arms(num):
    if(num == 1):
        pen.setpos(0,-10)
        pen.goto(-20,-20)
    else:
        pen.setpos(0,-10)
        pen.goto(20,-20)

