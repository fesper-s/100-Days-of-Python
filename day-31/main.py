import pandas, tkinter, random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict_data)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    dict_data.remove(current_card)
    data = pandas.DataFrame(dict_data)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

if __name__ == "__main__":
    try:
        data = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        data = pandas.read_csv("data/french_words.csv")
    finally:
        dict_data = data.to_dict(orient="records")

    window = tkinter.Tk()
    window.title("Flashy")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    flip_timer = window.after(3000, func=flip_card)

    canvas = tkinter.Canvas(width=800, height=526)
    card_back_img = tkinter.PhotoImage(file="images/card_back.png")
    card_front_img = tkinter.PhotoImage(file="images/card_front.png")
    card_background = canvas.create_image(400, 263, image=card_front_img)
    card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
    card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.grid(row=0, column=0, columnspan=2)

    wrong_img = tkinter.PhotoImage(file="images/wrong.png")
    wrong_button = tkinter.Button(image=wrong_img, highlightthickness=0, command=next_card)
    wrong_button.grid(row=1, column=0)

    right_img = tkinter.PhotoImage(file="images/right.png")
    right_button = tkinter.Button(image=right_img, highlightthickness=0, command=is_known)
    right_button.grid(row=1, column=1)

    next_card()

    window.mainloop()
