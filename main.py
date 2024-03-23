from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
# setup screen size
screen.setup(width=500, height=400)
# ask for user input
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
# Create an empty dictionary to store the turtles
all_turtles = []

for i in range(0, 6):
    # This line creates a new Turtle object with the specified shape ("turtle")
    turtle = Turtle(shape="turtle")
    # turtle.shapesize(stretch_wid=2, stretch_len=2)  # default size is 20x20
    # if we don't put inside a dict, it won't be accessible outside this loop
    turtle.color(colors[i])
    turtle.penup()
    # turtles[turtle_name].goto(x=-230, y=-100 + i * 40)
    turtle.goto(x=-230, y=y_positions[i])
    # append new turtle to all_turtles list
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:  # default turtle's cursor width is 20, but heads is over 20
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)  # inclusive
        turtle.forward(rand_distance)

screen.exitonclick()
