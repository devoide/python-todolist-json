from todolist import *
import tkinter as tk

color1 = '#363062'
color2 = '#435585'
color3 = '#F5E8C7'

#root configuration
root = tk.Tk()
root.title("todolist")
root.geometry("600x400")
root.configure(bg=color1)
root.maxsize(1024, 768)
root.minsize(300, 200)

#frame configuration
titleCon = tk.Frame(root, width=200, height=100, bg=color2)
titleCon.place(relx=0.5, rely=0.2, anchor='center')

#label
title = tk.Label(titleCon, bg=color2, fg=color3, text="Add Item")
title.pack(pady=10, padx=20)

#input
inputEntry = tk.Entry(titleCon)
inputEntry.pack(pady=10, padx=20)

root.mainloop()
