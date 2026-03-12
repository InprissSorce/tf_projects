# Sierpinski's Triangle with the Turtle Module
# 3.12.2026 @ 12:12 pm

# Documentation for the Turtle module at:
# https://docs.python.org/3/library/turtle.html

import math, turtle, time

tess = turtle.Turtle()  # Create an instance of type Turtle.
canvas = turtle.Screen()  # Create an instance of type Screen.
canvas.bgcolor("lightblue")  # background color
canvas.tracer(50)  # Render only every 50th frame - increases animation speed.
# canvas.screensize(640, 480) # Throws an exception at CodeHS.
tess.speed(0)  # max draw speed
tess.pensize(1)
tess.hideturtle()  # Remove to see tess.

def drawTriangle(leftCorner, sideLength, color):
    # Draw a regular triagle with given position of left corner,
    # length of a side and line color.
    x, y = leftCorner[0], leftCorner[1]
    tess.color(color)
    tess.penup()
    tess.goto(x, y)
    tess.pendown()
    tess.goto(x + sideLength / 2, y + math.sqrt(3) * sideLength / 2)
    tess.goto(x + sideLength, y)
    tess.goto(x, y)
    tess.penup()

def serpTri(leftCorner, sideLength, depth, color):
    if depth == 0:  # The maximum recursion depth is achieved.
        return
    drawTriangle(leftCorner, sideLength, color)
    # Compute location of triangles to be drawn in next recursive call.
    mdptLeft = (leftCorner[0] + sideLength / 4, leftCorner[1] + sideLength * math.sqrt(3) / 4)
    mdptBottom = (leftCorner[0] + sideLength / 2, leftCorner[1])
    # In each resursive call, depth is decreased by 1.
    # When the depth reaches 0, the recurion ends.
    serpTri(leftCorner, sideLength / 2, depth - 1, color)
    serpTri(mdptLeft, sideLength / 2, depth - 1, color)
    serpTri(mdptBottom, sideLength / 2, depth - 1, color)

def draw():
    sideLength = 250
    maxDepth = 8
    leftCorner = (-150, -50)
    color = "green"
    for currDepth in range(1, maxDepth + 1):
        # Arguments sent to serpTri: coordinates of left corner,
        # then side length, then recursion depth, then line color.
        serpTri(leftCorner, sideLength, currDepth, color)
        canvas.update()  # Necessary if a tracer has been set.
        time.sleep(2)  # Pause for 2 seconds.
        if currDepth < maxDepth:
          tess.clear()  # Clear the screen.
    canvas.update()  # Perform the final update.
    canvas.exitonclick()  # Keep the window open.
    
draw()