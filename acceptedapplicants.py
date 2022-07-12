from importlib import reload
from tkinter import*
root = Tk()
root.geometry("500x500")
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y )
mylist = Listbox(root, width = 500, yscrollcommand = scrollbar.set )
try:
    open('Logged.txt', 'x')
except FileExistsError:
    pass
with open("Logged.txt") as h:
    lines = h.read()
    username = lines.split('\n', 0)[0].strip()
    username = username[:-1]
    try:
        open(username+"Accepted.txt", "x")
    except FileExistsError:
        pass
    file = open(username+ "Accepted.txt", "r")
    x = file.readlines()
    print(len(x))
for i in range(len(x)):
    if "\n" in x[i]:
        student_page = open(x[i][:-1]+"S.txt")
        student_info = student_page.readlines()
        mylist.insert(END, x[i][:-1])
        for j in range(len(student_info)):
            mylist.insert(END, student_info[j])
        mylist.insert(END, "     ")
    else:
        pass
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

root.mainloop()

