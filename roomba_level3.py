# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 3 version of the room
window = room.draw_room(level = 3, radius = 5)

###
# Start your code here
 
for i in range (4):
    forward(40)
    right(90)
    forward(3*40)
    left(90)
    forward(40)
    right(90)
    forward(40)
    left(90)
    forward(3*40)
    right(90)
    forward(40)
    right(180)

forward(2*40)
right(90)

for i in range (4):
    forward(2*40)
    left(90)
    forward(40)
    right(90)
    forward(40)
    left(90)
    forward(2*40)

left(90)
forward(40)
right(90)

for i in range (4):
    forward(40)
    left(90)
    forward(40)
    right(90)
    forward(40)
    left(90)
    forward(40)

left(90)
forward(40)

for i in range (4):
    forward(40)
    right(90)
    forward(40)
    right(180)
 
# End your code here
###
 
window.exitonclick()