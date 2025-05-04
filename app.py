# Import the Turtle and Screen classes from the turtle module
from turtle import Turtle, Screen

# Create a turtle object named 'tim'
tim = Turtle()

# Create a screen object to capture keyboard events
screen = Screen()

# Function to move the turtle forward by 10 units
def move_forward():
    tim.forward(10)

# Function to move the turtle backward by 10 units
def move_backward():
    tim.backward(10)

# Function to turn the turtle left by 10 degrees
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

# Function to turn the turtle right by 10 degrees
def turn_right():
    tim.right(10)

# Function to clear the screen and reset the turtle to its starting state
def clear_screen():
    tim.reset()

# Set up the screen to listen for key presses
screen.listen()

# Bind key presses to corresponding movement functions
screen.onkey(move_forward, "w")   # Press 'w' to move forward
screen.onkey(move_backward, "s")  # Press 's' to move backward
screen.onkey(turn_left, "a")      # Press 'a' to turn left
screen.onkey(turn_right, "d")     # Press 'd' to turn right
screen.onkey(clear_screen, "c")   # Press 'c' to clear the screen

# Close the turtle graphics window when clicked
screen.exitonclick()