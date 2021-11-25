from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
# create class student
class Student:
    # create constructor
    def __init__(self, root):
       self.root = root
       self.root.title("Student Management System")
       self.root.geometry("1350x700+0+0")

       # all variables
       self.id_var = StringVar()
       self.name_var = StringVar()
       self.gender_var=StringVar()
       self.dept_name_var=StringVar()
       self.session_var=StringVar()
       self.gmail_var = StringVar()
       self.contact_var = StringVar()
       self.search_by = StringVar()
       self.search_txt = StringVar()


       title = Label(self.root, text="Student Management System",bd=10,relief=GROOVE, font=("times new roman", 40, "bold"), bg="lightgreen", fg='red')
       title.pack(side=TOP, fill=X)
       # --------------manage frame------------------
       manage_frame = Frame(self.root, bd=3, relief=RIDGE, bg="lightyellow")
       manage_frame.place(x=15, y=100, width=450, height=600)
       
       m_title=Label(manage_frame, text="Manage Students", font=("times new roman", 30, "bold"), bg="gray",fg='white')
       m_title.grid(row=0, columnspan=2, pady=15)

       lbl_id = Label(manage_frame, text="ID", font=("times new roman", 15, "bold"), bg="lightyellow")
       lbl_id.grid(row=1, column=0, pady=10, padx=20, sticky="w")

       txt_id = Entry(manage_frame,textvariable=self.id_var, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_id.grid(row=1, column=1, pady=10, padx=20, sticky="w")

       lable_name = Label(manage_frame, text="Name", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

       txt_name = Entry(manage_frame,textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

       lable_gender = Label(manage_frame, text="Gender", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_gender.grid(row=3, column=0, pady=10, padx=20, sticky="w")
       # gender combobox
       combo_gender= ttk.Combobox(manage_frame,textvariable=self.gender_var, font=("times new roman", 13, "bold"),state='readonly')
       combo_gender['values']=('Male', 'Female', 'Other')
       combo_gender.grid(row=3, column=1, pady=10, padx=20, sticky="w")

       lable_dept = Label(manage_frame, text="Dept. Name", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_dept.grid(row=4, column=0, pady=10, padx=15, sticky="w")

       txt_dept = Entry(manage_frame, textvariable=self.dept_name_var,font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_dept.grid(row=4, column=1, pady=10, padx=20, sticky="w")

       lable_session = Label(manage_frame, text="Session", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_session.grid(row=5, column=0, pady=10, padx=15, sticky="w")

       txt_session = Entry(manage_frame,textvariable=self.session_var, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_session.grid(row=5, column=1, pady=10, padx=20, sticky="w")

       lable_gmail = Label(manage_frame, text="Gmail", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_gmail.grid(row=6, column=0, pady=10, padx=20, sticky="w")

       txt_gmail = Entry(manage_frame, textvariable=self.gmail_var, font=("times new roman", 15, "bold"),bd=4, relief=GROOVE)
       txt_gmail.grid(row=6, column=1, pady=10, padx=20, sticky="w")

       lable_contact = Label(manage_frame, text="Contact No.", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_contact.grid(row=7, column=0, pady=10, padx=20, sticky="w")

       txt_contact = Entry(manage_frame,textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_contact.grid(row=7, column=1, pady=10, padx=20, sticky="w")

       lable_address = Label(manage_frame, text="Address", font=("times new roman", 15, "bold"), bg="lightyellow")
       lable_address.grid(row=8, column=0, pady=10, padx=20, sticky="w")

       self.txt_address = Text(manage_frame, width=20,height=2, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       self.txt_address.grid(row=8, column=1, pady=10, padx=20, sticky="w")

       # --------------button frame------------------
       button_frame = Frame(manage_frame, bd=4, relief=RIDGE, bg="crimson")
       button_frame.place(x=10, y=525, width=420)

       Addbtn=Button(button_frame, text=" Add ",command=self.add_student, font=("times new roman", 15, "bold"), bg="green", fg="white").grid(row=0, column=0, padx=15, pady=10)
       Updatebtn=Button(button_frame, text="Update", command=self.update_data, font=("times new roman", 15, "bold"), bg="#ff00ff", fg="white").grid(row=0, column=1, padx=15, pady=10)
       Deletebtn=Button(button_frame, text="Delete", command=self.delete_data, font=("times new roman", 15, "bold"), bg="#116548", fg="white").grid(row=0, column=2, padx=15, pady=10)
       Clearbtn=Button(button_frame, text="Clear", command=self.clear, font=("times new roman", 15, "bold"), bg="red", fg="white").grid(row=0, column=3, padx=15, pady=10)



       ## --------------details frame------------------
       detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="gray")
       detail_frame.place(x=500, y=100, width=840, height=490)


       lblSearch = Label(detail_frame, text="Search By", font=("times new roman", 15, "bold"), bg="gray")
       lblSearch.grid(row=0, column=0, pady=10, padx=20, sticky="w")
       # search combobox
       combo_search= ttk.Combobox(detail_frame,textvariable=self.search_by, width=10,font=("times new roman", 13, "bold"),state='readonly')
       combo_search['values']=("ID", "Name", "Dept_Name", "Session","Contact")
       combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

       txt_search = Entry(detail_frame,textvariable=self.search_txt, width=15, font=("times new roman", 15, "bold"), bd=4, relief=GROOVE)
       txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

       searchbtn=Button(detail_frame,command=self.search_data, text="Search",width=10, font=("times new roman", 15, "bold"), bg="green", fg="white").grid(row=0, column=3, padx=15, pady=10)
       showallbtn=Button(detail_frame, text="Show All",command=self.fetch_data, width=10,font=("times new roman", 15, "bold"), bg="green", fg="white").grid(row=0, column=4, padx=15, pady=10)
     
        # --------------details frame table------------------
        # -----table frame
       table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="crimson")
       table_frame.place(x=10, y=70, width=810, height=400)
        #----details developer
       dev_section = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
       dev_section.place(x=500, y=595, width=840, height=100)
       # developer frame
       detail_dev = Frame(self.root, bd=4, relief=RIDGE, bg="gray")
       detail_dev.place(x=503, y=600, width=350, height=90)
       lbl_author = Label(detail_dev, text="Developed By", font=("Helvetica",30, "bold"), fg="red",bg='gray')
       lbl_author.grid(row=0, column=0, pady=10, padx=20, sticky="w")

       detail_author= Frame(self.root, bd=4, relief=RIDGE, bg="gray")
       detail_author.place(x=860, y=600, width=470, height=90)
       lbl_author = Label(detail_author, text="Md. Rasel Meya\nDepartment of CSTE\nNoakhali Science & Technology University.", font=("times new roman", 15, "bold"),bg="gray")
       lbl_author.grid(row=0, column=1, pady=10, padx=20, sticky="w")
       lbl_author.pack()


       #---student table
       scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
       scroll_y = Scrollbar(table_frame, orient=VERTICAL)
       self.student_table = ttk.Treeview(table_frame, columns=("ID", "Name", "Gender","Dept_Name", "Session", "Gmail", "Contact No.", "Address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
       scroll_x.pack(side=BOTTOM, fill=X)
       scroll_y.pack(side=RIGHT, fill=Y)
       scroll_x.config(command=self.student_table.xview)
       scroll_y.config(command=self.student_table.yview)
       self.student_table.heading("ID", text="ID")
       self.student_table.heading("Name", text="Name")
       self.student_table.heading("Gender",text="Gender")
       self.student_table.heading("Dept_Name", text="Dept_Name")
       self.student_table.heading("Session", text="Session")
       self.student_table.heading("Gmail", text="Gmail")
       self.student_table.heading("Contact No.", text="Contact No.")
       self.student_table.heading("Address", text="Address")
       self.student_table.column("ID", width=100)
       self.student_table.column("Name", width=100)
       self.student_table.column("Gender", width=100)
       self.student_table.column("Dept_Name", width=100)
       self.student_table.column("Session", width=100)
       self.student_table.column("Gmail", width=100)
       self.student_table.column("Contact No.", width=100)
       self.student_table.column("Address", width=100)
       self.student_table['show']='headings'
       self.student_table.pack(fill=BOTH, expand=1)
       self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
       self.fetch_data() 
    def add_student(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="student_management_system")
        cur=con.cursor()
        cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.id_var.get(),self.name_var.get(),self.gender_var.get(),self.dept_name_var.get(),self.session_var.get(),self.gmail_var.get(),self.contact_var.get(), self.txt_address.get("1.0", END)))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    def fetch_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="student_management_system")
        cur=con.cursor()
        cur.execute("select * from student")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
                con.commit()
        
        con.close()
    def clear(self):
        self.id_var.set("")
        self.name_var.set("")
        self.gender_var.set("")
        self.dept_name_var.set("")
        self.session_var.set("")
        self.gmail_var.set("")
        self.contact_var.set("")
        self.txt_address.delete("1.0", END)
    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.gender_var.set(row[2])
        self.dept_name_var.set(row[3])
        self.session_var.set(row[4])
        self.gmail_var.set(row[5])
        self.contact_var.set(row[6])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[7])

    #------------------update student details------------------
    def update_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="student_management_system")
        cur=con.cursor()
        cur.execute("update student set Name=%s,Gender=%s,Dept_Name=%s,Session=%s,Gmail=%s,Contact=%s,Address=%s where ID=%s",(self.name_var.get(),
                                                                                                                            self.gender_var.get(),
                                                                                                                            self.dept_name_var.get(),
                                                                                                                            self.session_var.get(),
                                                                                                                            self.gmail_var.get(),
                                                                                                                            self.contact_var.get(),
                                                                                                                            self.txt_address.get("1.0", END),
                                                                                                                            self.id_var.get()
                                                                                                                            ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


    #------------------delete student details------------------
    def delete_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="student_management_system")
        cur=con.cursor()
        cur.execute("delete from student where ID=%s",self.id_var.get())
        # confirmation messagebox
        ask_del=messagebox.askyesno("Student Management System","Do you want to delete this record?")
        if ask_del>0:
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
        else:
            return


    #-----search_box-------------
    def search_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="student_management_system")
        cur=con.cursor()
        cur.execute("select * from student where "+self.search_by.get()+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
                con.commit()
        else:
            messagebox.showerror("Student Management System","No Data Found")

        con.close()



root = Tk()
obj = Student(root)
root.mainloop()

