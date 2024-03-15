from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    char_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = char_list + symbols_list + numbers_list


    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_username_entry.get()
    passwrd = password_entry.get()

    if website == "" or passwrd == "":
        messagebox.showerror(title="Ooops", message="Don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\n"
                                                              f"Password: {passwrd}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"\n{website} | {email} | {passwrd}")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="ew")
website_entry.focus()

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
email_username_entry.insert(0, "joe_shmoe@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew")

generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="ew")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")


window.mainloop()
