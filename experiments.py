from turtle import*

from random import randint
from classfunctions import*
speed(0)

bgcolor('black')

V = 1

while V < 400:

    r = randint(0,255) 
    g = randint(0,255) 
    b = randint(0,255) 

    colormode(255) 


    pencolor(r,g,b)
    
    
    fd(20 + V)
    rt(20.911)


    V = V+1
    stars(V,"r,g,b")

penup()
goto(-50,-80)
pendown()

write("SpAcE", font = ("Arial", 20))

hideturtle()

exitonclick()
    

