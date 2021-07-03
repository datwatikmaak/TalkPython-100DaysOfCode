import tkinter as tk

window = tk.Tk()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    fg="yellow",
    bg="blue"
)

button.pack()

window.mainloop()
