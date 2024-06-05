import turtle
import pandas

# Intiate Screen & Set turtle to an image of blank US States
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create a list from the csv file which contains all the states
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    # Prompt player to input answer
    answer = (screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")).title()

    # If player's guess is correct, get coordinates of the state & print the name of state:
    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
    
    # If stops the game then generate a .csv file with the missing states' name
    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States that weren't guessed.csv")
        break

# States