from importlib import reload
from tkinter import*
root = Tk()
root.geometry("500x500")
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y )
mylist = Listbox(root, width = 500, yscrollcommand = scrollbar.set )
try:
    open("Employers.txt", "x")
except FileExistsError:
    pass
file = open("Employers.txt", "r")
x = file.readlines()
for i in range(len(x)):
    existing_check = 0
    employer_name = x[i][:-1]
    try:
        open(employer_name+"3.txt")
    except FileNotFoundError:
        existing_check = 1
    if existing_check == 0:       
        with open(employer_name+"3.txt") as j:
            top = j.read()
            topline = top.split('\n', 0)[0]
        employer_name = employer_name.strip("1")
        employer_page = open(employer_name+"E.txt")
        employer_info = employer_page.readlines()
        mylist.insert(END, employer_name)
        mylist.insert(END, "Reference Number: " + topline.strip("RefNo"))
        for j in range(len(employer_info)):
            mylist.insert(END, employer_info[j])
        mylist.insert(END, "     ")
    else:
        pass
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

root.mainloop()