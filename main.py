from turtle import *
import random

# generates a random color
def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

# Creates the rectangular game boundary
def playing_area():
    # Draw a filled rectangle that covers most of the screen,
    # leaving approximately a 20-pixel margin on all sides.
    t = Turtle()
    t.color("red")
    t.begin_fill()
    t.goto(-242.5, -237.5)
    t.setheading(90)
    for i in range(4):
        t.forward(480)
        t.right(90)
    t.end_fill()

# Function 1: Movement using turtle heading (forward + setheading)
def move_with_heading(t):
    # Move the turtle continuously using forward movement and its current heading.
    # The turtle should update its position each frame using forward().
    # When the turtle hits a boundary:
    #   - Use heading() to check its current direction.
    #   - Calculate the reflection angle based on the wall it hits.
    #   - Use setheading() to update the direction so it "bounces" off the wall.
    # The result should be smooth motion where direction is controlled by angles.
    pass


# Function 2: Movement using delta x / delta y (coordinate-based movement)
def move_with_deltas(t, deltax, deltay):
    # Move the turtle by directly updating its x and y position using dx and dy values.
    # Each update step:
    #   - Add deltax to x-coordinate and deltay to y-coordinate.
    # When the turtle hits a boundary:
    #   - Reverse deltax if it hits a left/right wall.
    #   - Reverse deltay if it hits a top/bottom wall.
    # This creates a bounce effect using vector-style movement instead of angles.
    # The turtle’s position should be updated using setx() and sety().
    pass




screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)

playing_area()

screen.exitonclick()