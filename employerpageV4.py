from tkinter import*
root = Tk()
root.geometry("500x500") #Sets the size of the page
scrollbar = Scrollbar(root) #Creates a scrollbar around the page of root
scrollbar.pack(side = RIGHT, fill = Y ) #Location of the scrollbar is put on the right side
mylist = Listbox(root, width = 500, yscrollcommand = scrollbar.set ) #Creates a textbox in the page that is a list
try:
    open('Logged.txt', 'x')
except FileExistsError: #This section just checks if the specific file exists
    pass
with open("Logged.txt") as h:
    lines = h.read()
    username = lines.split('\n', 0)[0].strip()
    username = username[:-1] #Gets the first line of the file and removes the last letter
    try:
        open(username+".txt", "x")
    except FileExistsError:
        pass
    file = open(username+ ".txt", "r")
    x = file.readlines() #Reads every line in the text file and sets them as a list 
for i in range(len(x)): #Does this loop for the amount of items that are in the file
    if i == 0:
        mylist.insert(END, "APPLICANTS")
        mylist.insert(END, "     ")
    else:
        pass
    student_name = x[i][:-1]
    student_name = student_name.strip("1")
    student_page = open(student_name+"S.txt")
    student_info = student_page.readlines()
    mylist.insert(END, student_name) #This section adds the student name and all their information into the scroll section
    for j in range(len(student_info)):
        mylist.insert(END, student_info[j])
    mylist.insert(END, "     ")
mylist.pack(side = LEFT, fill = BOTH ) #Puts the list on the left side and fills up to the width of the screen
scrollbar.config(command = mylist.yview ) #Says that the scrollbar controls the y-axis for the page

root.mainloop()

