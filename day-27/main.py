import tkinter

def km_to_miles():
    km = float(km_input.get())
    miles = round(km / 1.609)
    miles_result_label.config(text=f"{miles}")

if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("Km to Mile converter")
    window.config(padx=20, pady=20)

    km_input = tkinter.Entry(width=7)
    km_input.grid(column=1, row=0)

    km_label = tkinter.Label(text="Km")
    km_label.grid(column=2, row=0)

    is_equal_label = tkinter.Label(text="is equal to")
    is_equal_label.grid(column=0, row=1)

    miles_result_label = tkinter.Label(text="0")
    miles_result_label.grid(column=1, row=1)

    miles_label = tkinter.Label(text="Miles")
    miles_label.grid(column=2, row=1)

    button = tkinter.Button(text="Calculate", command=km_to_miles)
    button.grid(column=1, row=2)

    window.mainloop()
