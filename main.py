from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
bet = screen.textinput("Place your bet!", "Which turtle will win the race? Pick a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x = - screen.window_width() / 2 + 30
y = screen.window_height() / 2 - 30

turtles = []
# creating a list of turtles
for num_turtles in range(0, 6):
    turtles.append(Turtle())

color_index = 0
for turtle in turtles:
    # sending turtles to their locations, giving them the right shape and color
    turtle.up()
    turtle.goto(x, y)
    y -= 66
    turtle.shape("turtle")
    turtle.color(colors[color_index])
    color_index += 1

if bet:
    is_race_on = True

winner = ""
while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= screen.window_width()/2 - 30:
            winner = turtle.fillcolor()
            is_race_on = False

if winner == bet:
    print(f"You won! The {winner} turtle is the winner!")
else:
    print(f"Sorry, you did not win. {winner.capitalize()} won instead.")

screen.exitonclick()
