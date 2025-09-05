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

# Draw the Level 2 version of the room
window = room.draw_room(level = 2)

###
# Start your code here

fr=19
fd=14

left(90)

def move(loop):
    forward((fr-loop)*40)
    right(90)
    forward((fd-loop)*40)
    right(90)
    forward((fr-loop)*40)
    right(90)
    forward((fd-loop)*40)
    right(90)

move(0)
move(1)
move(2)
move(3)
move(4)
move(5)
move(6)
move(7)
move(8)
move(9)
move(10)
move(11)
move(12)
move(13)
 
# End your code here
###
 
window.exitonclick()