from turtle import Screen, Turtle
import time
import random


# Initialize Screen size to 600x600 and change background to black
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off automatic screen updates


# Create a "Snake" class
class Snake:
    def __init__(self):
        self.snake = []
        self.create_starting_snake()
        self.head = self.snake[0]
    
    def create_starting_snake(self):
        for i in range(4):
            segment = Turtle(shape='square')
            segment.color("white")
            x_position = i * (-20) # Each segment is 20 pixels from each other
            segment.penup()
            segment.goto(x_position, y=0)
            self.snake.append(segment)
    
    def add_segment(self):
        last_segment = self.snake[-1]
        new_segment = Turtle(shape='square')
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(last_segment.xcor(), last_segment.ycor())
        self.snake.append(new_segment)
    
    def move_snake(self):
        for seg_num in range(len(self.snake) - 1, 0, -1): # for each segments in the list: 'snake'
            new_x = self.snake[seg_num - 1].xcor() # x-coords of the previous segment
            new_y = self.snake[seg_num - 1].ycor() # y-coords of the previous segment
            self.snake[seg_num].goto(new_x, new_y) # Move current segment to position of previous segment
        self.head.forward(20)
    
    def up(self):
        if self.head.heading() != 270: # If snake heading downwards, then it will not be able to head upwards
            self.head.setheading(90) 

    def down(self):
        if self.head.heading() != 90: # If snake heading upwards, then it will not be able to head downwards
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0: # If snake heading towards right, then it will not be able to head towards left
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180: # If snake heading towards left, then it will not be able to head towards right
            self.head.setheading(0)


# Create a "Food" class, inheriting from "Turtle" class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # Change dim of circle from 20x20 to 10x10
        self.color("blue")
        self.speed("fastest")
        self.random_spawn()       
    
    def random_spawn(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y) # Place food on random places of the screen


# Create a "Scoreboard" class, inherting from "Turtle" Class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align='Center', font=('Arial', 20, 'normal'))
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!!!", align='Center', font=('Arial', 20, 'normal'))


# Create a snake, food & scoreboard object
snake = Snake() 
food = Food()
scoreboard = Scoreboard()

# Binding keyboard to moving the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# While game is still running 
game_over = False
score = 0
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.random_spawn()
        snake.add_segment()
        scoreboard.increase_score()
    
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over = True
        scoreboard.game_over()
    
    # Detect collision with body
    for segment in snake.snake:
        if segment == snake.head: # To exclude head of snake from segments
            pass
        elif snake.head.distance(segment) < 10:
            game_over = True
            scoreboard.game_over()


screen.exitonclick()
