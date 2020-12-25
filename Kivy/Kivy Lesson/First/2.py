import tkinter as tk
import random

def omikuji():
	kuji = ["大吉","中吉","小吉","吉","凶"]
	label.configure(text = random.choice(kuji))

root = tk.Tk()
root.geometry("200x100")

label = tk.Label(text="LABEL")
button = tk.Button(text="PUSH",command = omikuji)

label.pack()
button.pack()
tk.mainloop()
