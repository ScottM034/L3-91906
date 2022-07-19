from os import close
import tkinter as tk
from tkinter import RIGHT, VERTICAL, Y, Button, Frame, Label, Toplevel, ttk
from random import randint
import webbrowser
import time



class jobapp(tk.Tk): #This class holds all the code and allows the code to be split into parts
    def __init__(self, *arg, **kwarg):
        tk.Tk.__init__(self, *arg, **kwarg)
        self.geometry("500x500") #Defines the window shape for all parts of the code
        self.title("JoBDSC")

        self.login = ttk.Frame() #Here I set the groups for each part of the code that can be called at any time
        self.student = ttk.Frame(self)
        self.student2 = ttk.Frame(self)
        self.reference = ttk.Frame(self)
        self.employer = ttk.Frame(self)
        self.link_ref = ttk.Frame(self)
        self.ref_comment = ttk.Frame(self)
        self.employer_setup = ttk.Frame(self)
        self.student_setup = ttk.Frame(self)
        self.reference_setup = ttk.Frame(self)

        self.login.pack() #Showing the initial window on start up

        #Login Page Code
        #These long sections of Label, Button, .grid etc. sets the GUI for each given page
        var = tk.IntVar() #Set the type of variable gained by the RadioButton
        con = tk.IntVar()
        lbl1 = ttk.Label(self.login, text="Login", font = ("Arial")) #Adding a bit of text in a specific page
        lbl1.grid(row = 3, column = 4) #.grid sets the placement in the window with an imaginary grid
        lbl2 = ttk.Label(self.login, text="Name :", width = 15, font = ("Arial"))
        lbl2.grid(row = 8, column = 2)
        login_username = ttk.Entry(self.login, font =('Arial', 12), width = 30) #Creates a text box for the User to enter in
        login_username.grid(row = 8, column = 3, columnspan=6)
        lbl21 = ttk.Label(self.login, text="", width=1)
        lbl21.grid(row = 9, column = 1)
        lbl3 = ttk.Label(self.login, text="Password :", width = 15, font = ("Arial"))
        lbl3.grid(row = 10, column = 2)
        login_password = ttk.Entry(self.login, font =('Arial', 12), width = 30)
        login_password.grid(row = 10, column = 3, columnspan=6)
        lbl24 = ttk.Label(self.login, text=" ", width=1)
        lbl24.grid(row = 11, column = 1)
        lbl6 = ttk.Label(self.login, text = "Account Type :", font = ("Arial"), width= 15)
        lbl6.grid(row=12, column = 2)
        r4 = ttk.Radiobutton(self.login, text = "Student", variable=con, value = 1) #Creates a button that can be selected as one of 3
        #to figure out the user's account type
        r4.grid(row = 12, column = 3)
        r5 = ttk.Radiobutton(self.login, text = "Reference", variable=con, value = 2)
        r5.grid(row = 12, column = 4)
        r6 = ttk.Radiobutton(self.login, text = "Employer", variable=con, value = 3)
        r6.grid(row = 12, column = 5)
        btn1 = ttk.Button(self.login, text="Login", command=lambda : self.user_check(login_username.get(), login_password.get(), con.get()))
        btn1.grid(row = 14, column = 4) #This button checks if the user's login is correct and tells them if something is wrong by use of a function
        lbl23 = ttk.Label(self.login, text="", width=1)
        lbl23.grid(row = 15, column = 1)
        lbl4 = ttk.Label(self.login, text="Sign-Up", font = ("Arial"))
        lbl4.grid(row = 18, column = 4)
        lbl5 = ttk.Label(self.login, text="Name :", width = 15, font = ("Arial"))
        lbl5.grid(row = 23, column = 2)
        signup_username = ttk.Entry(self.login, font =('Arial', 12), width = 30)
        signup_username.grid(row = 23, column = 3, columnspan=6)
        lbl22 = ttk.Label(self.login, text=" ", width=1)
        lbl22.grid(row = 24, column = 1)
        lbl6 = ttk.Label(self.login, text="Password :", width = 15, font = ("Arial"))
        lbl6.grid(row = 25, column = 2)
        signup_password = ttk.Entry(self.login, font =('Arial', 12), width = 30)
        signup_password.grid(row = 25, column = 3, columnspan=6)
        btn2 = ttk.Button(self.login, text="Sign-Up", command=lambda : self.user_check_s(signup_username.get(), signup_password.get(), var.get()))
        btn2.grid(row = 28, column = 4) #This function tells the code that it is a new user and thus should be given the other type of login paeg
        lbl24 = ttk.Label(self.login, text=" ", width=1)
        lbl24.grid(row = 26, column = 1)
        lbl6 = ttk.Label(self.login, text = "Account Type :", font = ("Arial"), width = 15)
        lbl6.grid(row = 27, column = 2)
        r1 = ttk.Radiobutton(self.login, text = "Student", variable=var, value = 1)
        r1.grid(row = 27, column = 3)
        r2 = ttk.Radiobutton(self.login, text = "Reference", variable=var, value = 2)
        r2.grid(row = 27, column = 4)
        r3 = ttk.Radiobutton(self.login, text = "Employer", variable=var, value = 3)
        r3.grid(row = 27, column = 5)

        #Reference Page Code
        placeholder = ttk.Label(self.reference, text= ' ')
        placeholder.grid(row = 0, column= 0)
        btn2 = ttk.Button(self.reference, text="Logout", command = lambda : self.next_page(self.reference, self.login), width=14)
        btn2.grid(row = 1, column = 1)
        students_label = ttk.Label(self.reference, text = "Your Students", font = ("Helvetica 14 underline"))
        students_label.grid(row = 2, column = 3, columnspan= 2)

        #ReferenceCommenting Page
        lbl21 = ttk.Label(self.ref_comment, text = " ")
        lbl21.grid(row = 1, column = 1)
        comment_title = ttk.Label(self.ref_comment, text = "Comment as a Reference: ", width = 30)
        comment_title.grid(row = 7, column = 2, columnspan= 2)
        lbl21 = ttk.Label(self.ref_comment, text = " ")
        lbl21.grid(row = 8, column = 1)
        commenting = ttk.Entry(self.ref_comment, width = 30)
        commenting.grid(row = 7, column = 6, columnspan = 2)
        btn1 = ttk.Button(self.ref_comment, text = "Comment", command=lambda : self.comment(str(commenting.get())))
        btn1.grid(row = 9, column = 7)
        btn2 = ttk.Button(self.ref_comment, text = "Cancel", command=lambda : self.next_page(self.ref_comment, self.reference))
        btn2.grid(row = 9, column = 6)

        #Linking a Reference Page
        lbl1 = ttk.Label(self.link_ref, text="Link a Reference", width = 20)
        lbl1.grid(row = 3, column = 3, columnspan=2)
        lbl2 = ttk.Label(self.link_ref, text="Name :", width = 15)
        lbl2.grid(row = 8, column = 2)
        linked_reference = ttk.Entry(self.link_ref, width = 30)
        linked_reference.grid(row = 8, column = 3, columnspan=6)
        lbl21 = ttk.Label(self.link_ref, text="", width=1)
        lbl21.grid(row = 9, column = 1)
        lbl3 = ttk.Label(self.link_ref, text="Reference Number :", width = 15)
        lbl3.grid(row = 10, column = 2)
        refno = ttk.Entry(self.link_ref, width = 30)
        refno.grid(row = 10, column = 3, columnspan=6)
        lbl24 = ttk.Label(self.link_ref, text=" ", width=1)
        lbl24.grid(row = 11, column = 1)
        btn1 = ttk.Button(self.link_ref, text = "Link", width = 20, command = lambda : self.link(linked_reference.get(), refno.get()))
        btn1.grid(row = 12, column = 3)
        btn2= ttk.Button(self.link_ref, text = "Cancel", width = 20, command = lambda : self.next_page(self.link_ref, self.student))
        btn2.grid(row = 12, column = 4)
        lbl24 = ttk.Label(self.link_ref, text="   ", width=1)
        lbl24.grid(row = 13, column = 1)

        #Student Page 1
        link1 = ttk.Button(self.student, text="Company List", command = lambda : self.employer_list(), width = 20)
        link1.grid(row = 0, column = 2, columnspan= 3)
        btn1 = ttk.Button(self.student, text="Link a Reference", command = lambda : self.next_page(self.student, self.link_ref), width=15)
        btn1.grid(row = 0, column = 1)
        btn2 = ttk.Button(self.student, text="Logout", command = lambda : self.next_page(self.student, self.login), width=14)
        btn2.grid(row = 0, column = 5, columnspan= 2)
        lbl21 = ttk.Label(self.student, text ="  ", width = 1)
        lbl21.grid(row=1, column = 1)
        lbl22 = ttk.Label(self.student, text ="  ", width = 8)
        lbl22.grid(row=1, column = 6)
        lbl22 = ttk.Label(self.student, text ="  ", width = 10)
        lbl22.grid(row=1, column = 4)
        try: #This section just creates a file if it is not already created so that the code can check what is in the file later
            open("Employers.txt", "x")
        except FileExistsError:
            pass
        try:
            g = open("Counter.txt", 'x')
        except FileExistsError:
            pass
        placeholder = ttk.Label(self.student, text = '   ')
        placeholder.grid(row = 2, column = 0)
        search_label = ttk.Label(self.student, text = "Company Name:", width = 20)
        search_label.grid(row = 3, column = 2, columnspan= 2)
        search_bar = ttk.Entry(self.student, font =('Arial', 12), width = 20)
        search_bar.grid(row = 3, column = 4, columnspan= 2)
        company_number = ttk.Entry(self.student, font = ('Arial', 12), width = 20)
        company_number.grid(row = 5, column = 4, columnspan=2)
        company_number_label = ttk.Label(self.student, text = "Company Number:", width = 20)
        company_number_label.grid(row = 5, column = 2, columnspan= 2)
        placeholder = ttk.Label(self.student, text = " ", width = 3)
        placeholder.grid(row = 4, column = 4)
        placeholder = ttk.Label(self.student, text = " ", width = 3)
        placeholder.grid(row = 6, column = 4)
        search_button = ttk.Button(self.student, text = "Apply", width = 20, command = lambda : self.search_application(search_bar.get(), company_number.get(), ))
        search_button.grid(row = 7, column = 4, columnspan= 2)


        #Employer Information Page
        lbl0 = ttk.Label(self.employer_setup, text="Set-Up", width=15)
        lbl0.grid(row = 3, column = 4)
        lbl2 = ttk.Label(self.employer_setup, text="Job Title:", width = 15)
        lbl2.grid(row = 8, column = 2)
        e_job_title = ttk.Entry(self.employer_setup, font =('Arial', 12), width = 30)
        e_job_title.grid(row = 8, column = 3, columnspan=6)
        lbl21 = ttk.Label(self.employer_setup, text="", width=1)
        lbl21.grid(row = 9, column = 1)
        lbl3 = ttk.Label(self.employer_setup, text="Location:", width = 15)
        lbl3.grid(row = 10, column = 2)
        e_location = ttk.Entry(self.employer_setup, font =('Arial', 12), width = 30)
        e_location.grid(row = 10, column = 3, columnspan=6)
        lbl21 = ttk.Label(self.employer_setup, text="", width=1)
        lbl21.grid(row = 12, column = 1)
        lbl5 = ttk.Label(self.employer_setup, text="Email:", width = 15)
        lbl5.grid(row = 23, column = 2)
        e_email = ttk.Entry(self.employer_setup, font =('Arial', 12), width = 30)
        e_email.grid(row = 23, column = 3, columnspan=6)
        lbl22 = ttk.Label(self.employer_setup, text=" ", width=1)
        lbl22.grid(row = 25, column = 1)
        lbl6 = ttk.Label(self.employer_setup, text="Mobile Number:", width = 15)
        lbl6.grid(row = 27, column = 2)
        e_phone = ttk.Entry(self.employer_setup, font =('Arial', 12), width = 30)
        e_phone.grid(row = 27, column = 3, columnspan=6)
        lbl24 = ttk.Label(self.employer_setup, text=" ", width=1)
        lbl24.grid(row = 29, column = 1)
        btn1 = ttk.Button(self.employer_setup, text="Finish", command=lambda : self.finish(e_job_title.get(), e_location.get(), e_email.get(), e_phone.get()))
        btn1.grid(row = 30, column = 3)

        #Employer Page
        logout = ttk.Button(self.employer, text="Logout", command = lambda : self.next_page(self.employer, self.login), width=14)
        logout.grid(row = 0, column = 3)
        try:
            open("CurrentLogged.txt", 'x')
        except FileExistsError:
            pass
        with open("CurrentLogged.txt") as h: #This section of code gets the first line of the desired external file
                    lines = h.read()
                    employer = lines.split('\n', 0)[0].strip()
        placeholder = ttk.Label(self.employer, text = ' ')
        placeholder.grid(row = 0 ,column=0)
        delete_account = ttk.Button(self.employer, text="Delete Account", command = lambda : self.delete(employer), width=14)
        delete_account.grid(row = 0, column = 1, columnspan=1)
        view_list = ttk.Button(self.employer, text = "View Applicants", command = lambda : self.view_applicants(), width = 40)
        view_list.grid(row = 3, column = 2)
        placeholder = ttk.Label(self.employer, text = ' ')
        placeholder.grid(row = 4 ,column=0)
        applicant_name = ttk.Label(self.employer, text = "Applicant Name: ")
        applicant_name.grid(row = 5, column = 1)
        applicant_name_entry = ttk.Entry(self.employer, width = 40)
        applicant_name_entry.grid(row = 5, column = 2)
        placeholder = ttk.Label(self.employer, text = ' ')
        placeholder.grid(row = 6,column=0)
        accept_applicant = ttk.Button(self.employer, text = "Accept", width = 40, command = lambda : self.accept(applicant_name_entry.get()))
        accept_applicant.grid (row = 8, column = 2)
        placeholder = ttk.Label(self.employer, text = ' ')
        placeholder.grid(row = 9 ,column=0)
        accepted_button = ttk.Button(self.employer, text = "Accepted Applicants", width = 40, command = lambda : self.accepted_list())
        accepted_button.grid(row = 13, column = 2)



        #Student Information Page
        lbl1 = ttk.Label(self.student_setup, text = "Student Information", width = 30)
        lbl1.grid(row = 1, column = 4)
        lbl2 = ttk.Label(self.student_setup, text="Achievements:", width = 15)
        lbl2.grid(row = 8, column = 2)
        s_achievements = ttk.Entry(self.student_setup, font =('Arial', 12), width = 30)
        s_achievements.grid(row = 8, column = 3, columnspan=6)
        lbl21 = ttk.Label(self.student_setup, text="", width=1)
        lbl21.grid(row = 9, column = 1)
        lbl3 = ttk.Label(self.student_setup, text="Location:", width = 15)
        lbl3.grid(row = 10, column = 2)
        s_location = ttk.Entry(self.student_setup, font =('Arial', 12), width = 30)
        s_location.grid(row = 10, column = 3, columnspan=6)
        lbl21 = ttk.Label(self.student_setup, text="", width=1)
        lbl21.grid(row = 12, column = 1)
        lbl5 = ttk.Label(self.student_setup, text="Email:", width = 15)
        lbl5.grid(row = 23, column = 2)
        s_email = ttk.Entry(self.student_setup, font =('Arial', 12), width = 30)
        s_email.grid(row = 23, column = 3, columnspan=6)
        lbl22 = ttk.Label(self.student_setup, text=" ", width=1)
        lbl22.grid(row = 25, column = 1)
        lbl6 = ttk.Label(self.student_setup, text="Mobile Number:", width = 15)
        lbl6.grid(row = 27, column = 2)
        s_phone = ttk.Entry(self.student_setup, font =('Arial', 12), width = 30)
        s_phone.grid(row = 27, column = 3, columnspan=6)
        lbl24 = ttk.Label(self.student_setup, text=" ", width=1)
        lbl24.grid(row = 29, column = 1)
        btn1 = ttk.Button(self.student_setup, text="Finish", command=lambda : self.finish_s(s_achievements.get(), s_location.get(), s_email.get(), s_phone.get()))
        btn1.grid(row = 30, column = 3)
        
        #Reference Information Page
        lbl0 = ttk.Label(self.reference_setup, text="Set-Up", width=15)
        lbl0.grid(row = 3, column = 5)
        lbl2 = ttk.Label(self.reference_setup, text="Reference Job:", width = 15)
        lbl2.grid(row = 8, column = 2)
        r_job_title = ttk.Entry(self.reference_setup, font =('Arial', 12), width = 30)
        r_job_title.grid(row = 8, column = 3, columnspan=6)
        lbl21 = ttk.Label(self.reference_setup, text="", width=1)
        lbl21.grid(row = 12, column = 1)
        lbl5 = ttk.Label(self.reference_setup, text="Email:", width = 15)
        lbl5.grid(row = 23, column = 2)
        r_email = ttk.Entry(self.reference_setup, font =('Arial', 12), width = 30)
        r_email.grid(row = 23, column = 3, columnspan=6)
        lbl22 = ttk.Label(self.reference_setup, text=" ", width=1)
        lbl22.grid(row = 25, column = 1)
        lbl6 = ttk.Label(self.reference_setup, text="Mobile Number:", width = 15)
        lbl6.grid(row = 27, column = 2)
        r_phone = ttk.Entry(self.reference_setup, font =('Arial', 12), width = 30)
        r_phone.grid(row = 27, column = 3, columnspan=6)
        lbl24 = ttk.Label(self.reference_setup, text=" ", width=1)
        lbl24.grid(row = 29, column = 1)
        btn1 = ttk.Button(self.reference_setup, text="Finish", command=lambda : self.finish_t(r_job_title.get(), r_email.get(), r_phone.get()))
        btn1.grid(row = 30, column = 3)

    def view_applicants(self): #Function that calls another code to show the applicants for an employer
        import employerpage

    def accepted_list(self): #Function that calls another code to show the employer's accepted applicants
        import acceptedapplicants

    def employer_list(self):
        import studentpage

    def callback(self, url): #Function that opens the URL that I want the program to link to
        webbrowser.open_new(url)
        
    def finish(self, job_t, location, email, phone): #From the user's intital sign-up we create a file that has all his information
        if "@" not in str(email): #Checking if the email the user entered is invalid
            lbl30 = ttk.Label(self.employer_setup, text="Please enter a valid email", width = 30)
            lbl30.grid(row = 24, column = 3, columnspan=2)
        else:
            if len(phone) < 9: #Checking if the mobile number the user entered is invalid
                lbl30 = ttk.Label(self.employer_setup, text="Please enter a valid Mobile Number", width = 35)
                lbl30.grid(row = 28, column = 3, columnspan=2)
            else:
                with open("CurrentLogged.txt") as h:
                    lines = h.read()
                    first = lines.split('\n', 0)[0].strip()
                    try:
                        f = open("Employers.txt", "x")
                    except FileExistsError:
                        pass
                    write_r = open("Employers.txt", "a") #Opens the append version of the text to write to
                    write_r.write(first[:-1]+"\n")#This means the given text will be added to the end of the external file
                    write_r.close()
                    try:
                        g = open(first[:-1]+"E.txt", 'x')
                    except FileExistsError:
                        pass
                    write_i = open(first[:-1]+"E.txt", "a")
                    write_i.write("Job Title: "+ job_t +"\n")
                    write_i.write("Location: "+ location +"\n")
                    write_i.write("Email: "+ email +"\n")
                    write_i.write("Mobile Number: "+ phone +"\n")
                    write_i.close()
                    try:
                        open(first[:-1]+"3.txt", 'x')
                    except FileExistsError:
                            pass
                    with open(first[:-1]+"3.txt") as j:
                        top = j.read()
                        topline = top.split('\n', 0)[0]
                        lbl22 = ttk.Label(self.employer, anchor = "center", text=("Reference Number: "+ topline.strip("RefNo")), font = ("Helvetica 12 underline"))
                        lbl22.grid(row = 1, column = 2)
                        new_space = ttk.Label(self.employer, text = "                  ", width= 8)
                        new_space.grid(row = 2, column = 3, pady = 5)
                    self.next_page(self.employer_setup, self.employer)

    def finish_s(self, job_t, location, email, phone): #Function that adds the information for a new student that signed up
        if "@" not in email:
            lbl30 = ttk.Label(self.student_setup, text="Please enter a valid email", width = 30)
            lbl30.grid(row = 24, column = 3, columnspan=2)
        else:
            if len(phone) < 9:
                lbl30 = ttk.Label(self.student_setup, text="Please enter a valid Mobile Number", width = 35)
                lbl30.grid(row = 28, column = 3, columnspan=2)
            else:
                with open("CurrentLogged.txt") as h:
                    lines = h.read()
                    first = lines.split('\n', 0)[0].strip()
                    try:
                        f = open("Students.txt", "x")
                    except FileExistsError:
                        pass
                    write_r = open("Students.txt", "a")
                    write_r.write(first[:-1]+"\n")
                    write_r.close()
                    g = open(first[:-1]+"S.txt", 'x')
                    write_i = open(first[:-1]+"S.txt", "a")
                    write_i.write("Achievements: "+ job_t +"\n")
                    write_i.write("Location: "+ location +"\n")
                    write_i.write("Email: "+ email +"\n")
                    write_i.write("Mobile Number: "+ phone +"\n")
                    write_i.close()
                    self.next_page(self.student_setup, self.student)

    def delete(self, employer): #Function to delete an employer account when they want so their application
        # does not sit on the app when a job is not available
        employer = employer.strip("3")
        with open('Employers.txt', 'r') as file :
            filedata = file.read()
        filedata = filedata.replace(employer, str(randint(10000, 10000000000)))
        with open('Employers.txt', 'w') as file:
            file.write(filedata)
        with open('Usernames.txt', 'r') as file :
            filedata = file.read()
        filedata = filedata.replace(employer[:-8], str(randint(10000,10000000000)))
        with open('Usernames.txt', 'w') as file:
            file.write(filedata)
        self.next_page(self.employer, self.login)




    def finish_t(self, job_t, email, phone): #Adds information when a new reference is added
        if "@" not in email:
            lbl30 = ttk.Label(self.reference_setup, text="Please enter a valid email", width = 20)
            lbl30.grid(row = 24, column = 3, columnspan=2)
        else:
            if len(phone) < 9:
                lbl30 = ttk.Label(self.reference_setup, text="Please enter a valid Mobile Number", width = 35)
                lbl30.grid(row = 28, column = 3, columnspan=2)
            else:
                with open("CurrentLogged.txt") as h:
                    lines = h.read()
                    first = lines.split('\n', 0)[0].strip()
                    try:
                        f = open("References.txt", "x")
                    except FileExistsError:
                        pass
                    write_r = open("References.txt", "a")
                    write_r.write(first[:-1]+"\n")
                    write_r.close()
                    g = open(first[:-1]+"T.txt", 'x')
                    write_i = open(first[:-1]+"T.txt", "a")
                    write_i.write("Reference Job: "+ job_t +"\n")
                    write_i.write("Email: "+ email +"\n")
                    write_i.write("Mobile Number: "+ phone +"\n")
                    write_i.close()
                    try:
                        open(first[:-1]+"2.txt", 'x')
                    except FileExistsError:
                            pass
                    with open(first[:-1]+"2.txt") as j:
                        top = j.read()
                        topline = top.split('\n', 0)[0]
                        lbl22 = ttk.Label(self.reference, anchor = "center", text=("Reference Number: "+ topline.strip("RefNo")), font = ("Helvetica 10 underline"))
                        lbl22.grid(row = 1, column = 6)
                        new_space = ttk.Label(self.employer, text = "                  ", width= 8)
                        new_space.grid(row = 2, column = 3, pady = 5)
                    self.next_page(self.reference_setup, self.reference)


    def next_page(self, current, next): 
        #This will take the User from their current frame to the next indended frame depending on which button they pressed
        current.pack_forget()
        next.pack()

    def user_check_s(self, user, password, act_type): #This checks a signing up user if they already have an account
        #or if their password does not meet the requirements for security
        if len(password) < 8:
            lbl10 = ttk.Label(self.login, text="Password should be 8 characters or more", width = 42)
            lbl10.grid(row = 24, column = 3, columnspan=6, sticky='W')
        else:
            try:
                f = open("Usernames.txt", "x")
                g = open("Passwords.txt", "x")
                h = open("AccountTypes.txt", "x")
            except FileExistsError:
                pass
            username_check = open("AccountTypes.txt")
            if user+str(act_type) in username_check.read():
                lbl10 = ttk.Label(self.login, text="Username already exists, please try again", width = 40)
                lbl10.grid(row = 26, column = 3, columnspan=3)
                pass    
            else:
                write_account = open("AccountTypes.txt", "a")
                write_account.write(user+(str(act_type))+"\n")
                write_account.close()
                write_users = open("Usernames.txt", "a")
                write_users.write(user+password+(str(act_type))+"\n")
                write_users.close()
                write_users = open("Usernames.txt", "r")
                try:
                    h = open("Logged.txt", "x")
                    h.close()
                except FileExistsError:
                    pass
                write_logs = open("Logged.txt", "w")
                write_logs.write(user+str(act_type)+"\n")
                write_logs.close()
                try:
                    h = open(user+".txt", "x")
                    h.close()
                except FileExistsError:
                    pass
                try:
                    f = open("CurrentLogged.txt", "x")
                    f.close()
                except FileExistsError:
                    pass
                write_clogs = open("CurrentLogged.txt", "w")
                write_clogs.write(user+str(act_type)+"\n")
                write_clogs.close()
                if act_type == 1:
                    self.next_page(self.login, self.student_setup)
                elif act_type == 2:
                    try:
                        open(user+str(act_type)+".txt", "x")
                    except FileExistsError:
                        pass
                    z = open(user+str(act_type)+".txt")
                    if "RefNo" in z.read():
                        pass
                    else:
                        reference_no = str(randint(1,1000000))
                        try:
                            open(user+str(act_type)+".txt", "x")
                        except FileExistsError:
                            pass
                        reference_write = open(user+str(act_type)+".txt", "a")
                        reference_write.write("RefNo" + reference_no + "\n")
                        reference_write.close()
                    try:
                        f = open("References.txt", "x")
                    except FileExistsError:
                        pass
                    write_r = open("References.txt", "a")
                    write_r.write(user+"\n")
                    write_r.close()
                    try:
                        open("CurrentLogged.txt", 'x')
                    except FileExistsError:
                        pass
                    with open("CurrentLogged.txt") as k:
                            lines = k.read()
                            first = lines.split('\n', 0)[0]
                            try:
                                open(first[:-2]+"2.txt", 'x')
                            except FileExistsError:
                                pass
                            with open(first[:-2]+"2.txt") as j:
                                top = j.read()
                                topline = top.split('\n', 0)[0]
                                if "RefNo" in z.read():
                                    pass
                                else:
                                    lbl22 = ttk.Label(self.reference, anchor = "center", text=("Reference Number: "+ topline.strip("RefNo")), font = ("Helvetica 10 underline"))
                                    lbl22.grid(row = 1, column = 6)
                                new_space = ttk.Label(self.reference, text = "                  ", width= 8)
                                new_space.grid(row = 100, column = 4, pady = 5)
                    self.next_page(self.login, self.reference_setup)
                elif act_type == 3:
                    reference_no = str(randint(1,1000000))
                    try:
                        open(user+str(act_type)+".txt", "x")
                    except FileExistsError:
                        pass
                    z = open(user+str(act_type)+".txt")
                    if "RefNo" in z.read():
                        pass
                    else:
                        reference_write = open(user+str(act_type)+".txt", "a")
                        reference_write.write("RefNo"+ reference_no + "\n")
                        reference_write.close()
                    try:
                        f = open("Employers.txt", 'x')
                    except FileExistsError:
                        pass
                    with open("Employers.txt") as file:
                        contents = file.read()
                        if user in contents:                          
                            self.next_page(self.login, self.employer)
                        else:
                            self.next_page(self.login, self.employer_setup)
                else:
                    print("Something went wrong")


    def user_check(self, username, password, act_type): #This function checks if the person logging in does
        #have an account and if their password matches
        space_check = username+password
        if len(space_check) == 0:
            lbl25 = Label(self.login, text="That account doesn't exist")
            lbl25.grid(row = 13, column = 3, columnspan=6)
        else:
            u_p = username+password+str(act_type) 
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
                    write_logs.write(username+str(act_type)+"\n")
                    write_logs.close()
                    try:
                        f = open("CurrentLogged.txt", "x")
                    except FileExistsError:
                        pass
                    write_clogs = open("CurrentLogged.txt", "w")
                    write_clogs.write(username+str(act_type)+"\n")
                    write_clogs.close()
                    if act_type == 1:
                        self.next_page(self.login, self.student)
                    elif act_type == 2:
                        try:
                            open("Students.txt", "x")
                        except FileExistsError:
                            pass
                        file = open("Students.txt", "r")
                        line_count = len(file.readlines())
                        for i in range(line_count):
                            file = open("Students.txt")
                            students = file.readlines()
                            stud = (str(students[i]))
                            stud = stud[:-1]
                            try:
                                open(stud+"1.txt", 'x')
                            except FileExistsError:
                                pass
                            referencelook = open(stud+"1.txt")
                            try:
                                open("Logged.txt", "x")
                            except FileExistsError:
                                pass
                            with open("Logged.txt") as h:
                                lines = h.read()
                                first = lines.split('\n', 0)[0].strip()
                            if first[:-1] in referencelook.read():
                                student_constant = ttk.Label(self.reference, text = "Student: ")
                                student_constant.grid(row = 10+i, column= 1)
                                new_label = ttk.Label(self.reference, text = stud, width=15)
                                new_label.grid(row = 10+i, column = 4)
                                new_apply = ttk.Button(self.reference, text = "Comment", command=lambda stud = stud : self.which_stud(stud), width=15)
                                new_apply.grid(row = 10+i, column = 6)
                                new_space = ttk.Label(self.reference, text = "                  ", width= 8)
                                new_space.grid(row = 10+i+1, column = 3, pady = 20)
                        try:
                            open("CurrentLogged.txt", 'x')
                        except FileExistsError:
                            pass
                        with open("CurrentLogged.txt") as k:
                                lines = k.read()
                                first = lines.split('\n', 0)[0]
                                try:
                                    open(first[:-2]+"2.txt", 'x')
                                except FileExistsError:
                                    pass
                                with open(first[:-2]+"2.txt") as j:
                                    top = j.read()
                                    topline = top.split('\n', 0)[0]
                                    lbl22 = ttk.Label(self.reference, anchor = "center", text=("Reference Number: "+ topline.strip("RefNo")), font = ("Helvetica 10 underline"))
                                    lbl22.grid(row = 1, column = 6)
                                    new_space = ttk.Label(self.reference, text = "                  ", width= 8)
                                    new_space.grid(row = 100, column = 4, pady = 5)
                        self.next_page(self.login, self.reference)
                    elif act_type == 3:
                        try:
                            open("Logged.txt", "x")
                        except FileExistsError:
                            pass
                        with open("Logged.txt") as h:
                            lines = h.read()
                            first = lines.split('\n', 0)[0].strip()
                            try:
                                open(first[:-1]+"3.txt", 'x')
                            except FileExistsError:
                                    pass
                            k = open(first[:-1]+"3.txt")
                            with open(first[:-1]+"3.txt") as j:
                                top = j.read()
                                if "RefNo" in top:
                                    pass
                                else:
                                    topline = top.split('\n', 0)[0]
                                    lbl22 = ttk.Label(self.employer, anchor = "center", text=("Reference Number: "+ topline.strip("RefNo")), font = ("Helvetica 12 underline"), width=40)
                                    lbl22.grid(row = 1, column = 2)
                                new_space = ttk.Label(self.employer, text = "                  ", width= 8)
                                new_space.grid(row = 2, column = 3, pady = 5)
                            try:
                                f = open("Employers.txt", 'x')
                            except FileExistsError:
                                pass
                            with open("Employers.txt") as file:
                                contents = file.read()
                                if username in contents:                           
                                    self.next_page(self.login, self.employer)
                                else:
                                    lbl25 = Label(self.login, text="That account doesn't exist")
                                    lbl25.grid(row = 13, column = 3, columnspan=6)
                    else:
                        lbl25 = Label(self.login, text="That account doesn't exist")
                        lbl25.grid(row = 13, column = 3, columnspan=6)
                else:
                    lbl25 = Label(self.login, text="That account doesn't exist")
                    lbl25.grid(row = 13, column = 3, columnspan=6)
                        


    def reject(self, student): 
        with open("Logged.txt") as h:
            lines = h.read()
            first = lines.split('\n', 0)[0].strip()
            try:
                k = open(first[:-1] +"Rejected.txt", 'x')
            except FileExistsError:
                pass
            write_rejected = open(first[:-1] + "Rejected.txt", 'a')
            write_rejected.write(student + "\n")
            write_rejected.close()
  
    def accept(self, student):
        with open("Logged.txt") as h:
            lines = h.read()
            first = lines.split('\n', 0)[0].strip()
            if student in open(first[:-1]+".txt").read():
                try:
                    f = open(first[:-1] + "Accepted.txt", 'x')
                except FileExistsError:
                    pass
                write_accepted = open(first[:-1] + "Accepted.txt", "a")
                write_accepted.write(student+"\n")
                write_accepted.close()
                import acceptedapplicants
        
            else:
                false_applicant = ttk.Label(self.employer, text = "Please enter a real applicant", width = 30)
                false_applicant.grid(row = 9, column = 1, columnspan= 4)
                time.sleep(3)
                false_applicant.destroy()

                

                         
    def which_stud(self, button_press):
        try:
            f = open("CurrentComment.txt", "x")
        except FileExistsError:
            pass
        write_comment = open("CurrentComment.txt", "w")
        write_comment.write(button_press+"\n")
        write_comment.close()
        with open("CurrentComment.txt") as h:
            lines = h.read()
            first = lines.split('\n', 0)[0].strip()
            with open("Logged.txt", "r") as d:
                commenter = d.readline().strip()
                commenter = commenter[:-1]
                self.next_page(self.reference, self.ref_comment)
      
        
    def comment(self, text):
        with open("CurrentComment.txt") as h:
            lines = h.read()
            first = lines.split('\n', 0)[0].strip()
            with open("Logged.txt") as d:
                commenter = d.readline().strip()
                j = open(first+"S.txt", 'a')
                j.write("Reference: " + commenter[:-1]+": "+ text + "\n")
                with open(commenter[:-1]+"T.txt") as t:
                    info = t.readlines()
                for i in range(len(info)):
                    j.write(info[i])
                j.write("\n")
                j.close()
                self.next_page(self.ref_comment, self.reference)

    def link(self, user, refno):
        if len(user) == 0:
            lbl10 = Label(self.link_ref, text="Please Enter a User", width = 20)
            lbl10.grid(row = 24, column = 3, columnspan=2)
        else:
            open_u = open("References.txt")
            with open("Logged.txt") as h:
                lines = h.read()
                first = lines.split('\n', 0)[0].strip()
            if user in open_u.read():
                open_e = open(user+"2.txt", "r")
                if ("RefNo" + str(refno)) in open_e.read():
                    try:
                        f = open(first+".txt", "x")
                    except FileExistsError:
                        pass
                    write_reference = open(first+".txt", "a")
                    write_reference.write(user+"\n")
                    write_reference.close()
                    self.next_page(self.link_ref, self.student)
                else:
                    lbl10 = Label(self.link_ref, text="That User does not exist", width = 42)
                    lbl10.grid(row = 24, column = 3, columnspan=6, sticky='W')
            else:
                lbl10 = Label(self.link_ref, text="That User does not exist", width = 42)
                lbl10.grid(row = 24, column = 3, columnspan=6, sticky='W')

    def search_application(self, user, refno):
        if len(user) == 0:
            lbl10 = Label(self.link_ref, text="Please Enter a User", width = 20)
            lbl10.grid(row = 24, column = 3, columnspan=2)
        else:
            open_u = open("Employers.txt")
            with open("Logged.txt") as h:
                lines = h.read()
                first = lines.split('\n', 0)[0].strip()
            if user in open_u.read():
                open_e = open(user+"3.txt", "r")
                if (refno) in open_e.read():
                    if first in open(user+".txt","r").read():
                        applied_label = ttk.Label(self.student, text = "You have applied already!", width = 30)
                        applied_label.grid(row = 15, column= 4)
                    else:
                        try:
                            f = open(user+".txt", "x")
                        except FileExistsError:
                            pass
                        with open(user+'.txt', 'r+') as file:
                            content = file.read()
                            file.seek(0)
                            file.write(first+"\n" + content)
                        applied_label = ttk.Label(self.student, text = "You have successfully applied!", width = 30)
                        applied_label.grid(row = 15, column= 4, columnspan= 3)
                        contact_label = ttk.Label(self.student, text = "You will be contacted later", width = 30)
                        contact_label.grid(row = 16, column= 4, columnspan= 3)

                else:
                    lbl10 = Label(self.link_ref, text="That User does not exist", width = 42)
                    lbl10.grid(row = 24, column = 3, columnspan=6)
            else:
                lbl10 = Label(self.link_ref, text="That User does not exist", width = 42)
                lbl10.grid(row = 24, column = 3, columnspan=6)

root = jobapp()
root.mainloop()