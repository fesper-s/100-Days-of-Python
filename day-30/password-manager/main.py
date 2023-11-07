import tkinter as tk
from tkinter import messagebox
from random import randint, shuffle, choice
import json

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)


def save():
    website = website_entry.get()
    login = login_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "login": login,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as fd:
                data = json.load(fd)
        except FileNotFoundError:
            with open("data.json", "w") as fd:
                json.dump(new_data, fd, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as fd:
                json.dump(data, fd, indent=4)
        finally:
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as fd:
            data = json.load(fd)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            login = data[website]["login"]
            password = data[website]["password"]
            messagebox.showinfo(tittle=website, message=f"Login: {login}\nPassword: {password}")
        else:
            messagebox.showinfo(tittle="Error", message=f"No details for {website} exists.")

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    canvas = tk.Canvas(height=200, width=200)
    logo_img = tk.PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(column=1, row=0)

    website_label = tk.Label(text="Website:")
    website_label.grid(column=0, row=1)
    website_entry = tk.Entry(width=21)
    website_entry.grid(column=1, row=1)
    website_entry.focus()
    search_button = tk.Button(text="Search", width=13, command=find_password)
    search_button.grid(column=2, row=1)

    login_label = tk.Label(text="Email/Username:")
    login_label.grid(column=0, row=2)
    login_entry = tk.Entry(width=35)
    login_entry.grid(column=1, row=2, columnspan=2)
    login_entry.insert(0, "fabricio_esper@outlook.com")

    password_label = tk.Label(text="Password:")
    password_label.grid(column=0, row=3)
    password_entry = tk.Entry(width=21)
    password_entry.grid(column=1, row=3)
    password_button = tk.Button(text="Generate Password", command=generate_password)
    password_button.grid(column=2, row=3)

    add_button = tk.Button(width=36, text="Add", command=save)
    add_button.grid(column=1, row=4, columnspan=2)

    window.mainloop()
