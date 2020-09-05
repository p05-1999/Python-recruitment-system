# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:01:30 2020

@author: Parnisha
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 14:06:30 2020

@author: Parnisha
"""


# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 20:59:35 2020

@author: Parnisha
"""
from tkinter.ttk import *
from tkinter import *
import os
import mysql.connector
from tkinter import messagebox

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="poulami@2",
    database="candidate"
)
mycursor=mydb.cursor()
root = Tk()
v=StringVar()

root.configure(bg="light green")
root.geometry("1199x600+60+20")

root.title("WELCOME TO RECRUITMENT SCREEN")

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
e4.grid(row = 4, column = 1,ipadx=80,pady=10)

Label(root,text="AADHAR_NUMBER",fg="black",bg="light green",font=("Bold",10)).grid(row=5,column=0)
e5 = Entry(root)
e5.grid(row=5 ,column=1,ipadx=80,pady=10)

Label(root,text="PASSWORD",fg="black",bg="light green",font=("Bold",10)).grid(row=6,column=0)
e6 = Entry(root)
e6.grid(row=6,column=1,ipadx=80,pady=10)

Label(root,text="GENDER",fg="black",bg="light green",font=("Bold",10)).grid(row=7,column=0,pady=10)
rd = Radiobutton(root,text = "MALE",variable=v,value="male",fg="navy blue",bg="light green",font=("Calibri Bold",12))
rd.grid(row=7,column=1)
rd2 = Radiobutton(root,text ="FEMALE",variable=v,value="female",fg="navy blue",bg="light green",font=("Calibri Bold",12))
rd2.grid(row=7,column=2)


Label(root,text="QUALIFICATION",fg="black",bg="light green",font=("Bold",10)).grid(row=8,column=0,pady=15)
e7 = Entry(root)
e7.grid(row=8,column=1,pady=10,padx=30,ipadx=80)

Label(root,text="SKILLS",fg="black",bg="light green",font=("Bold",10)).grid(row=9,column=0,pady=15)
e8 = Entry(root)
e8.grid(row=9, column=1,pady=10,ipadx=80)

Label(root,text="WRITE_SOMETHING_ABOUT_YOURSELF",fg="black",bg="light green",font=("Bold",10)).grid(row=10,column=0)
mline = Text(root,height=6,width=60)
mline.grid(row=10,column=1,pady=20,padx=50)

def Submit():
    CANDIDATEID=e1.get()
    dbCANDIDATEID=""
    Select="select CANDIDATEID from student where CANDIDATEID='%s'" %(CANDIDATEID)
    mycursor.execute(Select)
    result=mycursor.fetchall()
    for i in result:
        dbCANDIDATEID=i[0]
    if(CANDIDATEID == dbCANDIDATEID):
            messagebox.askokcancel("INFORMATION","Record Already Exists")
    else:
        Insert="""Insert into student(CANDIDATEID,FIRST_NAME,LAST_NAME,ADDRESS,AADHAR_NUMBER,PASSWORD,GENDER,QUALIFICATION,SKILLS,WRITE_SOMETHING_ABOUT_YOURSELF) 
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        FIRST_NAME=e2.get()
        LAST_NAME=e3.get()
        ADDRESS=e4.get()
        AADHAR_NUMBER=e5.get()
        PASSWORD=e6.get()
        GENDER=v.get()
        QUALIFICATION=e7.get()
        SKILLS=e8.get()
        WRITE_SOMETHING_ABOUT_YOURSELF=mline.get(1.0,END)
        if(CANDIDATEID !="" and FIRST_NAME !="" and LAST_NAME !="" and ADDRESS !="" and AADHAR_NUMBER !="" and PASSWORD !="" and GENDER !="" and QUALIFICATION !="" and SKILLS !="" and WRITE_SOMETHING_ABOUT_YOURSELF !=""):
            Value=(CANDIDATEID,FIRST_NAME,LAST_NAME,ADDRESS,AADHAR_NUMBER,PASSWORD,GENDER,QUALIFICATION,SKILLS,WRITE_SOMETHING_ABOUT_YOURSELF)
            mycursor.execute(Insert,Value)
            mydb.commit()
            messagebox.askokcancel("Information","Record inserted")
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            v.set(0)
            e7.delete(0, END)
            e8.delete(0, END)
            mline.delete('1.0',END)
        else:
            if(FIRST_NAME == "" and LAST_NAME == "" and ADDRESS =="" and AADHAR_NUMBER == "" and PASSWORD == "" and GENDER == "" and QUALIFICATION == "" and SKILLS =="" and WRITE_SOMETHING_ABOUT_YOURSELF ==""):
                messagebox.askokcancel("Information","New Entry Fill All Details")
            else:
                messagebox.askokcancel("Information", "Some fields left blank")

def callnext():
    root.destroy()
    os.system('python welcome.py')
     
       
def Clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    v.set(0)
    e7.delete(0, END)
    e8.delete(0, END)
    mline.delete('1.0',END)
    
btn1 = Button(root,text = "SUBMIT",fg="White",bg="Purple",font=("Bahnschrift",14),width=10,command=Submit)
btn1.grid(row=11,column=0)
btn2= Button(root,text = "CLEAR",fg="White",bg="Purple",font=("Bahnschrift",14),width=10,command=Clear)
btn2.grid(row=11,column=1)
btn3= Button(root,text = "LOGIN",fg="White",bg="Purple",font=("Bahnschrift",14),width=10,command=callnext)
btn3.grid(row=11,column=2)
btn4= Button(root,text="CANCEL",fg="Red",bg="Yellow",font=("Bahnschrift",14),width=10,command=root.destroy)
btn4.grid(row=11,column=4,padx=80,pady=20)

root.mainloop()
