from tkinter import*
import tkinter.font as font
from random import*
import time

root = Tk()
root.geometry("600x600")

def student_page():
    root.destroy()
    import studentpage
def reference_page():
    root.destroy()
    import referencepage
def employer_page():
    root.destroy()
    import employerpage

def login():
    username = e1.get()
    password = e2.get()
    act_type = con.get()
    u_p = username+password+str(act_type) 
    print(u_p)
    try:
        f = open("Usernames.txt", "x")
        g = open("Passwords.txt", "x")
        f.close()
        g.close()
    except FileExistsError:
        pass
    with open("Usernames.txt") as file:
        contents = file.read()
        if u_p in contents:
            try:
                f = open("Logged.txt", "x")
            except FileExistsError:
                pass
            write_logs = open("Logged.txt", "w")
            write_logs.write(username+str(var.get())+"\n")
            write_logs.close()
            try:
                f = open("CurrentLogged.txt", "x")
            except FileExistsError:
                pass
            write_clogs = open("CurrentLogged.txt", "w")
            write_clogs.write(username+str(var.get())+"\n")
            write_clogs.close()
            if act_type == 1:
                student_page()
            elif act_type == 2:
                reference_page()
            elif act_type == 3:
                employer_page()
        else:
            lbl25 = Label(root, text="That account doesn't exist")
            lbl25.grid(row = 13, column = 3, columnspan=6)
    
        
def signup():
    username = e3.get()
    password = e4.get()
    if len(password) < 8:
        lbl10 = Label(root, text="Password should be 8 characters or more", width = 42, fg='#FF0000')
        lbl10.grid(row = 24, column = 3, columnspan=6, sticky='W')
    else:
        try:
            f = open("Usernames.txt", "x")
            g = open("Passwords.txt", "x")
            h = open("AccountTypes.txt", "x")
        except FileExistsError:
            pass
        username_check = open("AccountTypes.txt")
        if username+str(var.get()) in username_check.read():
            lbl10 = Label(root, text="Username already exists, please try again", width = 30,fg='#FF0000')
            lbl10.grid(row = 26, column = 3, columnspan=3)
            pass    
        else:
            write_account = open("AccountTypes.txt", "a")
            write_account.write(username+(str(var.get()))+"\n")
            write_account.close()
            print("HEllo"+username+password+(str(var.get()))+"\n")
            write_users = open("Usernames.txt", "a")
            write_users.write(username+password+(str(var.get()))+"\n")
            write_users.close()
            write_users = open("Usernames.txt", "r")
            try:
                h = open("Logged.txt", "x")
                h.close()
            except FileExistsError:
                pass
            write_logs = open("Logged.txt", "w")
            write_logs.write(username+str(var.get())+"\n")
            write_logs.close()
            try:
                h = open(username+".txt", "x")
                h.close()
            except FileExistsError:
                pass
            try:
                f = open("CurrentLogged.txt", "x")
                f.close()
            except FileExistsError:
                pass
            write_clogs = open("CurrentLogged.txt", "w")
            write_clogs.write(username+str(var.get())+"\n")
            write_clogs.close()
            if var.get() == 1:
                try:
                    f = open("Students.txt", "x")
                except FileExistsError:
                    pass
                write_r = open("Students.txt", "a")
                write_r.write(username+"\n")
                write_r.close()
                student_page()
            elif var.get() == 2:
                reference_no = str(randint(1,1000000))
                try:
                    open(username+str(var.get())+".txt", "x")
                except FileExistsError:
                    pass
                reference_write = open(username+str(var.get())+".txt", "a")
                reference_write.write(reference_no + "\n")
                reference_write.close()
                try:
                    f = open("References.txt", "x")
                except FileExistsError:
                    pass
                write_r = open("References.txt", "a")
                write_r.write(username+"\n")
                write_r.close()
                reference_page()
            elif var.get() == 3:
                try:
                    f = open("Employers.txt", "x")
                except FileExistsError:
                    pass
                write_r = open("Employers.txt", "a")
                write_r.write(username+"\n")
                write_r.close()
                employer_page()
            else:
                print("Something went wrong")

  
f1 = font.Font(family='Times New Roman')
f2 = font.Font(family='Times New Roman', size = 12)
var = IntVar()
con = IntVar()

lbl1 = Label(root, text="Login", width = 15, font = f1)
lbl1.grid(row = 3, column = 4)
lbl2 = Label(root, text="Name :", width = 15, font = f1)
lbl2.grid(row = 8, column = 2)
e1 = Entry(root, font =('Arial', 12), width = 30)
e1.grid(row = 8, column = 3, columnspan=6)
lbl21 = Label(root, text="", width=1)
lbl21.grid(row = 9, column = 1)
lbl3 = Label(root, text="Password :", width = 15, font = f1)
lbl3.grid(row = 10, column = 2)
e2 = Entry(root, font =('Arial', 12), width = 30)
e2.grid(row = 10, column = 3, columnspan=6)
lbl24 = Label(root, text=" ", width=1)
lbl24.grid(row = 11, column = 1)
lbl6 = Label(root, text = "Account Type :", font = f1)
lbl6.grid(row=12, column = 2)
r4 = Radiobutton(root, text = "Student", variable=con, value = 1)
r4.grid(row = 12, column = 3)
r5 = Radiobutton(root, text = "Reference", variable=con, value = 2)
r5.grid(row = 12, column = 4)
r6 = Radiobutton(root, text = "Teacher", variable=con, value = 3)
r6.grid(row = 12, column = 5)
btn1 = Button(root, text="Login", font = f1, command=login)
btn1.grid(row = 14, column = 4)
lbl23 = Label(root, text="", width=1)
lbl23.grid(row = 15, column = 1)
lbl4 = Label(root, text="Sign-Up", width = 15, font = f1)
lbl4.grid(row = 18, column = 4)
lbl5 = Label(root, text="Name :", width = 15,font = f1)
lbl5.grid(row = 23, column = 2)
e3 = Entry(root, font =('Arial', 12), width = 30)
e3.grid(row = 23, column = 3, columnspan=6)
lbl22 = Label(root, text=" ", width=1)
lbl22.grid(row = 24, column = 1)
lbl6 = Label(root, text="Password :", width = 15, font = f1)
lbl6.grid(row = 25, column = 2)
e4 = Entry(root, font =('Arial', 12), width = 30)
e4.grid(row = 25, column = 3, columnspan=6)
btn2 = Button(root, text="Sign-Up", font = f1, command=signup)
btn2.grid(row = 28, column = 4)
lbl24 = Label(root, text=" ", width=1)
lbl24.grid(row = 26, column = 1)
lbl6 = Label(root, text = "Account Type :", font = f1)
lbl6.grid(row = 27, column = 2)
r1 = Radiobutton(root, text = "Student", variable=var, value = 1)
r1.grid(row = 27, column = 3)
r2 = Radiobutton(root, text = "Reference", variable=var, value = 2)
r2.grid(row = 27, column = 4)
r3 = Radiobutton(root, text = "Employer", variable=var, value = 3)
r3.grid(row = 27, column = 5)

root.mainloop()
