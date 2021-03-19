"""Paint, for drawing shapes.
Team 3: 
Carolina Ortega 
Yossi Khebzou
Alejandro Gaviria

Exercises

1. Add a color.
2. Complete circle
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

import turtle
from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    fillcolor("pink")
    radius= 50 #Set the size of the radius for the circle
    #circle(radius)
    turtle.circle(radius) #Command circle paints circle with turtle
    turtle.left(90) #Turn of 90 degrees to the left while circle is colored
    end_fill()



def rectangle(start, end):
    "Draw rectangle from start to end."
    pass  # TODO
 
    begin_fill()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    end_fill()
    penup()
def triangle(start, end):
    "Draw triangle from start to end."
	
    pass  # TODO

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value


#state = {'start': None, 'shape': line}
state = {'start': None, 'shape': circle}
setup(420, 420, 370, 0)
onscreenclick(tap)

listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('pink'), 'P')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: color('cyan'), 'C')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
onkey(lambda: color('orange'), 'O')
onkey(lambda: color('cyan'),'A')
done()

