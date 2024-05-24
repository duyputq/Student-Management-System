from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import smtplib
from SQLaccount import host_name, user_name, password_key, database_name
from emailAccount import email_account, app_password

class Student:
    #UI
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("QUAN LY SINH VIEN")

        #variable
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_email = StringVar()
        self.var_dob = StringVar()
        self.var_grade = StringVar()
        self.var_avr = StringVar()
        self.var_scholarship = StringVar()
        self.var_creadits = StringVar()
        

        #1st
        img = Image.open(r"college_images\1.png")
        img = img.resize((540,160), Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        self.btn_1 = Button(self.root, image=self.photoimg, cursor="hand2")
        self.btn_1.place(x=0,y=0,width=540,height=160)

        #2st
        img_2 = Image.open(r"college_images\2.png")
        img_2 = img_2.resize((540,160), Image.ADAPTIVE)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        self.btn_1 = Button(self.root, image=self.photoimg_2, cursor="hand2")
        self.btn_1.place(x=510,y=0,width=540,height=160)

        #3rd
        img_5 = Image.open(r"college_images\3.png")
        img_5 = img_5.resize((540,160), Image.ADAPTIVE)
        self.photoimg_3 = ImageTk.PhotoImage(img_5)

        self.btn_1 = Button(self.root, image=self.photoimg_3, cursor="hand2")
        self.btn_1.place(x=1020,y=0,width=540,height=160)

        #bg

        img_4 = Image.open(r"college_images\uet_university.png")
        img_4 = img_4.resize((1530,710), Image.ADAPTIVE)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)

        bg_lbl = Label(self.root, image=self.photoimg_4, bd=2, relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1530,height=710)
        
        lbl_title = Label(bg_lbl, text="CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN", font=("times new roman",33,"bold"), fg = "blue", bg="white")
        lbl_title.place(x=0,y=0, width=1530, height=50)
        # manage frame
        Mange_frame = Frame(bg_lbl, bd = 2, relief=RIDGE, bg="white")
        Mange_frame.place(x=15,y=55, width=1500,height=800)

        #left frame 
        DataLeft = LabelFrame(Mange_frame,bd=4, relief=RIDGE,padx=2, text="THÔNG TIN SINH VIÊN", font=("times new roman",12,"bold"), fg = "red", bg="white")
        DataLeft.place(x=10,y=10, width=660, height=540)

        #img
        img_5 = Image.open(r"college_images\kinhte.png")
        img_5 = img_5.resize((550,150), Image.ADAPTIVE)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)

        my_img = Label(DataLeft, image=self.photoimg_5, bd=2, relief=RIDGE)
        my_img.place(x=0,y=0,width=650,height=120)

        # Current course LabelFrame Information
        std_lbl_info_frame = LabelFrame(DataLeft, bd=4, relief=RIDGE, padx=2, text="Ngành học", font=("times new roman",12,"bold"), fg = "red", bg="white")
        std_lbl_info_frame.place(x=0,y=120,width=650, height=70)
        
    
        # Major
        lbl_dep = Label(std_lbl_info_frame,text="Major", font=("arial",12,"bold"), bg="white")
        lbl_dep.grid(row=0, column=0, padx=2,sticky=W)

        combo_dep = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_dep, font=("arial",12,"bold"), width=30, state="readonly")
        combo_dep["value"] = ("Select Major", "Computer Science","Computer Engineering" ,"Electrical Engineering","Telecomunication Engineering")
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

       
       # Class course LabelFrame Information
        std_lbl_class_frame = LabelFrame(DataLeft, bd=4, relief=RIDGE, padx=2, text="Thông tin cá nhân", font=("times new roman",12,"bold"), fg = "red", bg="white")
        std_lbl_class_frame.place(x=0,y=200,width=650, height=250)

        #ID
        lbl_id = Label(std_lbl_class_frame, font=("arial",12,"bold"),text="Student ID:", bg="white")
        lbl_id.grid(row=0, column=0,sticky=W,padx=2,pady=7)

        id_entry = ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_id, font=("arial",12,"bold"),width=20)
        id_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)

        #Name
        lbl_id = Label(std_lbl_class_frame, font=("arial",12,"bold"),text="Student Name:", bg="white")
        lbl_id.grid(row=0, column=2,sticky=W,padx=2,pady=7)

        id_entry = ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_name, font=("arial",12,"bold"),width=17)
        id_entry.grid(row=0,column=3,sticky=W,padx=2,pady=7)


        #Class division
        lbl_id = Label(std_lbl_class_frame, font=("arial",12,"bold"),text="Class devision:", bg="white")
        lbl_id.grid(row=1, column=0,sticky=W,padx=2,pady=7)

        id_entry = ttk.Combobox(std_lbl_class_frame,textvariable=self.var_div, font=("arial",12,"bold"),width=18)
        id_entry["value"] = ("Select class","Class1", "Class2","Class3")
        id_entry.current(0)
        id_entry.grid(row=1,column=1,sticky=W,padx=2,pady=7)


        #Credits
        lbl_id = Label(std_lbl_class_frame, font=("arial",12,"bold"),text="Credits: ", bg="white")
        lbl_id.grid(row=1, column=2,sticky=W,padx=2,pady=7)

        id_entry = ttk.Entry(std_lbl_class_frame,textvariable=self.var_creadits, font=("arial",12,"bold"),width=17)
        id_entry.grid(row=1,column=3,sticky=W,padx=2,pady=7)



        #Gender
        lbl_id = Label(std_lbl_class_frame, font=("arial",12,"bold"),text="Gender:", bg="white")
        lbl_id.grid(row=2, column=0,sticky=W,padx=2,pady=7)

        id_entry = ttk.Combobox(std_lbl_class_frame,textvariable=self.var_gender, font=("arial",12,"bold"),width=18)
        id_entry["value"] = ("Select gender","Male", "Female")
        id_entry.current(0)
        id_entry.grid(row=2,column=1,sticky=W,padx=2,pady=7)



         #DOB 
        lbl_id = Label(std_lbl_class_frame, font=("arial",12,"bold"),text="Date of birth:", bg="white")
        lbl_id.grid(row=2, column=2,sticky=W,padx=2,pady=7)

        id_entry = ttk.Entry(std_lbl_class_frame,textvariable=self.var_dob, font=("arial",12,"bold"),width=17)
        id_entry.grid(row=2,column=3,sticky=W,padx=2,pady=7)

         #Grade
        lbl_id = Label(std_lbl_class_frame, font=("arial",12,"bold"),text="Grade:", bg="white")
        lbl_id.grid(row=3, column=0,sticky=W,padx=2,pady=7)

        id_entry = ttk.Entry(std_lbl_class_frame,textvariable=self.var_grade, font=("arial",12,"bold"),width=20)
        id_entry.grid(row=3,column=1,sticky=W,padx=2,pady=7)

         #Email
        lbl_id = Label(std_lbl_class_frame, font=("arial",12,"bold"),text="Email:", bg="white")
        lbl_id.grid(row=3, column=2,sticky=W,padx=2,pady=7)

        id_entry = ttk.Entry(std_lbl_class_frame,textvariable=self.var_email, font=("arial",12,"bold"),width=17)
        id_entry.grid(row=3,column=3,sticky=W,padx=2,pady=7)

        #Button GPA toi da
        btn_Max = Button(std_lbl_class_frame,text="GPA Toi da",command=self.max_gpa,font=("arial",11,"bold"), width=17,bg="blue", fg="white")
        btn_Max.grid(row=4,column=0,padx=1)        

        #Button Frame

        btn_frame = Frame(DataLeft,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=470,width=650,height=38)

        btn_Add = Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"), width=17,bg="blue", fg="white")
        btn_Add.grid(row=0,column=0,padx=1)

        btn_update = Button(btn_frame,text="Update",command=self.update_data,font=("arial",11,"bold"), width=17,bg="blue", fg="white")
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete = Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",11,"bold"), width=17,bg="blue", fg="white")
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset = Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"), width=17,bg="blue", fg="white")
        btn_reset.grid(row=0,column=3,padx=1)


        #right frame 
        DataRight = LabelFrame(Mange_frame,bd=4, relief=RIDGE,padx=2, text="Danh sách sinh viên & Các chức năng", font=("times new roman",12,"bold"), fg = "red", bg="white")
        DataRight.place(x=680,y=10, width=800, height=540)

        #img1
        # img_6 = Image.open(r"college_images\uet3.jpg")
        # img_6 = img_6.resize((780,200), Image.ADAPTIVE)
        # self.photoimg_6 = ImageTk.PhotoImage(img_6)

        # my_img= Label(DataRight, image=self.photoimg_6,bd=2,relief=RIDGE)
        # my_img.place(x=0,y=0,width=790,height=200)
        
        #right frame 
        Search_Frame = LabelFrame(DataRight,bd=4, relief=RIDGE,padx=2, text="Các chức năng", font=("times new roman",12,"bold"), fg = "red", bg="white")
        Search_Frame.place(x=0,y=0, width=790, height=160)

        search_by = Label(Search_Frame, font=("times new roman",11,"bold"),text="Tìm kiếm theo: ", fg="red",bg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)


        #search
        self.var_com_search=StringVar()
        com_txt_search = ttk.Combobox(Search_Frame, state="readonly",textvariable=self.var_com_search,font=("arial",12,"bold"),width=12)
        com_txt_search['value'] = ("Select search","Name","DOB","StudentID")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W, padx=2)

        self.var_search = StringVar()
        txt_search = ttk.Entry(Search_Frame, textvariable=self.var_search,width=15,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2)

        btn_search = Button(Search_Frame,text="Search",command=self.search_data,font=("arial",11,"bold"),width=12,bg="blue",fg="white")
        btn_search.grid(row=0,column=3)

        btn_Showall = Button(Search_Frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),width=12,bg="blue",fg="white")
        btn_Showall.grid(row=2,column=2)

        btn_GpaStatistics = Button(Search_Frame,text="Statistic GPA",command=self.statistic_gpa,font=("arial",11,"bold"),width=12,bg="blue",fg="white")
        btn_GpaStatistics.grid(row=2,column=3)


        # Add sorting functionality
        sort_by = Label(Search_Frame, font=("times new roman", 11, "bold"), text="Sắp xếp theo: ", fg="red", bg="white")
        sort_by.grid(row=1, column=0, sticky=W, padx=5)

        self.var_sort_by = StringVar()
        com_txt_sort = ttk.Combobox(Search_Frame, state="readonly", textvariable=self.var_sort_by, font=("arial", 12, "bold"), width=18)
        com_txt_sort['value'] = ("Select sort", "Name", "DOB", "StudentID", "Grade")
        com_txt_sort.current(0)
        com_txt_sort.grid(row=1, column=1, sticky=W)

        btn_sort = Button(Search_Frame, text="Sort",command=self.sort_data, font=("arial", 11, "bold"), width=12, bg="blue", fg="white")
        btn_sort.grid(row=1, column=2, padx=5)

        #gpa
        btn_calculate_gpa = Button(Search_Frame, text="Calculate GPA & Scholarship", command=self.calculate_gpa_and_scholarship, font=("arial", 11, "bold"), width=25, bg="blue", fg="white")
        btn_calculate_gpa.grid(row=2, column=1, padx=5)

        #export data
        # Button to export data to Excel
        btn_export = Button(Search_Frame, text="Export data", command=self.export_to_excel, font=("arial", 11, "bold"), width=20, bg="blue", fg="white")
        btn_export.grid(row=2, column=0, padx=5)

        # Send email Scholarship
        btn_export = Button(Search_Frame, text="Send Email Scholarship", command=self.send_email, font=("arial", 11, "bold"), width=20, bg="green", fg="white")
        btn_export.grid(row=3, column=0, padx=5)

        # ========================Frame hien thi dach sach sinh vien================================ #

        table_frame = Frame(DataRight,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=170,width=790,height=340)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=("dep","id","name","div","Gender",'Email',"DOB","Grade","Average","Credits","SchoolarShip"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Major")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Class Div")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("DOB",text="Date of birth")
        self.student_table.heading("Grade",text="Grade")
        self.student_table.heading("Credits",text="Credits")
        self.student_table.heading("Average",text="GPA")
        
        self.student_table.heading("SchoolarShip",text="SchoolarShip")

        self.student_table["show"] = "headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Grade",width=100)
        self.student_table.column("Average",width=100)
        self.student_table.column("Credits",width=100)
        self.student_table.column("SchoolarShip",width=100)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #fecth
    def fetch_data(self):
        conn = mysql.connector.connect(host=host_name,user=user_name,password=password_key, database=database_name)
        my_cursur = conn.cursor()
        my_cursur.execute("SELECT * FROM student")
        data = my_cursur.fetchall()
        if (len(data) != 0):
            self.student_table.delete(*self.student_table.get_children())
            # for i in data:
            #     self.student_table.insert("",END,values=i)
            conn.commit()

        for row in data:
            gpa = row[-3]  # Assuming GPA is the second to last column in the student table
            if gpa is not None and gpa <= 2.3:
                self.student_table.insert("", "end", values=row, tags=("low_gpa",))
            else:
                self.student_table.insert("", "end", values=row)
        self.student_table.tag_configure("low_gpa", background="red")

        conn.close()


    def add_data(self):
        if (self.var_dep.get() == "" or self.var_std_id.get() == ""):
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host=host_name,user=user_name,password=password_key, database=database_name)
                my_cusur = conn.cursor()
                my_cusur.execute("Insert into student (Dep, StudentID, Name, Division, Gender,email,DOB,Grade,Credits) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_dob.get(),
                    self.var_grade.get(),
                    self.var_creadits.get() ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been added",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)



    def calculate_gpa_and_scholarship(self):
     try:
        conn = mysql.connector.connect(host=host_name, user=user_name, password=password_key, database=database_name)
        my_cusur = conn.cursor()

        # Lấy dữ liệu từ bảng Grade
        my_cusur.execute(" SELECT StudentID, Grade FROM student")
        data = my_cusur.fetchall()

        def convert_grade_to_gpa(average_grade):
                return average_grade*0.4
        low_gpa_students = []
        # Duyệt qua từng sinh viên
        for student in data:
            student_id = student[0]
            my_cusur.execute("SELECT Grade FROM student WHERE StudentID = %s", (student_id,))
            grades = my_cusur.fetchall()
            total_grades = sum([grade[0] for grade in grades])
            if len(grades) > 0:
                average_grade = total_grades / len(grades)
            else:
                average_grade = 0
            gpa = convert_grade_to_gpa(average_grade)

            scholarship = "Yes" if gpa >= 3.6 else "No"
            my_cusur.execute("UPDATE student SET gpa=%s, scholarship=%s WHERE StudentID=%s", (gpa, scholarship, student_id))

            if gpa <= 2.3:
                low_gpa_students.append(student_id)           
        
        conn.commit()
        conn.close()

        if low_gpa_students:
            messagebox.showwarning("Low GPA Warning", f"Students with low GPA (<= 2.3): {', '.join(low_gpa_students)}", parent=self.root)

        messagebox.showinfo("Success", "GPA and Scholarship status updated", parent=self.root)
        self.fetch_data()
     except Exception as es:
        messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    #export data
    def export_to_excel(self):
        try:
            conn = mysql.connector.connect(host=host_name, user=user_name, password=password_key, database=database_name)
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            data = my_cursor.fetchall()
            conn.close()

            # Convert data to pandas DataFrame
            columns = ["Major", "StudentID", "Name", "Division", "Gender","Email","DOB", "Grade", "GPA","Credits","Scholarship"]
            df = pd.DataFrame(data, columns=columns)

            # Ask user where to save the file
            file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
            if file_path:
                df.to_excel(file_path, index=False)
                messagebox.showinfo("Success", f"Data exported successfully to {file_path}", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
        
    #sort 
    def sort_data(self):
        sort_option = self.var_sort_by.get()
        if sort_option == "None":
            self.fetch_data()
            return

        sort_column = {
            "Name": "name",
            "StudentID": "StudentID",
            "DOB":"DOB",
            "Grade": "Grade"
        }.get(sort_option, "name")

        try:
            conn = mysql.connector.connect(host=host_name, user=user_name, password=password_key, database=database_name)
            my_cursur = conn.cursor()
            my_cursur.execute(f"SELECT * FROM student ORDER BY {sort_column}")
            data = my_cursur.fetchall()
            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    #get cursor
    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_std_id.set(data[1])
        self.var_std_name.set(data[2])
        self.var_div.set(data[3])
        self.var_gender.set(data[4])
        self.var_email.set(data[5])
        self.var_dob.set(data[6])
        self.var_grade.set(data[7])
        self.var_avr.set(data[8])
        self.var_creadits.set(data[9])
        self.var_scholarship.set(data[10])
    
    def update_data(self):
        if (self.var_dep.get() == "" or self.var_std_id.get() == ""):
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                update = messagebox.askyesno("Update","Are you sure update this student's data", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host=host_name,user=user_name,password=password_key, database=database_name)
                    my_cusur = conn.cursor()
                    my_cusur.execute("update student set Dep=%s,Name=%s,Division=%s,Gender=%s,email=%s,DOB=%s, Grade=%s,Credits=%s where StudentID=%s",(
                        self.var_dep.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_dob.get(),
                        self.var_grade.get(),
                        self.var_creadits.get(),
                        self.var_std_id.get()))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been updated",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #delete
    def delete_data(self):
        if (self.var_std_id.get() == "" ):
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                Delete = messagebox.askyesno("Delete","Are you want to delete this student")
                if Delete > 0:
                    conn = mysql.connector.connect(host=host_name,user=user_name,password=password_key, database=database_name)
                    my_cursur = conn.cursor()
                    sql = "delete FROM student where StudentID =%s"
                    value=(self.var_std_id.get(),)
                    my_cursur.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Your data is deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #reset
    def reset_data(self):
        self.var_dep.set("Select Major")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_gender.set("")
        self.var_email.set("")
        self.var_dob.set("")
        self.var_grade.set("")
        self.var_creadits.set("")

    #search
    def search_data(self):
        if self.var_com_search.get() == "" or self.var_search.get()=="":
            messagebox.showerror("Error", "Select options")
        else:
            try:
                conn = mysql.connector.connect(host=host_name,user=user_name,password=password_key, database=database_name)
                my_cusur = conn.cursor()
                my_cusur.execute("select * FROM student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data = my_cusur.fetchall()
                if (len(data) != 0):
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    def max_gpa(self):
        grade = float(self.var_grade.get())
        credits = int(self.var_creadits.get())
        def convert_grade_to_gpa(average_grade):
            return average_grade*0.4
        gpa = convert_grade_to_gpa(grade)

        gpa_max = ((gpa*credits + 4*(141-credits) ))/141


        messagebox.showinfo("Success", f"GPA toi da la: {float(gpa_max)}", parent=self.root)

        if(gpa_max>=3.6):
            messagebox.showinfo("Success","Sinh vien nay co the dat bang xuat sac", parent=self.root)
        elif(gpa_max >= 3.2 and gpa_max <=3.6):
            messagebox.showinfo("Success","Sinh vien nay co the dat bang gioi", parent=self.root)
        elif (gpa_max >= 2.5 and gpa_max <= 3.2):
            messagebox.showinfo("Success","Sinh vien nay co the dat bang kha", parent=self.root)
        else:
            messagebox.showinfo("Success","Sinh vien nay co the dat bang trung binh", parent=self.root)

    def statistic_gpa(self):
        divisions = ["0-0.4  ","0.4-0.8  ","0.8-1.2  ","1.2-1.6","1.6-2.0", "2.0-2.4", "2.4-2.8", "2.8-3.2", "3.2 2-3.6", "3.6-4.0"]

        conn = mysql.connector.connect(host=host_name,user=user_name,password=password_key, database=database_name)
        my_cursur = conn.cursor()
        my_cursur.execute("SELECT * FROM student")
        data = my_cursur.fetchall()

        count0 = 0
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        count6 = 0
        count7 = 0
        count8 = 0
        count9 = 0

        if (len(data) != 0):
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()

        for row in data:
            gpa = row[-3]  # Assuming GPA is the second to last column in the student table
            if gpa < 0.4:
                count0 += 1
            elif (gpa >= 0.4 and gpa < 0.8):
                count1 += 1
            elif (gpa >= 0.8 and gpa < 1.2):
                count2 += 1
            elif (gpa >= 1.2 and gpa < 1.6):
                count3 += 1
            elif (gpa >= 1.6 and gpa < 2.0):
                count4 += 1
            elif (gpa >= 2.0 and gpa < 2.4):
                count5 += 1
            elif (gpa >= 2.4 and gpa < 2.8):
                count6 += 1
            elif (gpa >= 2.8 and gpa < 3.2):
                count7 += 1
            elif (gpa >= 3.2 and gpa < 3.6):
                count8 += 1
            elif (gpa >= 3.6 and gpa <= 4.0):
                count9 += 1
        conn.close()

        listGPA = [count0,count1, count2, count3, count4, count5, count6, count7, count8, count9]
        plt.bar(divisions,listGPA, color='green', width=0.5)
        plt.title("Thong ke GPA cua sinh vien")
        plt.xlabel("Cac khoang GPA")
        plt.ylabel("So luong sinh vien")
        plt.show()
    
    def send_email(self):
        conn = mysql.connector.connect(host=host_name,user=user_name,password=password_key, database=database_name)
        my_cursur = conn.cursor()
        my_cursur.execute("SELECT * FROM student")
        data = my_cursur.fetchall()
        email=email_account
        password=app_password
        email_sent=[]
        #xuly
        session=smtplib.SMTP('smtp.gmail.com',587)
        session.starttls() #enable security
        session.login(email,password)
        #noidung
        mail_content='''Subject: Thông báo về học bổng

        Kính gửi em,

        Sau nhiều đắn đo suy nghĩ, Đại học Công Nghệ hàng đầu xin trân trọng thông báo rằng: Chúc mừng em đã nhận được học bổng kỳ này!!
        Keep trying! 
        
        Thân mến,
        Phòng đào tạo.
        '''

        mail_content_encoded = mail_content.encode()

        for row in data:
            schoolarship = row[-1]
            if schoolarship == "Yes":
                r = row[5]
                print (row[5])
                email_sent.append(r);

        for _ in range(len(email_sent)):
            session.sendmail(email,email_sent[_],mail_content_encoded)
            print('Your mail has been sent!')
        
        if(len(email_sent)==0):
            messagebox.showinfo("Thong bao","Khong co sinh vao duoc hoc bong",parent = self.root)
        else:
            messagebox.showinfo("Success","Email duoc gui di thanh cong",parent = self.root)
        conn.close()