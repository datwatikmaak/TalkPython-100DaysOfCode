import tkinter as tk

window = tk.Tk()

greeting = tk.Label(
    text="Hello Tkinter",
    fg="#34A2FE",     # set the text color to light blue
    bg="black",      # set the background color to black
    width=10,
    height=5        # tkinter uses the 0 to set the hight and width instead of pixels
)

greeting.pack()

window.mainloop()
