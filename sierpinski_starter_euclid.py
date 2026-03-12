# Sierpinski's Triangle with the Euclid Module
# 3.12.2026 @ 12:12 pm

import euclid
from colors import *
import math, time

# The greater the tracer value, the faster the animation.
euclid.createPage(size = (640, 480), color = "LIGHTBLUE", tracer = 50)
logos = euclid.Pen()

def drawTriangle(leftCorner, sideLength, color):
    # Draw a regular triagle with given position of left corner,
    # length of a side and line color.
    x, y = leftCorner[0], leftCorner[1]
    logos.setColor(color)
    logos.up()
    logos.goto(x, y)
    logos.down()
    logos.goto(x + sideLength / 2, y - math.sqrt(3) * sideLength / 2)
    logos.goto(x + sideLength, y)
    logos.goto(x, y)
    logos.up()

def serpTri(leftCorner, sideLength, depth, color):
    if depth == 0:  # The maximum recursion depth is achieved.
        return
    drawTriangle(leftCorner, sideLength, color)
    # Compute location of triangles to be drawn in next recursive call.
    mdptLeft = (leftCorner[0] + sideLength / 4, leftCorner[1] - sideLength * math.sqrt(3) / 4)
    mdptBottom = (leftCorner[0] + sideLength / 2, leftCorner[1])
    # In each resursive call, depth is decreased by 1.
    # When the depth reaches 0, the recurion ends.
    serpTri(leftCorner, sideLength / 2, depth - 1, color)
    serpTri(mdptLeft, sideLength / 2, depth - 1, color)
    serpTri(mdptBottom, sideLength / 2, depth - 1, color)

def draw():
    sideLength = 200
    maxDepth = 8
    leftCorner = (200, 300)
    color = "RED"
    for currDepth in range(1, maxDepth + 1):
        # Arguments sent to serpTri: coordinates of left corner,
        # then side length, then recursion depth, then pen color.
        serpTri(leftCorner, sideLength, currDepth, color)
        euclid.finish()  # Necessary if a tracer has been set.
        time.sleep(2)  # Pause for 2 seconds.
        if currDepth < maxDepth:
          euclid.clear() # Clear the screen.
    euclid.finish()  # Perform the final update.
    
draw()

euclid.finish()
euclid.wait()