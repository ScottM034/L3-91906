from importlib import reload
from tkinter import*
root = Tk()
root.geometry("500x500") #Sets the size of the window 
scrollbar = Scrollbar(root) #Creates a scrollbar around the window
scrollbar.pack(side = RIGHT, fill = Y ) #Puts the scrollbar on the right side of the window
mylist = Listbox(root, width = 500, yscrollcommand = scrollbar.set ) #Makes the window a list of text
try:
    open("Employers.txt", "x") #Checks if this file exists
except FileExistsError:
    pass
file = open("Employers.txt", "r")
x = file.readlines() #Creates a python list from everything in the external file
mylist.insert(END, "COMPANY POSTINGS")
mylist.insert(END, "     ")
for i in range(len(x)):
    existing_check = 0
    employer_name = x[i][:-1]
    try:
        open(employer_name+"3.txt")
    except FileNotFoundError:
        existing_check = 1 #This checks if the company is complete and is ready to be applied for
    if existing_check == 0:       
        with open(employer_name+"3.txt") as j:
            top = j.read()
            topline = top.split('\n', 0)[0] #Gets the first line in that file which is the reference number
        employer_name = employer_name.strip("1") #Gets the employer name without the type 
        employer_page = open(employer_name+"E.txt")
        employer_info = employer_page.readlines() #Gets the list of the company's information
        mylist.insert(END, employer_name) 
        mylist.insert(END, "Reference Number: " + topline.strip("RefNo")) #Adds the company's name and refernce number to this scrolling list
        for j in range(len(employer_info)):
            mylist.insert(END, employer_info[j]) #Adds the company's info to the list
        mylist.insert(END, "     ")
    else:
        pass
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview ) #Tells the scrollbar that when scrolled it goes vertically

root.mainloop()