from turtle import Screen, Turtle
import time
import random


# Initialize Screen size to 600x600 pixels
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        # Shape of car
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        # Color of Car
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        chosen_color = colors[random.randint(0, (len(colors) - 1))]
        self.color(chosen_color)
        # Spawn cars
        self.penup()
        spawn_point_y = random.randint(-250, 250)
        self.goto(x=300, y=spawn_point_y)
    
    def move_car(self, level = 0):
        self.backward(5 + level)

    def stop_car(self):
        self.goto(x=self.xcor(), y=self.ycor())


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(x=0, y=-280)
        self.setheading(90)
    
    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)
    
    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
    
    def move_right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())
    
    def move_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())
    
    def reset_position(self):
        self.goto(x=0, y=-280)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(x= -250, y= 250)
        self.write(f"Level: {self.level}", align='left', font=('Courier', 22, 'bold'))
        
    def level_up(self):
        self.level += 1 
        self.update_scoreboard()
    
    def game_over(self):
        self.update_scoreboard()
        self.goto(0,0)
        self.write(f"GAME OVER", align='center', font=('Courier', 22, 'bold'))


player = Player()
scoreboard = Scoreboard()
set_of_cars = []
car_spawn_counter = 0
speed_increment = 0


screen.listen()
# To move player Up, Down, Left & Right
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_down, "s")
screen.onkeypress(player.move_left, "a")
screen.onkeypress(player.move_right, "d")


game_over = False
while not game_over:
    time.sleep(0.1)
    screen.update()
    car_spawn_counter += 1

    # Generate a new car every 5 loops
    if car_spawn_counter == 5:
        new_car = Car()
        set_of_cars.append(new_car)
        car_spawn_counter = 0

    # Move cars
    for car in set_of_cars:
        car.move_car(speed_increment)

        # Remove cars if it exits screen
        if car.xcor() < -320:
            car.hideturtle()
            set_of_cars.remove(car)
    
        # Detect collision
        if player.distance(car) < 20:
            game_over = True
            car.stop_car()
    
        # Player reachers finish line
        if player.ycor() > 280:
            player.reset_position()
            speed_increment += 5
            scoreboard.level_up()
if game_over == True:
    scoreboard.game_over()
            

screen.exitonclick()