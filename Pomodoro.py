from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WORK_MIN = 0 #25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

## Timer Reset
def reset_timer():
     window.after_cancel(timer)
     canvas.itemconfig(timer_text, text="00:00")
     timer_label.config(text="Timer")
     checkmark_label.config(text="")
     global reps
     reps = 0


## Timer Mechanism
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60    
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If its the 1st/3rd/5th/7th rep then work for 25 mins
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

    # If its the 2nd/4th/6th rep then break for 5 mins
    if reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    
    # If its the 8th rep then break for 20 mins
    if reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    

## Countdown Mechanism
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        window.after(1000, count_down, count - 1) 
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark += "✔"
        checkmark_label.config(text=mark)


## Window Setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)  

# Canvas Setup for Image & Timer
canvas = Canvas(width=200, height=224, bg=YELLOW)    
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=("Courier", 35, "bold"))
canvas.grid(row=1, column=1)

# Placement of "Timer" & "Checkmark" Labels
timer_label = Label(text="Timer",fg=GREEN, bg= YELLOW, font=("Courier", 30, "bold"))
timer_label.grid(row=0, column=1)
checkmark_label = Label(text="", bg= YELLOW, font=("Courier", 15))
checkmark_label.grid(row=3, column=1)

# Placement of "Start" & Reset Buttons
start_button = Button(text="Start", font=("Arial", 12, "bold"), command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", font=("Arial", 12, "bold"), command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()