from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
BLACK = "#000000"

# Read csv
try:
    data = read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

## Choose & Display next card from "data"
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_language, text="French", fill=BLACK)
    canvas.itemconfig(card_word, text=current_card["French"], fill=BLACK)
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)      # Flip card after 3s

## Flipping of card
def flip_card():
    canvas.itemconfig(card_language, text="English", fill=WHITE)
    canvas.itemconfig(card_word, text=current_card["English"], fill=WHITE)
    canvas.itemconfig(card_background, image=card_back_img)

## If user knows the current card, remove the card from "to_learn" then save the words to learn to an Excel file and call the next card
def is_known():
    to_learn.remove(current_card)
    data = DataFrame(to_learn)
    data.to_csv("words_to_learn.csv")
    next_card()

# Window Setup
window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flip card after 3s
flip_timer = window.after(3000, func=flip_card)      

# Image Setup
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
right_img = PhotoImage(file="right.png")
wrong_img = PhotoImage(file="wrong.png")

# Canvas Setup
canvas = Canvas(width=800, height=526)
card_background = canvas.create_image(400, 263, image=card_front_img)
card_language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Placement of "Right" & "Wrong" Buttons
right_button = Button(image=right_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()