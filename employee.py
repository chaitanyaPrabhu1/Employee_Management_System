from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import mysql.connector
from tkinter import messagebox

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1536x864+0+0")
        self.root.title("Employee Management System")

        '''Variables'''
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designition=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_country=StringVar()
        self.var_phone=StringVar()
        self.var_salary=StringVar()
        self.var_location=StringVar()



        '''Making Title'''
        lbl_title=Label(self.root, text = "Employee Management System", font = ("times new roaman", 37, "bold"), fg = "darkblue", bg = "white")
        lbl_title.place(x=0, y=0, width=1536, height=73)

        '''Inserting employee logo'''
        img_logo=Image.open('image/emplogo.jpg')
        img_logo=img_logo.resize((73, 73), Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=150, y=0, width= 73, height = 73)

        '''Placing the frame in GUI'''
        img_frame=Frame(self.root, bd=2, relief = RIDGE, bg='white')
        img_frame.place(x=0, y=73, width=1536, height=160)

        '''Inserting Image in Frame~1st-Iamage'''
        img1=Image.open('image/emp5.jpg')
        img1=img1.resize((1536, 160), Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=1536, height = 160)

        '''Designing Main Frame'''
        Main_frame=Frame(self.root, bd=2, relief = RIDGE, bg='white')
        Main_frame.place(x=10, y=240, width=1514, height=610)

        '''Upper Frame'''
        upper_frame=LabelFrame(Main_frame, bd=2, relief = RIDGE,text='Employee Information', font = ("times new roaman", 11, "bold"), fg = "red", bg = "white")
        upper_frame.place(x=10, y=1, width=1490, height=288)

        '''Labels'''
        lbl_dep = Label(upper_frame, text='Department', font = ("arial", 12, "bold"), fg = "black", bg = "white")
        lbl_dep.grid(row=0, column=0,padx=2,sticky=W)
        
        combo_dep=ttk.Combobox(upper_frame, textvariable=self.var_dep, font = ("arial", 12, "bold"), width=17, state='readonly')
        combo_dep['value']=('Select Department', 'HR', 'Software Engineer', 'Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        '''Name'''
        lbl_name = Label(upper_frame, font = ("arial", 12, "bold"), text="Name:", bg = "white")
        lbl_name.grid(row=0, column=2,padx=2, pady=7, sticky=W)
        
        txt_Name=ttk.Entry(upper_frame, textvariable=self.var_name, width=22, font=("arial", 11, "bold"))
        txt_Name.grid(row=0, column=3, padx=2, pady=7)

        '''lbl-Designition'''
        lbl_Designition = Label(upper_frame, font = ("arial", 12, "bold"), text="Designition:", bg = "white")
        lbl_Designition.grid(row=1, column=0,padx=2, pady=7, sticky=W)
        
        txt_Designition=ttk.Entry(upper_frame, textvariable=self.var_designition, width=22, font=("arial", 11, "bold"))
        txt_Designition.grid(row=1, column=1, padx=2, sticky=W, pady=7)

        '''Email'''
        lbl_email = Label(upper_frame, font = ("arial", 12, "bold"), text="Email:", bg = "white")
        lbl_email.grid(row=1, column=2,padx=2, pady=7, sticky=W)
        
        txt_email=ttk.Entry(upper_frame, textvariable=self.var_email, width=22, font=("arial", 11, "bold"))
        txt_email.grid(row=1, column=3, padx=2, pady=7)

        '''Address'''
        lbl_address = Label(upper_frame, font = ("arial", 12, "bold"), text="Address:", bg = "white")
        lbl_address.grid(row=2, column=0,padx=2, pady=7, sticky=W)
        
        txt_address=ttk.Entry(upper_frame, textvariable=self.var_address, width=22, font=("arial", 11, "bold"))
        txt_address.grid(row=2, column=1, padx=2, pady=7)

        '''Married'''
        lbl_married = Label(upper_frame, text='Married Status:', font = ("arial", 12, "bold"), fg = "black", bg = "white")
        lbl_married.grid(row=2, column=2,padx=2, pady=7, sticky=W)
        
        combo_txt_married=ttk.Combobox(upper_frame, textvariable=self.var_married, font = ("arial", 12, "bold"), width=18, state='readonly')
        combo_txt_married['value']=('Married', 'Unmarried')
        combo_txt_married.current(0)
        combo_txt_married.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        '''D.O.B'''
        lbl_dob = Label(upper_frame, font = ("arial", 12, "bold"), text="DOB:", bg = "white")
        lbl_dob.grid(row=3, column=0,padx=2, pady=7, sticky=W)
        
        txt_dob=ttk.Entry(upper_frame, textvariable=self.var_dob, width=22, font=("arial", 11, "bold"))
        txt_dob.grid(row=3, column=1, padx=2, pady=7)

        '''D.O.J'''
        lbl_doj = Label(upper_frame, font = ("arial", 12, "bold"), text="DOJ:", bg = "white")
        lbl_doj.grid(row=3, column=2,padx=2, pady=7, sticky=W)
        
        txt_doj=ttk.Entry(upper_frame, textvariable=self.var_doj, width=22, font=("arial", 11, "bold"))
        txt_doj.grid(row=3, column=3, padx=2, pady=7)

        '''ID Proof'''
        
        combo_txt_proof=ttk.Combobox(upper_frame, textvariable=self.var_idproofcomb, font = ("arial", 12, "bold"), width=18, state='readonly')
        combo_txt_proof['value']=('ID TYPE', 'PAN CARD', 'AADHAR CARD', 'DRIVING LISENCE', "VOTER ID")
        combo_txt_proof.current(0)
        combo_txt_proof.grid(row=4, column=0, padx=2, pady=10, sticky=W)

        txt_proof=ttk.Entry(upper_frame, textvariable=self.var_idproof, width=22, font=("arial", 12, "bold"), background="black")
        txt_proof.grid(row=4, column=1,padx=2,pady=7)

        '''Gender'''
        lbl_proof = Label(upper_frame, text='Gender:', font = ("arial", 12, "bold"), fg = "black", bg = "white")
        lbl_proof.grid(row=4, column=2,padx=2, pady=7, sticky=W)
        
        combo_txt_proof=ttk.Combobox(upper_frame, textvariable=self.var_gender, font = ("arial", 12, "bold"), width=18, state='readonly')
        combo_txt_proof['value']=('Gender', 'Male', 'Female', 'Defective')
        combo_txt_proof.current(0)
        combo_txt_proof.grid(row=4, column=3, padx=2, pady=10, sticky=W)

        '''Country'''
        lbl_country = Label(upper_frame, text='Country:', font = ("arial", 12, "bold"), fg = "black", bg = "white")
        lbl_country.grid(row=0, column=4,padx=2, pady=7, sticky=W)
        
        combo_txt_country=ttk.Combobox(upper_frame, textvariable=self.var_country, font = ("arial", 12, "bold"), width=18, state='readonly')
        combo_txt_country['value']=('Country', 'India')
        combo_txt_country.current(0)
        combo_txt_country.grid(row=0, column=5, padx=2, pady=10, sticky=W)

        '''Phone Number'''
        lbl_number = Label(upper_frame, font = ("arial", 12, "bold"), text="Phone No:", bg = "white")
        lbl_number.grid(row=1, column=4,padx=2, pady=7, sticky=W)
        
        txt_number=ttk.Entry(upper_frame, textvariable=self.var_phone, width=22, font=("arial", 11, "bold"))
        txt_number.grid(row=1, column=5, padx=2, pady=7)

        '''CTC'''
        lbl_ctc = Label(upper_frame, font = ("arial", 12, "bold"), text="CTC:", bg = "white")
        lbl_ctc.grid(row=2, column=4,padx=2, pady=7, sticky=W)
        
        txt_ctc=ttk.Entry(upper_frame, textvariable=self.var_salary, width=22, font=("arial", 11, "bold"))
        txt_ctc.grid(row=2, column=5, padx=2, pady=7)

        '''Location'''
        lbl_location = Label(upper_frame, font = ("arial", 12, "bold"), text="Location:", bg = "white")
        lbl_location.grid(row=3, column=4,padx=2, pady=7, sticky=W)
        
        txt_location=ttk.Entry(upper_frame, textvariable=self.var_location, width=22, font=("arial", 11, "bold"))
        txt_location.grid(row=3, column=5, padx=2, pady=7)

        

        '''Button Frame'''
        Button_frame=Frame(upper_frame, bd=2, relief = RIDGE, bg='white')
        Button_frame.place(x=1295, y=10, width=189, height=220)

        '''Button 1'''
        btn_add=Button(Button_frame, text="Save",command=self.add_data, font=("arial", 13, "bold"), width=13, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=0, pady=4)

        '''Button 2'''
        btn_update=Button(Button_frame,command=self.update_data, text="Update", font=("arial", 13, "bold"), width=13, bg='blue', fg='white')
        btn_update.grid(row=1, column=0, padx=0, pady=10)

        '''Button 3'''
        btn_delete=Button(Button_frame,command=self.delete_data, text="Delete", font=("arial", 13, "bold"), width=13, bg='blue', fg='white')
        btn_delete.grid(row=2, column=0, padx=0, pady=10)

        '''Button 4'''
        btn_clear=Button(Button_frame, command=self.reset_data, text="Clear", font=("arial", 13, "bold"), width=13, bg='blue', fg='white')
        btn_clear.grid(row=3, column=0, padx=0, pady=10)

        '''Lower Frame'''
        down_frame=LabelFrame(Main_frame, bd=2, relief = RIDGE,text='Employee Information Table', font = ("times new roaman", 11, "bold"), fg = "red", bg = "white")
        down_frame.place(x=10, y=290, width=1490, height=305)

        '''Search Frame'''
        search_frame=LabelFrame(down_frame, bd=2, relief = RIDGE,text='Search Employee Information', font = ("times new roaman", 11, "bold"), fg = "red", bg = "white")
        search_frame.place(x=0, y=0, width=1486, height=70)

        search_by=Label(search_frame,font=("arial",11,"bold"), text="Search By:",fg="white", bg="red")
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        '''Search'''

        
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame, textvariable=self.var_com_search,state="readonly",font=("arial", 12, 'bold'), width=18)    
        com_txt_search['value']=('Select Option', 'Phone', 'ID Proof')
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, padx=5, sticky=W)

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search, width=22, font=("arial", 11, "bold"))
        txt_search.grid(row=0, column=2,padx=5)

        btn_search=Button(search_frame, command=self.search_data,text="Search", font=("arial", 11, "bold"), width=14, background="blue", fg="white")
        btn_search.grid(row=0, column=3,padx=5)

        btn_ShowAll=Button(search_frame, command=self.fetch_data, text="Show All",font=("times new roman", 11, "bold"),fg="white", bg="blue")
        btn_ShowAll.grid(row=0, column=4, padx=5)

        '''Text'''
        stayhome=Label(search_frame, text="Wear a mask", font=("times new roaman", 20, "bold"), fg="black", bg="white")
        stayhome.place(x=1035, y=0, width=300, height=30)

        '''================================================================Employee-Table=============================================================='''

        '''Designing Table Frame'''
        table_frame=Frame(down_frame, bd=3, relief = RIDGE)
        table_frame.place(x=1, y=60, width=1485, height=200)

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame, columns=('dep','name','degi', 'email', 'address', 'married', 'dob', 'doj', 'idproofcomb', 'idproof', 'gender', 'country', 'phone', 'ctc', 'location'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep', text='Department')
        self.employee_table.heading('name', text='Name')
        self.employee_table.heading('degi', text='Designation')
        self.employee_table.heading('email', text='Email')
        self.employee_table.heading('address', text='Address')
        self.employee_table.heading('married', text='Married Status')
        self.employee_table.heading('dob', text='DOB')
        self.employee_table.heading('doj', text='DOJ')
        self.employee_table.heading('idproofcomb', text='ID Type')
        self.employee_table.heading('idproof', text='ID Proof')
        self.employee_table.heading('gender', text='Gender')
        self.employee_table.heading('country', text='Country')
        self.employee_table.heading('phone', text='Phone No')
        self.employee_table.heading('ctc', text='CTC')
        self.employee_table.heading('location', text='Location')

        self.employee_table['show']='headings'
        self.employee_table.column('dep',width=150)

        self.employee_table.pack(fill=BOTH, expand=1)

        self.employee_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()


    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error", 'All Fields are required.')
        else:
            try:
                conn= mysql.connector.connect(host='localhost', username='chaitanya',password='1173191', database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)',(

        self.var_dep.get(),
        self.var_name.get(),
        self.var_designition.get(),
        self.var_email.get(),
        self.var_address.get(),
        self.var_married.get(),
        self.var_dob.get(),
        self.var_doj.get(),
        self.var_idproofcomb.get(),
        self.var_idproof.get(),
        self.var_gender.get(),
        self.var_country.get(),
        self.var_phone.get(),
        self.var_salary.get(),
        self.var_location.get()   ))
    
    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Employee has beeen added', parent=self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due to:{str(es)}', parent=self.root)
    #Fatch Data
    def fetch_data(self):
        conn= mysql.connector.connect(host='localhost', username='chaitanya',password='1173191', database='mydata')
        my_cursor=conn.cursor() 
        my_cursor.execute('select * from employee1')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("", END, value=i)
            
            conn.commit()
        conn.close()

    #Get Cursor

    def get_cursor(self, event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designition.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_country.set(data[11])
        self.var_phone.set(data[12])
        self.var_salary.set(data[13])
        self.var_location.set(data[14])

    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error", 'All Fields are required.')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure')
                if update>0:
                    conn= mysql.connector.connect(host='localhost', username='chaitanya',password='1173191', database='mydata')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update employee1 set Department=%s,Name=%s,Designition=%s,Email=%s,Address=%s,Married Status=%s,DOB=%s,DOJ=%s,ID_PROOF_COMBO=%s,Gender=%s,Country=%s,Phone=%s,Salary=%s,Location=%s, where ID_PROOF=%s', (

                                                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                                                                                        self.var_designition.get(),
                                                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                                                        self.var_married.get(),
                                                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                                                        self.var_doj.get(),
                                                                                                                                                                                                                                                        self.var_idproofcomb.get(),
                                                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                                                        self.var_country.get(),
                                                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                                                        self.var_salary.get(),
                                                                                                                                                                                                                                                        self.var_location.get(),
                                                                                                                                                                                                                                                        self.var_idproof.get()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                   
                
                
                                                                                                                                                                                                                                                                                       ))
                else:
                    if not update:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Employee successfully updated', parent=self.root)

            except Exception as es:
                messagebox.showerror('Error', f'Due to:{str(es)}', parent=self.root)



    #Delete
    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror('Error', "All fields are required")
        else:
            try:
                Delete=messagebox.askyesno('Delete', 'Are you sure to delete this?',parent=self.root)
                if Delete>0:
                    conn= mysql.connector.connect(host='localhost', username='chaitanya',password='1173191', database='mydata')
                    my_cursor=conn.cursor()
                    sql='delete from employee1 where id_proof=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete', 'Employee successfully deleted', parent=self.root)

            except Exception as es:
                messagebox.showerror('Error', f'Due to:{str(es)}', parent=self.root)

    #Reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_designition.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_country.set("")
        self.var_phone.set("")
        self.var_salary.set("")
        self.var_location.set("")

    #search
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error', 'Please select option')
        else:
            try:
                conn= mysql.connector.connect(host='localhost', username='chaitanya',password='1173191', database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from employee1 where ' + str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("", END, values=i)

                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due to:{str(es)}', parent=self.root)










if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()