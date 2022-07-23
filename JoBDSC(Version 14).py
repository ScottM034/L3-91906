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
        signup_at = tk.IntVar() #Set the type of variable gained by the RadioButton
        login_at = tk.IntVar()
        login_label = ttk.Label(self.login, text="Login", font = ("Arial")) #Adding a bit of text in a specific page
        login_label.grid(row = 3, column = 4) #.grid sets the placement in the window with an imaginary grid
        name_l_label = ttk.Label(self.login, text="Name :", width = 15, font = ("Arial"))
        name_l_label.grid(row = 8, column = 2)
        username_l_entry = ttk.Entry(self.login, font =('Arial', 12), width = 30) #Creates a text box for the User to enter in
        username_l_entry.grid(row = 8, column = 3, columnspan=6)
        placeholder1 = ttk.Label(self.login, text="", width=1)
        placeholder1.grid(row = 9, column = 1)
        password_l_label = ttk.Label(self.login, text="Password :", width = 15, font = ("Arial"))
        password_l_label.grid(row = 10, column = 2)
        login_password_entry = ttk.Entry(self.login, font =('Arial', 12), width = 30)
        login_password_entry.grid(row = 10, column = 3, columnspan=6)
        placeholder2 = ttk.Label(self.login, text=" ", width=1)
        placeholder2.grid(row = 11, column = 1)
        account_type_l_label = ttk.Label(self.login, text = "Account Type :", font = ("Arial"), width= 15)
        account_type_l_label.grid(row=12, column = 2)
        student_l_rb = ttk.Radiobutton(self.login, text = "Student", variable=login_at, value = 1) #Creates a button that can be selected as one of 3
        #to figure out the user's account type
        student_l_rb.grid(row = 12, column = 3)
        reference_l_rb = ttk.Radiobutton(self.login, text = "Reference", variable=login_at, value = 2)
        reference_l_rb.grid(row = 12, column = 4)
        employer_l_rb = ttk.Radiobutton(self.login, text = "Employer", variable=login_at, value = 3)
        employer_l_rb.grid(row = 12, column = 5)
        login_button = ttk.Button(self.login, text="Login", command=lambda : self.user_check(username_l_entry.get(), login_password_entry.get(), login_at.get()))
        login_button.grid(row = 14, column = 4) #This button checks if the user's login is correct and tells them if something is wrong by use of a function
        placeholder33 = ttk.Label(self.login, text="", width=1)
        placeholder33.grid(row = 15, column = 1)
        signup_label = ttk.Label(self.login, text="Sign-Up", font = ("Arial"))
        signup_label.grid(row = 18, column = 4)
        name_s_label = ttk.Label(self.login, text="Name :", width = 15, font = ("Arial"))
        name_s_label.grid(row = 23, column = 2)
        username_s_entry = ttk.Entry(self.login, font =('Arial', 12), width = 30)
        username_s_entry.grid(row = 23, column = 3, columnspan=6)
        placeholder34 = ttk.Label(self.login, text=" ", width=1)
        placeholder34.grid(row = 24, column = 1)
        password_s_label = ttk.Label(self.login, text="Password :", width = 15, font = ("Arial"))
        password_s_label.grid(row = 25, column = 2)
        password_s_entry = ttk.Entry(self.login, font =('Arial', 12), width = 30)
        password_s_entry.grid(row = 25, column = 3, columnspan=6)
        signup_button = ttk.Button(self.login, text="Sign-Up", command=lambda : self.user_check_s(username_s_entry.get(), password_s_entry.get(), signup_at.get()))
        signup_button.grid(row = 28, column = 4) #This function tells the code that it is a new user and thus should be given the other type of login paeg
        placeholder35 = ttk.Label(self.login, text=" ", width=1)
        placeholder35.grid(row = 26, column = 1)
        account_type_s_label= ttk.Label(self.login, text = "Account Type :", font = ("Arial"), width = 15)
        account_type_s_label.grid(row = 27, column = 2)
        student_s_rb = ttk.Radiobutton(self.login, text = "Student", variable=signup_at, value = 1)
        student_s_rb.grid(row = 27, column = 3)
        reference_s_rb = ttk.Radiobutton(self.login, text = "Reference", variable=signup_at, value = 2)
        reference_s_rb.grid(row = 27, column = 4)
        employer_s_rb = ttk.Radiobutton(self.login, text = "Employer", variable=signup_at, value = 3)
        employer_s_rb.grid(row = 27, column = 5)

        #Reference Page Code
        placeholder = ttk.Label(self.reference, text= ' ')
        placeholder.grid(row = 0, column= 0)
        logout_r_button = ttk.Button(self.reference, text="Logout", command = lambda : self.next_page(self.reference, self.login), width=14)
        logout_r_button.grid(row = 1, column = 1)
        students_r_label = ttk.Label(self.reference, text = "Your Students", font = ("Helvetica 14 underline"))
        students_r_label.grid(row = 2, column = 3, columnspan= 2)

        #ReferenceCommenting Page
        placeholder36 = ttk.Label(self.ref_comment, text = " ")
        placeholder36.grid(row = 1, column = 1)
        comment_rc_label = ttk.Label(self.ref_comment, text = "Comment as a Reference: ", width = 30)
        comment_rc_label.grid(row = 7, column = 2, columnspan= 2)
        placeholder37 = ttk.Label(self.ref_comment, text = " ")
        placeholder37.grid(row = 8, column = 1)
        comment_rc_entry = ttk.Entry(self.ref_comment, width = 30)
        comment_rc_entry.grid(row = 7, column = 6, columnspan = 2)
        comment_rc_button = ttk.Button(self.ref_comment, text = "Comment", command=lambda : self.comment(str(comment_rc_entry.get())))
        comment_rc_button.grid(row = 9, column = 7)
        cancel_rc_button = ttk.Button(self.ref_comment, text = "Cancel", command=lambda : self.next_page(self.ref_comment, self.reference))
        cancel_rc_button.grid(row = 9, column = 6)

        #Linking a Reference Page
        link_a_reference_label = ttk.Label(self.link_ref, text="Link a Reference", width = 20)
        link_a_reference_label.grid(row = 3, column = 3, columnspan=2)
        name_label = ttk.Label(self.link_ref, text="Name :", width = 15)
        name_label.grid(row = 8, column = 2)
        linked_reference = ttk.Entry(self.link_ref, width = 30)
        linked_reference.grid(row = 8, column = 3, columnspan=6)
        placeholder3 = ttk.Label(self.link_ref, text="", width=1)
        placeholder3.grid(row = 9, column = 1)
        reference_number_label = ttk.Label(self.link_ref, text="Reference Number :", width = 25)
        reference_number_label.grid(row = 10, column = 2)
        refno = ttk.Entry(self.link_ref, width = 30)
        refno.grid(row = 10, column = 3, columnspan=6)
        placeholder4 = ttk.Label(self.link_ref, text=" ", width=1)
        placeholder4.grid(row = 11, column = 1)
        link_button = ttk.Button(self.link_ref, text = "Link", width = 20, command = lambda : self.link(linked_reference.get(), refno.get()))
        link_button.grid(row = 12, column = 3)
        cancel_button= ttk.Button(self.link_ref, text = "Cancel", width = 20, command = lambda : self.cancel_lr())
        cancel_button.grid(row = 12, column = 4)
        placeholder5 = ttk.Label(self.link_ref, text="   ", width=1)
        placeholder5.grid(row = 13, column = 1)

        #Student Page 1
        company_list_button = ttk.Button(self.student, text="Company List", command = lambda : self.employer_list(), width = 20)
        company_list_button.grid(row = 0, column = 2, columnspan= 3)
        link_reference_button = ttk.Button(self.student, text="Link a Reference", command = lambda : self.next_page(self.student, self.link_ref), width=15)
        link_reference_button.grid(row = 0, column = 1)
        logout_button = ttk.Button(self.student, text="Logout", command = lambda : self.next_page(self.student, self.login), width=14)
        logout_button.grid(row = 0, column = 5, columnspan= 2)
        placeholder6 = ttk.Label(self.student, text ="  ", width = 1)
        placeholder6.grid(row=1, column = 1)
        placeholder7 = ttk.Label(self.student, text ="  ", width = 8)
        placeholder7.grid(row=1, column = 6)
        placeholder8 = ttk.Label(self.student, text ="  ", width = 10)
        placeholder8.grid(row=1, column = 4)
        try: #This section just creates a file if it is not already created so that the code can check what is in the file later
            open("Employers.txt", "x")
        except FileExistsError:
            pass
        placeholder9 = ttk.Label(self.student, text = '   ')
        placeholder9.grid(row = 2, column = 0)
        search_company_label = ttk.Label(self.student, text = "Company Name:", width = 20)
        search_company_label.grid(row = 3, column = 2, columnspan= 2)
        search_bar = ttk.Entry(self.student, font =('Arial', 12), width = 20)
        search_bar.grid(row = 3, column = 4, columnspan= 2)
        company_number = ttk.Entry(self.student, font = ('Arial', 12), width = 20)
        company_number.grid(row = 5, column = 4, columnspan=2)
        company_number_label = ttk.Label(self.student, text = "Company Number:", width = 20)
        company_number_label.grid(row = 5, column = 2, columnspan= 2)
        placeholder10 = ttk.Label(self.student, text = " ", width = 3)
        placeholder10.grid(row = 4, column = 4)
        placeholder11 = ttk.Label(self.student, text = " ", width = 3)
        placeholder11.grid(row = 6, column = 4)
        apply_button = ttk.Button(self.student, text = "Apply", width = 20, command = lambda : self.search_application(search_bar.get(), company_number.get(), ))
        apply_button.grid(row = 7, column = 4, columnspan= 2)


        #Employer Information Page
        setup_e_label = ttk.Label(self.employer_setup, text="Set-Up", width=15)
        setup_e_label.grid(row = 3, column = 3)
        job_title_e_label = ttk.Label(self.employer_setup, text="Job Title:", width = 15)
        job_title_e_label.grid(row = 8, column = 2)
        job_title_e_entry = ttk.Entry(self.employer_setup, font =('Arial', 12), width = 30)
        job_title_e_entry.grid(row = 8, column = 3, columnspan=6)
        placeholder12 = ttk.Label(self.employer_setup, text="", width=1)
        placeholder12.grid(row = 9, column = 1)
        location_e_label = ttk.Label(self.employer_setup, text="Location:", width = 15)
        location_e_label.grid(row = 10, column = 2)
        location_e_entry = ttk.Entry(self.employer_setup, font =('Arial', 12), width = 30)
        location_e_entry.grid(row = 10, column = 3, columnspan=6)
        placeholder13 = ttk.Label(self.employer_setup, text="", width=1)
        placeholder13.grid(row = 12, column = 1)
        email_e_label = ttk.Label(self.employer_setup, text="Email:", width = 15)
        email_e_label.grid(row = 23, column = 2)
        email_e_entry = ttk.Entry(self.employer_setup, font =('Arial', 12), width = 30)
        email_e_entry.grid(row = 23, column = 3, columnspan=6)
        placeholder14 = ttk.Label(self.employer_setup, text=" ", width=1)
        placeholder14.grid(row = 25, column = 1)
        mobile_e_label = ttk.Label(self.employer_setup, text="Mobile Number:", width = 15)
        mobile_e_label.grid(row = 27, column = 2)
        mobile_e_entry = ttk.Entry(self.employer_setup, font =('Arial', 12), width = 30)
        mobile_e_entry.grid(row = 27, column = 3, columnspan=6)
        placeholder15 = ttk.Label(self.employer_setup, text=" ", width=1)
        placeholder15.grid(row = 29, column = 1)
        finish_e_button = ttk.Button(self.employer_setup, text="Finish", command=lambda : self.finish(job_title_e_entry.get(), location_e_entry.get(), email_e_entry.get(), mobile_e_entry.get()))
        finish_e_button.grid(row = 30, column = 3)

        #Employer Page
        logout_e_button = ttk.Button(self.employer, text="Logout", command = lambda : self.next_page(self.employer, self.login), width=14)
        logout_e_button.grid(row = 0, column = 2)
        try:
            open("CurrentLogged.txt", 'x')
        except FileExistsError:
            pass
        with open("CurrentLogged.txt") as h: #This section of code gets the first line of the desired external file
                    lines = h.read()
                    employer = lines.split('\n', 0)[0].strip()
        placeholder16 = ttk.Label(self.employer, text = ' ')
        placeholder16.grid(row = 0 ,column=0)
        delete_listing = ttk.Button(self.employer, text="Delete Listing", command = lambda : self.delete(employer), width=14)
        delete_listing.grid(row = 0, column = 1, columnspan=1)
        view_applicants_button = ttk.Button(self.employer, text = "View Applicants", command = lambda : self.view_applicants(), width = 40)
        view_applicants_button.grid(row = 3, column = 2)
        placeholder17 = ttk.Label(self.employer, text = ' ')
        placeholder17.grid(row = 4 ,column=0)
        applicant_name_label = ttk.Label(self.employer, text = "Applicant Name: ")
        applicant_name_label.grid(row = 5, column = 1)
        applicant_name_entry = ttk.Entry(self.employer, width = 40)
        applicant_name_entry.grid(row = 5, column = 2)
        placeholder18 = ttk.Label(self.employer, text = ' ')
        placeholder18.grid(row = 6,column=0)
        accept_applicant_button = ttk.Button(self.employer, text = "Accept", width = 40, command = lambda : self.accept(applicant_name_entry.get()))
        accept_applicant_button.grid (row = 8, column = 2)
        placeholder19 = ttk.Label(self.employer, text = ' ')
        placeholder19.grid(row = 9 ,column=0)
        accepted_applicants_button = ttk.Button(self.employer, text = "Accepted Applicants", width = 40, command = lambda : self.accepted_list())
        accepted_applicants_button.grid(row = 13, column = 2)



        #Student Information Page
        student_information_label = ttk.Label(self.student_setup, text = "Student Information", width = 30)
        student_information_label.grid(row = 1, column = 4)
        achievements_s_label = ttk.Label(self.student_setup, text="Achievements:", width = 15)
        achievements_s_label.grid(row = 8, column = 2)
        achievements_s_entry = ttk.Entry(self.student_setup, font =('Arial', 12), width = 30)
        achievements_s_entry.grid(row = 8, column = 3, columnspan=6)
        placeholder20 = ttk.Label(self.student_setup, text="", width=1)
        placeholder20.grid(row = 9, column = 1)
        location_s_label = ttk.Label(self.student_setup, text="Location:", width = 15)
        location_s_label.grid(row = 10, column = 2)
        location_s_entry = ttk.Entry(self.student_setup, font =('Arial', 12), width = 30)
        location_s_entry.grid(row = 10, column = 3, columnspan=6)
        placeholder21 = ttk.Label(self.student_setup, text="", width=1)
        placeholder21.grid(row = 12, column = 1)
        email_s_label = ttk.Label(self.student_setup, text="Email:", width = 15)
        email_s_label.grid(row = 23, column = 2)
        email_s_entry = ttk.Entry(self.student_setup, font =('Arial', 12), width = 30)
        email_s_entry.grid(row = 23, column = 3, columnspan=6)
        placeholder22 = ttk.Label(self.student_setup, text=" ", width=1)
        placeholder22.grid(row = 25, column = 1)
        mobile_s_label = ttk.Label(self.student_setup, text="Mobile Number:", width = 15)
        mobile_s_label.grid(row = 27, column = 2)
        mobile_s_entry = ttk.Entry(self.student_setup, font =('Arial', 12), width = 30)
        mobile_s_entry.grid(row = 27, column = 3, columnspan=6)
        placeholder23 = ttk.Label(self.student_setup, text=" ", width=1)
        placeholder23.grid(row = 29, column = 1)
        finish_s_button = ttk.Button(self.student_setup, text="Finish", command=lambda : self.finish_s(achievements_s_entry.get(), location_s_entry.get(), email_s_entry.get(), mobile_s_entry.get()))
        finish_s_button.grid(row = 30, column = 3)
        
        #Reference Information Page
        setup_r_label = ttk.Label(self.reference_setup, text="Set-Up", width=15)
        setup_r_label.grid(row = 3, column = 3, columnspan= 6)
        job_title_r_label = ttk.Label(self.reference_setup, text="Reference Job:", width = 15)
        job_title_r_label.grid(row = 8, column = 2)
        job_title_r_entry = ttk.Entry(self.reference_setup, font =('Arial', 12), width = 30)
        job_title_r_entry.grid(row = 8, column = 3, columnspan=6)
        placeholder24 = ttk.Label(self.reference_setup, text="", width=1)
        placeholder24.grid(row = 12, column = 1)
        email_r_label = ttk.Label(self.reference_setup, text="Email:", width = 15)
        email_r_label.grid(row = 23, column = 2)
        email_r_entry = ttk.Entry(self.reference_setup, font =('Arial', 12), width = 30)
        email_r_entry.grid(row = 23, column = 3, columnspan=6)
        placeholder25 = ttk.Label(self.reference_setup, text=" ", width=1)
        placeholder25.grid(row = 25, column = 1)
        mobile_r_label = ttk.Label(self.reference_setup, text="Mobile Number:", width = 15)
        mobile_r_label.grid(row = 27, column = 2)
        mobile_r_entry = ttk.Entry(self.reference_setup, font =('Arial', 12), width = 30)
        mobile_r_entry.grid(row = 27, column = 3, columnspan=6)
        placeholder26 = ttk.Label(self.reference_setup, text=" ", width=1)
        placeholder26.grid(row = 29, column = 1)
        finish_r_button = ttk.Button(self.reference_setup, text="Finish", command=lambda : self.finish_t(job_title_r_entry.get(), email_r_entry.get(), mobile_r_entry.get()))
        finish_r_button.grid(row = 30, column = 3)

    def view_applicants(self): #Function that calls another code to show the applicants for an employer
        import employerpageV4

    def accepted_list(self): #Function that calls another code to show the employer's accepted applicants
        import acceptedapplicantsV4

    def employer_list(self):
        import studentpageV4

    def callback(self, url): #Function that opens the URL that I want the program to link to
        webbrowser.open_new(url)

    def cancel_lr(self):
        empty_user_lr_label = ttk.Label(self.link_ref, text="           ", width = 42)
        empty_user_lr_label.grid(row = 24, column = 3, columnspan=2)
        invalid_user_lr_label = ttk.Label(self.link_ref, text="           ", width = 42)
        invalid_user_lr_label.grid(row = 24, column = 3, columnspan=6, sticky='W')
        self.next_page(self.link_ref, self.student) 


    def finish(self, job_t, location, email, phone): #From the user's intital sign-up we create a file that has all his information
        if "@" not in str(email): #Checking if the email the user entered is invalid
            invalid_email_e_label = ttk.Label(self.employer_setup, text="Please enter a valid email", width = 30)
            invalid_email_e_label.grid(row = 24, column = 3, columnspan=2)
        else:
            invalid_email_e_label = ttk.Label(self.employer_setup, text="                          ", width = 30)
            invalid_email_e_label.grid(row = 24, column = 3, columnspan=2)
            if len(phone) < 9: #Checking if the mobile number the user entered is invalid
                invalid_mobile_e_label = ttk.Label(self.employer_setup, text="Please enter a valid Mobile Number", width = 35)
                invalid_mobile_e_label.grid(row = 28, column = 3, columnspan=2)
            else:
                invalid_mobile_e_label = ttk.Label(self.employer_setup, text="                                  ", width = 35)
                invalid_mobile_e_label.grid(row = 28, column = 3, columnspan=2)
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
                    write_i.write("Mobile Number: "+ phone +"\n" + "\n")
                    write_i.close()
                    try:
                        open(first[:-1]+"3.txt", 'x')
                    except FileExistsError:
                            pass
                    with open(first[:-1]+"3.txt") as j:
                        top = j.read()
                        topline = top.split('\n', 0)[0]
                        reference_number_e_label = ttk.Label(self.employer, anchor = "center", text=("Reference Number: "+ topline.strip("RefNo")), font = ("Helvetica 12 underline"))
                        reference_number_e_label.grid(row = 1, column = 2)
                    self.next_page(self.employer_setup, self.employer)

    def finish_s(self, job_t, location, email, phone): #Function that adds the information for a new student that signed up
        if "@" not in email:
            invalid_email_s_label = ttk.Label(self.student_setup, text="Please enter a valid email", width = 30)
            invalid_email_s_label.grid(row = 24, column = 3, columnspan=2)
        else:
            invalid_email_s_label = ttk.Label(self.student_setup, text="                          ", width = 30)
            invalid_email_s_label.grid(row = 24, column = 3, columnspan=2)
            if len(phone) < 9:
                invalid_mobile_s_label = ttk.Label(self.student_setup, text="Please enter a valid Mobile Number", width = 35)
                invalid_mobile_s_label.grid(row = 28, column = 3, columnspan=2)
                
            else:
                invalid_mobile_s_label = ttk.Label(self.student_setup, text="                                  ", width = 35)
                invalid_mobile_s_label.grid(row = 28, column = 3, columnspan=2)
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
                    write_i.write("Mobile Number: "+ phone +"\n" + "\n")
                    write_i.close()
                    self.next_page(self.student_setup, self.student)

    def delete(self, employer): #Function to delete an employer account when they want so their application
        # does not sit on the app when a job is not available
        with open('AccountTypes.txt', 'r') as file :
            filedata = file.read()
        filedata = filedata.replace(employer, str(randint(10000, 10000000000)))
        with open('AccountTypes.txt', 'w') as file:
            file.write(filedata)
        employer = employer.strip("3")
        with open('Employers.txt', 'r') as file :
            filedata = file.read()
        filedata = filedata.replace(employer, str(randint(10000, 10000000000)))
        with open('Employers.txt', 'w') as file:
            file.write(filedata)
        with open('Usernames.txt', 'r') as file :
            filedata = file.read()
        filedata = filedata.replace(employer, str(randint(10000,10000000000)))
        with open('Usernames.txt', 'w') as file:
            file.write(filedata)
        self.next_page(self.employer, self.login)




    def finish_t(self, job_t, email, phone): #Adds information when a new reference is added
        if "@" not in email:
            invalid_email_r_label = ttk.Label(self.reference_setup, text="Please enter a valid email", width = 30)
            invalid_email_r_label.grid(row = 24, column = 3, columnspan=2)
        else:
            invalid_email_r_label = ttk.Label(self.reference_setup, text="                          ", width = 30)
            invalid_email_r_label.grid(row = 24, column = 3, columnspan=2)
            if len(phone) < 9:
                invalid_mobile_r_label = ttk.Label(self.reference_setup, text="Please enter a valid Mobile Number", width = 35)
                invalid_mobile_r_label.grid(row = 28, column = 3, columnspan=2)
            else:
                invalid_mobile_r_label = ttk.Label(self.reference_setup, text="                                  ", width = 35)
                invalid_mobile_r_label.grid(row = 28, column = 3, columnspan=2)
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
                    write_i.write("Mobile Number: "+ phone +"\n" + "\n")
                    write_i.close()
                    try:
                        open(first[:-1]+"2.txt", 'x')
                    except FileExistsError:
                            pass
                    with open(first[:-1]+"2.txt") as j:
                        top = j.read()
                        topline = top.split('\n', 0)[0]
                        reference_number_r_label = ttk.Label(self.reference, anchor = "center", text=("Reference Number: "+ topline.strip("RefNo")), font = ("Helvetica 10 underline"))
                        reference_number_r_label.grid(row = 1, column = 6)
                    self.next_page(self.reference_setup, self.reference)


    def next_page(self, current, next): 
        #This will take the User from their current frame to the next indended frame depending on which button they pressed
        current.pack_forget()
        next.pack()

    def user_check_s(self, user, password, act_type): #This checks a signing up user if they already have an account
        #or if their password does not meet the requirements for security
        invalid_password_signup = ttk.Label(self.login, text="", width = 42)
        invalid_password_signup.grid(row = 24, column = 3, columnspan=6, sticky='W')
        invalid_username_l_label = ttk.Label(self.login, text="", width = 40)
        invalid_username_l_label.grid(row = 26, column = 3, columnspan=3)
        if len(user) == 0:
            invalid_username_signup = ttk.Label(self.login, text="Username should be your name", width = 42)
            invalid_username_signup.grid(row = 24, column = 3, columnspan=6, sticky='W')
        else:
            if len(password) < 8:
                invalid_password_signup = ttk.Label(self.login, text="Password should be 8 characters or more", width = 42)
                invalid_password_signup.grid(row = 24, column = 3, columnspan=6, sticky='W')
            else:
                try:
                    f = open("Usernames.txt", "x")
                    g = open("Passwords.txt", "x")
                    h = open("AccountTypes.txt", "x")
                except FileExistsError:
                    pass
                username_check = open("AccountTypes.txt")
                if act_type == 0:
                    invalid_acttype_signup = ttk.Label(self.login, text="Please enter an act type", width = 42)
                    invalid_acttype_signup.grid(row = 24, column = 3, columnspan=6, sticky='W')
                elif user+str(act_type) in username_check.read():
                    invalid_username_l_label = ttk.Label(self.login, text="Username already exists, please try again", width = 40)
                    invalid_username_l_label.grid(row = 26, column = 3, columnspan=3)
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
                                        reference_number_r_label = ttk.Label(self.reference, anchor = "center", text=("Reference Number: "+ topline.strip("RefNo")), font = ("Helvetica 10 underline"))
                                        reference_number_r_label.grid(row = 1, column = 6)
                        self.next_page(self.login, self.reference_setup)
                    elif act_type == 3:
                        reference_no = str(randint(1,1000000))
                        try:
                            open(user+str(act_type)+".txt", "x")
                        except FileExistsError:
                            pass
                        try:
                            z = open(user+"E.txt", "x")
                        except FileExistsError:
                            pass
                        z = open(user+"3.txt")
                        if "RefNo" in z.read():
                            pass
                        else:
                            reference_write = open(user+str(act_type)+".txt", "a")
                            reference_write.write("RefNo"+ reference_no + "\n")
                            reference_write.close()
                        try:
                            x = open(user+"3.txt", "x")
                        except FileExistsError:
                            pass
                        x = open(user + "E.txt")
                        if "Location" in x.read():
                            self.next_page(self.login, self.employer)
                        else:                         
                            self.next_page(self.login, self.employer_setup)
                    else:
                        invalid_username_signup = ttk.Label(self.login, text="Please select an account type", width = 42)
                        invalid_username_signup.grid(row = 24, column = 3, columnspan=6, sticky='W')


    def user_check(self, username, password, act_type): #This function checks if the person logging in does
        #have an account and if their password matches
        invalid_account_label = Label(self.login, text=" ", width = 25)
        invalid_account_label.grid(row = 13, column = 3, columnspan=6)
        space_check = username+password
        if len(space_check) == 0:
            invalid_account_label = Label(self.login, text="That account doesn't exist")
            invalid_account_label.grid(row = 13, column = 3, columnspan=6)
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
                                student_title_r_label = ttk.Label(self.reference, text = "Student: ")
                                student_title_r_label.grid(row = 10+i, column= 1)
                                student_r_label = ttk.Label(self.reference, text = stud, width=15)
                                student_r_label.grid(row = 10+i, column = 4)
                                comment_r_label = ttk.Button(self.reference, text = "Comment", command=lambda stud = stud : self.which_stud(stud), width=15)
                                comment_r_label.grid(row = 10+i, column = 6)
                                placeholder30 = ttk.Label(self.reference, text = "                  ", width= 8)
                                placeholder30.grid(row = 10+i+1, column = 3, pady = 20)
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
                                    reference_number_r_label = ttk.Label(self.reference, anchor = "center", text=("Reference Number: "+ topline.strip("RefNo")), font = ("Helvetica 10 underline"))
                                    reference_number_r_label.grid(row = 1, column = 6)
                                    placeholder31 = ttk.Label(self.reference, text = "                  ", width= 8)
                                    placeholder31.grid(row = 100, column = 4, pady = 5)
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
                                topline = top.split('\n', 0)[0]
                                reference_number_e_label = ttk.Label(self.employer, anchor = "center", text=("Reference Number: "+ topline.strip("RefNo")), font = ("Helvetica 12 underline"), width=40)
                                reference_number_e_label.grid(row = 1, column = 2)
                            try:
                                f = open("Employers.txt", 'x')
                            except FileExistsError:
                                pass
                            with open("Employers.txt") as file:
                                contents = file.read()
                                if username in contents:                           
                                    self.next_page(self.login, self.employer)
                                else:
                                    invalid_account_label = Label(self.login, text="That account doesn't exist")
                                    invalid_account_label.grid(row = 13, column = 3, columnspan=6)
                    else:
                        invalid_account_label = Label(self.login, text="Please select an account type")
                        invalid_account_label.grid(row = 13, column = 3, columnspan=6)
                else:
                    invalid_account_label = Label(self.login, text="That account doesn't exist")
                    invalid_account_label.grid(row = 13, column = 3, columnspan=6)
                        
  
    def accept(self, student): #Adds the accepted student to an external list for the company
        false_applicant_e_label = ttk.Label(self.employer, text = " ", width = 30)
        false_applicant_e_label.grid(row = 9, column = 2, columnspan= 2)
        with open("Logged.txt") as h:
            lines = h.read()
            first = lines.split('\n', 0)[0].strip()
            if len(student) == 0:
                false_applicant_e_label = ttk.Label(self.employer, text = "Please enter a student", width = 25)
                false_applicant_e_label.grid(row = 9, column = 2, columnspan= 2)
            elif student in open(first[:-1]+".txt").read(): #Checks if the user entered is actually applied
                try:
                    f = open(first[:-1] + "Accepted.txt", 'x')
                except FileExistsError:
                    pass
                accepted_check = open(first[:-1] + "Accepted.txt")
                if student in accepted_check.read():
                    false_applicant_e_label = ttk.Label(self.employer, text = "Student is already accepted", width = 25)
                    false_applicant_e_label.grid(row = 9, column = 2, columnspan= 2)
                else:
                    write_accepted = open(first[:-1] + "Accepted.txt", "a")
                    write_accepted.write(student+"\n")
                    write_accepted.close()
                    import acceptedapplicantsV4 #Imports another code which shows the employer their accepted applicants
            else: 
                false_applicant_e_label = ttk.Label(self.employer, text = "Please enter a real applicant", width = 25)
                false_applicant_e_label.grid(row = 9, column = 2, columnspan= 2)

                

                         
    def which_stud(self, button_press): #Checks which student is being commented on
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
      
        
    def comment(self, text): #Comments on the selected student and adds to their file
        with open("CurrentComment.txt") as h:
            lines = h.read()
            first = lines.split('\n', 0)[0].strip()
            with open("Logged.txt") as d:
                commenter = d.readline().strip()
                j = open(first+"S.txt", 'a')
                j.write("Reference: " + commenter[:-1] + "\n")
                j.write("Comment: " + '"' + text + '"' + "\n")
                with open(commenter[:-1]+"T.txt") as t:
                    info = t.readlines()
                for i in range(len(info)):
                    j.write(info[i])
                j.write("\n")
                j.close()
                self.next_page(self.ref_comment, self.reference)

    def link(self, user, refno): #Links a reference to a student when the student enters them
        empty_user_lr_label = Label(self.link_ref, text=" ", width = 20)
        empty_user_lr_label.grid(row = 24, column = 3, columnspan=2)
        invalid_user_lr_label = Label(self.link_ref, text=" ", width = 42)
        invalid_user_lr_label.grid(row = 24, column = 3, columnspan=6, sticky='W')
        if len(user) == 0:
            empty_user_lr_label = Label(self.link_ref, text="Please Enter a User", width = 20)
            empty_user_lr_label.grid(row = 24, column = 3, columnspan=2)
        else:
            try:
                open("References.txt", 'x')
            except FileExistsError:
                pass
            open_u = open("References.txt")
            with open("Logged.txt") as h:
                lines = h.read()
                first = lines.split('\n', 0)[0].strip()
            if user in open_u.read():
                open_e = open(user+"2.txt", "r")
                if len(refno) == 0:
                    invalid_user_lr_label = Label(self.link_ref, text="Please enter a reference number", width = 42)
                    invalid_user_lr_label.grid(row = 24, column = 3, columnspan=6, sticky='W')
                elif ("RefNo" + str(refno)) in open_e.read():
                    try:
                        f = open(first+".txt", "x")
                    except FileExistsError:
                        pass
                    write_reference = open(first+".txt", "a")
                    write_reference.write(user+"\n")
                    write_reference.close()
                    self.next_page(self.link_ref, self.student)
                else:
                    invalid_user_lr_label = Label(self.link_ref, text="That User does not exist", width = 42)
                    invalid_user_lr_label.grid(row = 24, column = 3, columnspan=6, sticky='W')
            else:
                invalid_user_lr_label = Label(self.link_ref, text="That User does not exist", width = 42)
                invalid_user_lr_label.grid(row = 24, column = 3, columnspan=6, sticky='W')

    def search_application(self, user, refno): #Checks if the user has applied for a company
        no_user_lr_label = Label(self.student, text=" ", width = 42)
        no_user_lr_label.grid(row = 24, column = 3, columnspan=6)
        applied_s_label = ttk.Label(self.student, text = " ", width = 30)
        applied_s_label.grid(row = 15, column= 4)
        applied_s_label = ttk.Label(self.student, text = " ", width = 30)
        applied_s_label.grid(row = 15, column= 4, columnspan= 3)
        if len(user) == 0:
            no_user_lr_label = Label(self.student, text="Please Enter a User", width = 42)
            no_user_lr_label.grid(row = 24, column = 3, columnspan=6)
        else:
            open_u = open("Employers.txt")
            with open("Logged.txt") as h:
                lines = h.read()
                first = lines.split('\n', 0)[0].strip()
            if user in open_u.read():
                open_e = open(user+"3.txt", "r")
                if len(refno) == 0:
                    applied_s_label = ttk.Label(self.student, text = "Please enter the company number", width = 30)
                    applied_s_label.grid(row = 15, column= 4)
                elif (refno) in open_e.read():
                    if first in open(user+".txt","r").read():
                        applied_s_label = ttk.Label(self.student, text = "You have applied already!", width = 30)
                        applied_s_label.grid(row = 15, column= 4)
                    else:
                        try:
                            f = open(user+".txt", "x")
                        except FileExistsError:
                            pass
                        with open(user+'.txt', 'r+') as file:
                            content = file.read()
                            file.seek(0)
                            file.write(first+"\n" + content)
                        applied_s_label = ttk.Label(self.student, text = "You have successfully applied!", width = 30)
                        applied_s_label.grid(row = 15, column= 4, columnspan= 3)
                        contact_s_label = ttk.Label(self.student, text = "You will be contacted later", width = 30)
                        contact_s_label.grid(row = 16, column= 4, columnspan= 3)
                else:
                    invalid_user_lr_label = Label(self.student, text="That User does not exist", width = 42)
                    invalid_user_lr_label.grid(row = 24, column = 3, columnspan=6)
            else:
                invalid_user_lr_label = Label(self.student, text="That User does not exist", width = 42)
                invalid_user_lr_label.grid(row = 24, column = 3, columnspan=6)

root = jobapp()
root.mainloop() #Causes the root to run which is defined as the code itself, showing the page