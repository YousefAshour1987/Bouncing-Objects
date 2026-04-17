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
    t.ht()
    t.speed(0)
    t.color("red")
    t.penup()
    t.goto(-240, -240)
    t.pendown()
    t.begin_fill()
    t.goto(-240, 240)
    t.goto(240, 240)
    t.goto(240, -240)
    t.goto(-240, -240)
    t.end_fill()
    
# Function 1: Movement using turtle heading (forward + setheading)
def move_heading(t):
    # Move the turtle continuously using forward movement and its current heading.
    # The turtle should update its position each frame using forward().
    # When the turtle hits a boundary:
    #   - Use heading() to check its current direction.
    #   - Calculate the reflection angle based on the wall it hits.
    #   - Use setheading() to update the direction so it "bounces" off the wall.
    # The result should be smooth motion where direction is controlled by angles.
    t.forward(5)
    if t.xcor() > 240 or t.xcor() < -240:
        t.setheading(180 - t.heading())
        t.forward(10)
    elif t.ycor() > 240 or t.ycor() < -240:
        t.setheading(-t.heading())
        t.forward(10)

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
    newX = turtle.xcor() + deltax
    newY = turtle.ycor() + deltay
    # check to see if turtle will leave the right or left side of playing area
    if newX > 240 or newX < -240:
        newX = turtle.xcor()
        deltax *= -1
    # check to see if turtle goes out of bounds on the upper or lower boundary
    if newY > 240 or newY < -240:
        newY = turtle.ycor()
        deltay *= -1

    # sends turtle to the new coordinates
    turtle.goto(newX, newY)
    # return any changes to deltax or deltay
    return deltax, deltay

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)

playing_area()


turtle = Turtle()
turtle.color(generate_color())
turtle.speed(1)
turtle.shape("circle")
turtle.setheading(random.randint(0, 360))
deltax = random.randint(-2, 2) # randomly selects how far to the right/left the turtle will move.
deltay = random.randint(-2, 2) # randomly selects how far to the up/down the turtle will move.


# turtles = [yertle]
# for i in range(10):
#     t = Turtle()
#     t.color(generate_color())
#     t.speed(0)
#     t.setheading(random.randint(0, 360))
#     turtles.append(t)

alive = True
while alive:
    # for turt in turtles:
    #     move_heading(turt)
    deltax, deltay = move_with_deltas(turtle, deltax, deltay)

screen.exitonclick()