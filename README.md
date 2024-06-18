## [Quiz Game](https://github.com/xinconggg/Mini-Python-Projects/blob/master/Quiz%20Game%20(GUI)%20-%20main.py)
- Project Structure: Consists of multiple Python mod
ules (Question, QuizBrain, QuizInterface, and question_data), renamed to comply with Python's naming conventions.
- Data Handling: Fetches quiz questions from the Open Trivia Database API using the requests library, with the question_data variable storing the fetched questions which are parsed to create Question objects.
- Core Classes:
  - Question: Represents a single quiz question with its text and answer.
  - QuizBrain: Manages the quiz logic, tracks the current question, and checks the user's answers.
  - QuizInterface: Uses Tkinter for the GUI, displaying questions, updating scores, and providing feedback on user answers.
- GUI Implementation: The Tkinter-based QuizInterface class creates the main window, score label, question canvas, and buttons for user interaction, including methods for updating the question text, handling button presses, and providing feedback based on user answers.
- Quiz Logic: The quiz progresses by fetching and displaying the next question, checking if the user’s answer is correct, updating the score accordingly, and ends when all questions are answered, disabling the answer buttons and showing the final score.


## [Turtle Crossing](https://github.com/xinconggg/Mini-Python-Projects/blob/master/Turtle%20Crossing.py)
- Game Mechanics: This project implements a simple turtle graphics-based game where the player navigates a turtle character through a traffic of cars. The player controls the turtle using the 'w', 's', 'a', and 'd' keys to move up, down, left, and right respectively. The objective is to avoid collisions with randomly generated cars and reach the finish line at the top of the screen.
- Dynamic Difficulty: As the game progresses, the difficulty increases dynamically. The speed of the cars spawned increases incrementally, providing a greater challenge for the player. This gradual speed increment enhances the game's replay value and adds to the sense of accomplishment as players progress through levels.
- Score Tracking and Game Over: The game includes a scoreboard that displays the current level. Each time the player successfully reaches the finish line, the level increases, and the speed of car spawning increases. If the player collides with any car, the game ends, displaying a "GAME OVER" message on the scoreboard. This clear feedback loop informs the player of their progress and performance within the game.
![2024-05-30 16-04-03(1) (online-video-cutter com)](https://github.com/xinconggg/Mini-Python-Projects/assets/82378681/c4048103-5570-4022-8c62-e6904eacdc16)

## [Flashcard](https://github.com/xinconggg/Mini-Python-Projects/blob/master/Flashcard.py)
- CSV Data Handling: Reads French-English word pairs from CSV files and stores them in a list of dictionaries, tracking learning progress.
- Card Display Functionality: Displays a random French word and flips to show the English translation after 3 seconds.
- Button Functionality: "Right" and "Wrong" buttons let users mark words as known, updating and saving progress.
- GUI Setup: Uses Tkinter for a styled interface with a canvas and buttons for user interaction.
- File Saving: Saves progress by updating words_to_learn.csv with remaining words.
![2024-06-16-14-20-36-_online-video-cutter com_](https://github.com/xinconggg/Mini-Python-Projects/assets/82378681/b0304a41-bda6-417d-b3a7-04e76dbd2186)


## [Pomodoro Timer](https://github.com/xinconggg/Mini-Python-Projects/blob/master/Pomodoro.py)
- Purpose and Functionality: This project implements a Pomodoro timer, a productivity tool that uses timed intervals to break work into focused sessions (25 minutes of work) and short (5 minutes) or long (20 minutes) breaks.
- User Interface: The application features a graphical user interface created with Tkinter. It includes a countdown timer displayed over an image of a tomato, start and reset buttons, and labels for indicating the current phase (work or break) and completed work sessions.
- Core Mechanisms: The timer operates in cycles, with the start_timer function managing the transition between work and break periods based on the number of completed sessions (reps). The count_down function handles the countdown mechanism, updating the timer display every second.
- Customization and Styling: The project uses various constants and configurations to set up colors, font styles, and the overall layout of the application. Labels and buttons are styled for clarity and ease of use.
- Reset Functionality: A reset button allows users to cancel the ongoing timer and reset the display, labels, and internal counters, providing a fresh start for the timer at any point.
  
![Screenshot 2024-06-10 165316](https://github.com/xinconggg/Mini-Python-Projects/assets/82378681/26366aae-4042-4f35-9d4d-223cc817cd9b)
![Work](https://github.com/xinconggg/Mini-Python-Projects/assets/82378681/985d414b-e224-4570-b79d-48ee0561337f) ![Short Break](https://github.com/xinconggg/Mini-Python-Projects/assets/82378681/26fac892-289c-47e9-852f-7d396e564e51) ![Long Break](https://github.com/xinconggg/Mini-Python-Projects/assets/82378681/e002974b-2955-4aea-b8df-7532c122e56c)

## [Password Generator & Manager](https://github.com/xinconggg/Mini-Python-Projects/blob/master/Password%20Generator%20%26%20Manager.py)
- Password Generation: The project includes a feature that generates secure passwords using a mix of letters, numbers, and symbols, ensuring strong and varied password creation.
- User Interface: Built with Tkinter, the GUI includes fields for entering website names, email addresses/usernames, and generated passwords, along with buttons for generating passwords and saving entries.
- Data Storage: It saves the entered and generated data (website, email, password) to a file (data.txt), appending each new entry on a new line, enabling simple password management.
- Error Handling: The program incorporates basic validation to ensure no fields are left empty before saving data, providing user prompts for confirmation and error messages when necessary.
- Usability Features: The interface ensures user-friendly interactions, such as setting focus on the website entry field on startup and clearing entry fields after saving data to streamline the process of adding new passwords.
![2024-06-12 16-09-58 (online-video-cutter com) (1)](https://github.com/xinconggg/Mini-Python-Projects/assets/82378681/d617fb9b-ed7b-4888-9d13-2c749ca58dc4)


## [Guessing US States](https://github.com/xinconggg/Mini-Python-Projects/blob/master/US%20States%20Game.py)
- Interactive Game: Players are prompted to guess the names of US states in an interactive turtle graphics window.
- Data Visualization: Correctly guessed states are displayed on a blank US map image at their respective coordinates.
- CSV Integration: State names and coordinates are loaded from a CSV file, and unguessed states are saved to a CSV file when the game ends.
- User Feedback: The game continuously updates the number of correctly guessed states in the prompt title.
![2024-06-0521-10-31online-video-cutter com-ezgif com-video-to-gif-converter](https://github.com/xinconggg/Mini-Python-Projects/assets/82378681/58e47f43-39ab-452f-95de-1de9f54588c5)


## [Snake Game](https://github.com/xinconggg/Mini-Python-Projects/blob/master/Snake%20Game.py)
- Utilizes "Turtle" graphics library for visual representation and animations for the Snake
![2024-05-29 11-17-51 (online-video-cutter com) (1)](https://github.com/xinconggg/Mini-Python-Projects/assets/82378681/563d5271-2cde-4f7d-b9f3-ec9282a5f471)


## [Turtle Race](https://github.com/xinconggg/Mini-Python-Projects/blob/master/Turtle%20Race.py)
- A simple and interactive game where user bets on turtles racing across the screen
- Utilizes the 'Turtle' module to create and control the turtles
  
![2024-05-2713-53-46online-video-cutter com-ezgif com-video-to-gif-converter](https://github.com/xinconggg/Mini-Python-Projects/assets/82378681/1460abeb-17ce-4173-ae6d-9002df0f09ad)
![Screenshot 2024-05-27 140425](https://github.com/xinconggg/Mini-Python-Projects/assets/82378681/546d480f-5a7e-487f-a41e-7f925492ab2f)

## [Pong](https://github.com/xinconggg/Mini-Python-Projects/blob/master/Pong.py)
- A simple Pong game with paddles controlled by the keyboard and keeps track of scores using a scoreboard
- Utilizes "Turtle" module for keeping track of scores and animation of paddles and ball
![2024-05-29-21-50-46_IGuMwaWv-ezgif com-crop (1)](https://github.com/xinconggg/Mini-Python-Projects/assets/82378681/1b4e591b-4465-4d43-85dc-ce4bdd58c0cd)


## [Etch-A-Sketch](https://github.com/xinconggg/Mini-Python-Projects/blob/master/Etch-A-Sketch.py)
**Control Mapping**
- W: Move Forward
- S: Move Backward
- A: Counter-Clockwise
- D: Clockwise
- C: Reset Drawing

![2024-05-2712-08-36-ezgif com-crop](https://github.com/xinconggg/Mini-Python-Projects/assets/82378681/795fc2f2-3f51-4a82-8950-9cd790c596f4)

## [NATO Alphabets](https://github.com/xinconggg/Mini-Python-Projects/blob/master/NATO%20Alphabet.py)
- Data Handling: The project involves handling and manipulating data using dictionaries and DataFrames with the pandas library, showcasing how to loop through dictionaries and DataFrame rows.
- Phonetic Alphabet Conversion: It reads data from a CSV file containing the NATO phonetic alphabet, creating a dictionary that maps each letter to its corresponding phonetic code word.
- Output Generation: The project outputs a list of phonetic code words corresponding to the input word, demonstrating how to generate and display a transformed list based on user input.
- Practical Application: This project exemplifies practical applications of data handling, user input processing, and data transformation using Python and pandas, with potential uses in educational tools and communication aids.

![Screenshot 2024-06-07 143135](https://github.com/xinconggg/Mini-Python-Projects/assets/82378681/f7326865-69ce-4822-89b1-480ba48d4082)
![Screenshot 2024-06-07 143210](https://github.com/xinconggg/Mini-Python-Projects/assets/82378681/71ef328e-8e3d-47e6-bb00-64f5d039f729)

## [ISS Tracker (API)](https://github.com/xinconggg/Mini-Python-Projects/blob/master/ISS%20Tracker%20(API).py)
- Objective: The project aims to send an email notification when the International Space Station (ISS) is overhead at the user's location during nighttime.
- ISS Position  & Nighttime Check: Uses the http://api.open-notify.org/iss-now.json API to get the current latitude and longitude of the ISS, and compares the ISS position with the user's location (within a 5-degree range) to determine if the ISS is overhead. Utilizes the https://api.sunrise-sunset.org/json API to get the sunrise and sunset times for the user's location, and determines if the current time is outside the period between sunrise and sunset, indicating nighttime.
- Email Notification: If both the ISS is overhead and it is nighttime, the program sends an email notification to the user using the smtplib library to connect to Gmail's SMTP server, authenticate, and send the email.
- Continuous Monitoring: The script runs continuously, checking every 60 seconds if the ISS is overhead and if it is nighttime, combining both conditions to ensure the notification is sent only when both are true.
- User Configuration: Requires user input for email credentials (my_email and my_password) and geographic coordinates (my_latitude and my_longtitude), ensuring that the email is sent to the user’s specified email address when the conditions are met.

## [Automated Email Sender (Motivational Quotes)](https://github.com/xinconggg/Mini-Python-Projects/blob/master/Automated%20Email%20Sender%20(Quotes).py) & [Automated Email Sender (Birthday)](https://github.com/xinconggg/Mini-Python-Projects/blob/master/Automated%20Email%20Sender%20(Birthday).py)
- Objective: Both projects aim to improve user experience and engagement through timely and relevant email communication. The Monday Motivational Quotes project focuses on providing weekly inspiration. The Birthday Reminder project focuses on acknowledging and celebrating birthdays with personalized messages.
- Email Automation: Both projects involve sending automated emails using the smtplib module to ensure timely delivery of messages. Emails are sent securely by using the starttls method to encrypt the connection.
- Use of datetime Module: Both projects utilize the datetime module to work with current dates. In the Monday Motivational Quotes project, it checks if the current day is Monday. In the Birthday Reminder project, it creates a tuple of the current month and day to match against birthdays.
- File Handling: Both projects involve reading content from files to get the necessary data. The Monday Motivational Quotes project reads quotes from a text file (quotes.txt). The Birthday Reminder project reads birthday data from a CSV file (birthdays.csv) and letter templates from text files (letter_1.txt, letter_2.txt, letter_3.txt).
- Personalization: The Birthday Reminder project personalizes the email content by replacing the placeholder [NAME] in the letter templates with the birthday person's name. The Monday Motivational Quotes project, while not personalized for the recipient, provides a motivational message to start the week.


