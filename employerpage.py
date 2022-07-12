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
        open(username+".txt", "x")
    except FileExistsError:
        pass
    file = open(username+ ".txt", "r")
    x = file.readlines()
    print(len(x))
for i in range(len(x)):
    student_name = x[i][:-1]
    student_name = student_name.strip("1")
    student_page = open(student_name+"S.txt")
    student_info = student_page.readlines()
    mylist.insert(END, student_name)
    for j in range(len(student_info)):
        mylist.insert(END, student_info[j])
    mylist.insert(END, "     ")
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

root.mainloop()

