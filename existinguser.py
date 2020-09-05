# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 15:04:26 2020

@author: Parnisha
"""


# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 16:12:43 2020

@author: Parnisha
"""
from tkinter.ttk import *
from tkinter import *
import mysql.connector
from tkinter import messagebox
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="poulami@2",
    database="candidate"
)
mycursor=mydb.cursor()
root=Tk()
root.configure(bg="#16ABB8")
root.geometry("900x600+30+30")
root.title("WELCOME TO YOUR PROFILE")
root.resizable(False,False)
Label(root,text="HEY! THERE",fg="#0A0B52",bg="#16ABB8",font=("Arial Bold",35)).grid(row=0,column=3,pady=10)

Label(root,text="YOUR PROFILE",fg="#141791",bg="#16ABB8",font=("Goudy old style",15)).grid(row=1,column=3,pady=10)
Label(root,text="Thank you for visiting",fg="#0A0B52",bg="#16ABB8",font=("Arial Bold",15)).grid(row=7,column=3)
def Show():
    class B:
        def __init__(self,root):
            self.root=root
            self.root.title("REGISTRATION FORM VIEW")
            self.root.geometry("1199x600+60+20")
            self.root.configure(bg="light green")
            self.root.resizable(False,False)
            Label(root,text="REGISTRATION FORM",fg="NAVY BLUE",bg="light green",font=("Arial Bold",19)).grid(row=0,column=1,pady=10)
            Label(root,text="CANDIDATEID",fg="black",bg="light green",font=("Bold",10)).grid(row=1,column=0)
            e1= Entry(root)
            e1.grid(row= 1, column=1,ipadx=80,pady=10)
            Label(root,text="FIRST_NAME",fg="black",bg="light green",font=("Bold",10)).grid(row=2,column=0)
            e2= Entry(root)
            e2.grid(row= 2, column=1,ipadx=80,pady=10)
            Label(root,text="LAST_NAME",fg="black",bg="light green",font=("Bold",10)).grid(row=3,column=0)
            e3= Entry(root)
            e3.grid(row= 3, column=1,ipadx=80,pady=10)
            Label(root,text="ADDRESS",fg="black",bg="light green",font=("Bold",10)).grid(row=4,column=0)
            e4 = Entry(root)
            e4.grid(row = 4, column=1,ipadx=80,pady=10)
            Label(root,text="AADHAR_NUMBER",fg="black",bg="light green",font=("Bold",10)).grid(row=5,column=0)
            e5 = Entry(root)
            e5.grid(row=5 ,column=1,ipadx=80,pady=10)
            Label(root,text="PASSWORD",fg="black",bg="light green",font=("Bold",10)).grid(row=6,column=0)
            e6 = Entry(root)
            e6.grid(row=6,column=1,ipadx=80,pady=10)
            Label(root,text="GENDER",fg="black",bg="light green",font=("Bold",10)).grid(row=7,column=0,pady=10)
            v =Entry(root)
            v.grid(row=7,column=1,pady=10,ipadx=80)
            Label(root,text="QUALIFICATION",fg="black",bg="light green",font=("Bold",10)).grid(row=8,column=0,pady=15)
            e7 = Entry(root)
            e7.grid(row=8,column=1,pady=10,padx=30,ipadx=80)
            Label(root,text="SKILLS",fg="black",bg="light green",font=("Bold",10)).grid(row=9,column=0,pady=15)
            e8 = Entry(root)
            e8.grid(row=9, column=1,pady=10,ipadx=80)
            Label(root,text="WRITE_SOMETHING_ABOUT_YOURSELF",fg="black",bg="light green",font=("Bold",10)).grid(row=10,column=0)
            mline = Text(root,height=6,width=60)
            mline.grid(row=10,column=1,pady=20,padx=50)
            
            def view():
                CANDIDATEID=e1.get()
                dbCANDIDATE=""
                Select="select CANDIDATEID from student where CANDIDATEID='%s'" %(CANDIDATEID)
                mycursor.execute(Select)
                result1=mycursor.fetchall()
                for i in result1:
                    dbCANDIDATE=i[0]
                Select1="""Select FIRST_NAME,LAST_NAME,ADDRESS,AADHAR_NUMBER,PASSWORD,GENDER,QUALIFICATION,SKILLS,
                WRITE_SOMETHING_ABOUT_YOURSELF from student where CANDIDATEID='%s'""" %(CANDIDATEID)
                mycursor.execute(Select1)
                result2=mycursor.fetchall()
                FIRST_NAME=""
                LAST_NAME=""
                ADDRESS=""
                AADHAR_NUMBER=""
                PASSWORD=""
                GENDER=""
                QUALIFICATION=""
                SKILLS=""
                WRITE_SOMETHING_ABOUT_YOURSELF=""
                if(CANDIDATEID == str(dbCANDIDATE)):
                    for i in result2:
                        FIRST_NAME=i[0]
                        LAST_NAME=i[1]
                        ADDRESS=i[2]
                        AADHAR_NUMBER=i[3]
                        PASSWORD=i[4]
                        GENDER=i[5]
                        QUALIFICATION=i[6]
                        SKILLS=i[7]
                        WRITE_SOMETHING_ABOUT_YOURSELF=i[8]
                    e2.insert(0, FIRST_NAME)
                    e3.insert(0, LAST_NAME)
                    e4.insert(0, ADDRESS)
                    e5.insert(0, AADHAR_NUMBER)
                    e6.insert(0, PASSWORD)
                    v.insert(0, GENDER)
                    e7.insert(0, QUALIFICATION)
                    e8.insert(0, SKILLS)
                    mline.insert(1.0, WRITE_SOMETHING_ABOUT_YOURSELF)
                else:
                    messagebox.showerror("ERROR","No Record Exists",parent=self.root)
            def update():
                CANDIDATEID=e1.get()
                FIRST_NAME=e2.get()
                LAST_NAME=e3.get()
                ADDRESS=e4.get()
                AADHAR_NUMBER=e5.get()
                PASSWORD=e6.get()
                GENDER=v.get()
                QUALIFICATION=e7.get()
                SKILLS=e8.get()
                WRITE_SOMETHING_ABOUT_YOURSELF=mline.get(1.0,END)
                Update="Update student set FIRST_NAME='%s',LAST_NAME='%s',ADDRESS='%s',AADHAR_NUMBER='%s',PASSWORD='%s',GENDER='%s',QUALIFICATION='%s',SKILLS='%s',WRITE_SOMETHING_ABOUT_YOURSELF='%s' where CANDIDATEID='%s'" %(FIRST_NAME,LAST_NAME,ADDRESS,AADHAR_NUMBER,PASSWORD,GENDER,QUALIFICATION,SKILLS,WRITE_SOMETHING_ABOUT_YOURSELF,CANDIDATEID)
                mycursor.execute(Update)
                mydb.commit()
                if(CANDIDATEID==""):
                    messagebox.showerror("ERROR","Fill Details",parent=self.root)
                else:
                    messagebox.showinfo("INFORMATION","Record Updated",parent=self.root)
            def delete():
                CANDIDATEID=e1.get()
                Delete="delete from student where CANDIDATEID='%s'" %(CANDIDATEID)
                mycursor.execute(Delete)
                mydb.commit()
                if(CANDIDATEID==""):
                    messagebox.showerror("ERROR","Fill Details",parent=self.root)
                else:
                    messagebox.showinfo("INFORMATION","Record Deleted",parent=self.root)
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                e6.delete(0, END)
                v.delete(0,END)
                e7.delete(0, END)
                e8.delete(0, END)
                mline.delete('1.0',END)
                
            btn2=Button(self.root,text="VIEW",font=("Bahnschrift",15),width=10,bg="#d77337",fg="white",command=view).grid(row=5,column=3)
            btn3= Button(self.root,text = "UPDATE",fg="White",bg="#d77337",font=("Bahnschrift",14),width=10,command=update).grid(row=7,column=3)
            btn5= Button(self.root,text = "DELETE",fg="White",bg="#d77337",font=("Bahnschrift",14),width=10,command=delete).grid(row=9,column=3)
            btn6= Button(self.root,text = "CANCEL",fg="White",bg="#d77337",font=("Bahnschrift",14),width=10,command=self.root.destroy).grid(row=10,column=3)
    
    root=Tk()
    ob=B(root)
    root.mainloop()
            
btn1 = Button(root,text = "SHOW DETAILS",fg="White",bg="#07663F",font=("Bahnschrift",14),width=15,command=Show)
btn1.grid(row=6,column=1,padx=60,pady=30)
btn4= Button(root,text="CANCEL",fg="white",bg="#A91208",font=("Bahnschrift",14),width=15,command=root.destroy)
btn4.grid(row=6,column=5,padx=20,pady=30)

root.mainloop()




        
        
        
        
        
        
        