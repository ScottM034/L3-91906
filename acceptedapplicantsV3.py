from tkinter import*
root = Tk()
root.geometry("500x500") #Sets the size of the page
scrollbar = Scrollbar(root) #Creates a scrollbar the size of the page
scrollbar.pack(side = RIGHT, fill = Y ) #Puts the scrollbar on the right side of the page
mylist = Listbox(root, width = 500, yscrollcommand = scrollbar.set ) #Creates a list of items with the scrollbar controlling it
try: 
    open('Logged.txt', 'x') #This section just checks if this external file exists
except FileExistsError:
    pass
with open("Logged.txt") as h:
    lines = h.read()
    username = lines.split('\n', 0)[0].strip()
    username = username[:-1] #This gets the first line of the file and removes the last letter
    try:
        open(username+"Accepted.txt", "x")
    except FileExistsError:
        pass
    file = open(username+ "Accepted.txt", "r")
    x = file.readlines() #Reads the file and sets each line as a list
mylist.insert(END, "YOUR ACCEPTED APPLICANTS")
mylist.insert(END, "     ")
for i in range(len(x)): #Repeats this loop for the length of the file
    if "\n" in x[i]: #Only does the loop if the line goes onto a new line to make sure empty lines are not read
        student_page = open(x[i][:-1]+"S.txt")
        student_info = student_page.readlines()
        mylist.insert(END, x[i][:-1]) #This adds the student name at the end of this scrolling list
        for j in range(len(student_info)):
            mylist.insert(END, student_info[j]) #Adds that student's information to the end of that list
        mylist.insert(END, "     ") #Just adds an extra line for space
    else:
        pass
mylist.pack(side = LEFT, fill = BOTH ) #Moves the list to stay on the left and fill the page if required
scrollbar.config( command = mylist.yview )#Tells the scrollbar to make it scroll vertically

root.mainloop()

