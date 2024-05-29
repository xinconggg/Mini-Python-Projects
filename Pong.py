from turtle import Turtle, Screen


# Initialize Screen size to 800x600 and change background to black
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


# Create a "Paddle" class, inheriting from "Turtle" class
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # Move Paddle Up
    def go_up(self): 
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    # Move Paddle Down
    def go_down(self): 
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


# Create a "Ball" class, inheriting from "Turtle" class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x=0, y=0)
        # Speed of Ball
        self.x_move = 0.5
        self.y_move = 0.5
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    # Collide with Wall
    def bounce_wall(self):
        self.y_move *= -1
    
    # Collide with Paddle
    def bounce_paddle(self):
        self.x_move *= -1
        # Increase Ball Speed
        self.x_move *= 1.3
    
    # Reset Ball Position / Ball Misses Paddle, then start with Other Player
    def reset(self):
        # Reset Ball Speed
        self.x_move = 0.25
        # Reset Position
        self.goto(x=0, y=0)
        # Reverse Direction
        self.x_move *= -1


# Create a "Scoreboard" class, inheriting from "Turtle" class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        # Scoreboard of Left Player
        self.goto(x=-100, y=200)
        self.write(self.left_score, align='center', font=('Courier', 80, 'normal'))
        # Scoreboard of Right Player
        self.goto(x=100, y=200)
        self.write(self.right_score, align='center', font=('Courier', 80, 'normal'))

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()
    
    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()


# Create a Ball,Scoreboard, Left & Right Paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


# Allow Paddle to move Up & Down    
screen.listen()
## Move Right Paddle
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')
## Move Left Paddle
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')

game_over = False
while not game_over:
    screen.update()
    ball.move()

    # Detect Collision with Ceiling/Floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detect Collision with  Paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_paddle()

    # Detect if Right Paddle misses then add to score
    if ball.xcor() > 380:
        scoreboard.left_point()
        ball.reset()

    # Detect if Left Paddle misses then add to score
    if ball.xcor() < -380:
        scoreboard.right_point()
        ball.reset()

screen.exitonclick()