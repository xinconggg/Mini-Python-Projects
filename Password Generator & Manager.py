from tkinter import *
from tkinter import messagebox
import random

## Password Generator
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate at least 8-10 Letters, 2-4 Symbols & 2-4 Numbers then shuffle it
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    # Insert password into "Password" entry
    password_entry.insert(0, password)


## Save Password
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Show error if there's no entry under "Website", "Email/Username" or "Password" else continue
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure none of the fields are empty.")
    else:
        # For user to double check the details & save data to file if user is ok
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nWebsite: {website} \nEmail: {email} \nPassword: {password} \n\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# Window Setup
window = Tk()
window.title("Password Generator & Manager")
window.config(padx=50, pady=50)

# Canvas Setup
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Placement of "Website", "Email/Username" & "Password" Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Placement of "Website", "Email/Username" & "Password" Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

# Placement of "Generate Password" & "Add" Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")



window.mainloop()