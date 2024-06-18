from tkinter import *
from Quiz_Game_GUI_Quiz_Brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Window Setup
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Image Setup
        self.right_img = PhotoImage(file="Quiz_Game_right.png")
        self.wrong_img = PhotoImage(file="Quiz_Game_wrong.png")

        # Canvas Setup
        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question Text Shows Up Here", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Label Setup
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 15, "bold"))
        self.score_label.grid(row=0, column=1)

        # Buttons Setup
        self.right_button = Button(image=self.right_img, highlightthickness=0, bg=THEME_COLOR, command=self.right_pressed)
        self.right_button.grid(row=2,column=0)
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, bg=THEME_COLOR, command=self.wrong_pressed)
        self.wrong_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()
    

    def get_next_question(self):
        # Change background back to white before updating the question
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            # Update Score
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # Disable "Right" & "Wrong" Buttons once the player reached the end of quiz
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz!\n\nYour final score is: {self.quiz.score}/10")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        # If answer is right change background to green, else change to red
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # After 1 second, update the question
        self.window.after(1000, self.get_next_question)