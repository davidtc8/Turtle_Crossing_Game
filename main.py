import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('🐢 Turtle Crossing Game 🐢')

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Setting the listening method so we can move our paddle
screen.listen()
screen.onkey(turtle.up, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        # This mean that if the car distance is less than 20 pixels from the turtle, it loses.
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False

    if turtle.ycor() > 280:
        turtle.goto(x = 0, y = -280)
        car_manager.level_up()
        scoreboard.next_level()

screen.exitonclick()
