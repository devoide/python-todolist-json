from todolist import *
import tkinter as tk

def begin():
    for index, i in enumerate(load(), start=0):
        itemCon = tk.Frame(listCon, bg=color2)
        listtext = tk.Label(itemCon, bg=color2, fg=color3, text=i["content"])
        var = tk.IntVar()
        var.set(0)
        checkbox = tk.Checkbutton(itemCon, bg=color2, variable=var)
        delbutton = tk.Button(itemCon, bg=color2, fg=color3, text='delete', command=lambda id=i["id"]: guidelete(id))
        itemCon.pack()
        checkbox.grid(row=0, column=0)
        listtext.grid(row=0, column=1)
        delbutton.grid(row=0, column=2)


def clearlist():
    for i in listCon.winfo_children():
        i.destroy()


def guiadd():
    task = inputEntry.get()
    inputEntry.delete(0, 'end')
    if task != ' ' * len(task):
        clearlist()
        tasks = load()
        item = {"id": str(time.time()), "content": str(task), "completed": False}
        tasks.append(item)
        write(tasks)
        begin()


def guidelete(id):
    print(id)
    tasks = load()
    tasks = [x for x in tasks if x["id"] != id]
    write(tasks)
    clearlist()
    begin()


def change(id):
    print("hello")
    tasks = load()
    for x in tasks:
        if x["id"] == id:
            x["completed"] = not x["completed"]
    print(tasks)
    write(tasks)
    clearlist()
    begin()



color1 = '#363062'
color2 = '#435585'
color3 = '#F5E8C7'

#root configuration
root = tk.Tk()
root.title("todolist")
root.geometry("600x400")
root.configure(bg=color1)
root.maxsize(1024, 768)
root.minsize(400, 300)

#frame configuration
mainCon = tk.Frame(root)
mainCon.pack(fill='both', expand=True)
mainCon.grid_rowconfigure(1, weight=1)
mainCon.grid_columnconfigure(0, weight=1)

titleCon = tk.Frame(mainCon, bg=color1)
titleCon.grid(row=0, column=0, sticky='ew')

listCon = tk.Frame(mainCon, bg=color2)
listCon.grid(row=1, column=0, sticky='nsew')

#label
title = tk.Label(titleCon, bg=color2, fg=color3, text="Add Item")
title.pack(pady=10, padx=20)

#button
button = tk.Button(titleCon, text="add", bg=color2, fg=color3, command=guiadd)
button.pack(pady=10, padx=20)

#input
inputEntry = tk.Entry(titleCon)
inputEntry.pack(pady=10, padx=20)


if __name__ == '__main__':
    begin()
    root.mainloop()