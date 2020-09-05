# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 14:09:00 2020

@author: Parnisha
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 23:01:02 2020

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
root.configure(bg="light blue")
root.geometry("900x400+100+50")
root.resizable(False,False)
root.title("CANDIDATE DETAILS")
Label(root,text="CANDIDATE APPLICATIONS",fg="NAVY BLUE",bg="light BLUE",font=("Arial Bold",19)).grid(row=0,column=2,pady=10)

Label(root, text="SKILLS",fg="navy blue",bg="light blue",font=("Bold",13),padx=20).grid(row=1,column=0)
e1 = Entry(root)
e1.grid(row= 1, column=1,ipadx=30,pady=30,padx=20)

def Showall():
    class A(Frame):
        def __init__(self,parent):
            Frame.__init__(self,parent)
            self.CreateUI()
            self.Loadtable()
            self.grid(sticky=(N,S,W,E))
            parent.grid_rowconfigure(0,weight=1)
            parent.grid_columnconfigure(0,weight=1)
            
        def CreateUI(self):
            tv=Treeview(self)
            tv.place(x=30, y=90)
            tv['columns']=('CANDIDATEID','FIRST_NAME','LAST_NAME','ADDRESS','AADHAR_NUMBER','PASSWORD','GENDER','QUALIFICATION','SKILLS','WRITE_SOMETHING_ABOUT_YOURSELF')
            tv.heading('#0',text='CANDIDATEID',anchor='center')
            tv.column('#0', anchor='center')
            tv.heading('#1', text='FIRST_NAME', anchor='center')
            tv.column('#1', anchor='center')
            tv.heading('#2', text='LAST_NAME', anchor='center')
            tv.column('#2', anchor='center')
            tv.heading('#3', text='ADDRESS', anchor='center')
            tv.column('#3', anchor='center')
            tv.heading('#4', text='AADHAR_NUMBER', anchor='center')
            tv.column('#4', anchor='center')
            tv.heading('#5', text='PASSWORD', anchor='center')
            tv.column('#5', anchor='center')
            tv.heading('#6', text='GENDER', anchor='center')
            tv.column('#6', anchor='center')
            tv.heading('#7', text='QUALIFICATION', anchor='center')
            tv.column('#7', anchor='center')
            tv.heading('#8', text='SKILLS', anchor='center')
            tv.column('#8',anchor='center')
            tv.heading('#9', text='WRITE_SOMETHING_ABOUT_YOURSELF', anchor='center')
            tv.column('#9', anchor='center')
            tv.grid(columnspan=1,sticky=(N,S,W,E))
            self.treeview = tv
            self.grid_rowconfigure(0,weight=1)
            self.grid_columnconfigure(0,weight=1)
            
        def Loadtable(self):
            SKILLS=e1.get()
            Select="Select * from student where SKILLS='%s'" %(SKILLS)
            mycursor.execute(Select)
            result=mycursor.fetchall()
            CANDIDATEID=""
            FIRST_NAME=""
            LAST_NAME=""
            ADDRESS=""
            AADHAR_NUMBER=""
            PASSWORD=""
            GENDER=""
            QUALIFICATION=""
            SKILLS=""
            WRITE_SOMETHING_ABOUT_YOURSELF=""
            for i in result:
                CANDIDATEID=i[0]
                FIRST_NAME=i[1]
                LAST_NAME=i[2]
                ADDRESS=i[3]
                AADHAR_NUMBER=i[4]
                PASSWORD=i[5]
                GENDER=i[6]
                QUALIFICATION=i[7]
                SKILLS=i[8]
                WRITE_SOMETHING_ABOUT_YOURSELF=i[9]
                self.treeview.insert("",'end',text=CANDIDATEID,values=(FIRST_NAME,LAST_NAME,ADDRESS,AADHAR_NUMBER,PASSWORD,GENDER,QUALIFICATION,SKILLS,WRITE_SOMETHING_ABOUT_YOURSELF))
    root=Tk()
    root.resizable(width=0, height=0)
    root.title("Overview Page")
    A(root)
    
    

btn1 = Button(root, text = "SEARCH",fg="White",bg="Purple",font=("Bahnschrift",14),width=15,command=Showall)
btn1.grid(row=1,column=2,padx=20)

btn2= Button(root, text="CANCEL",fg="White",bg="Red",font=("Bahnschrift",14),width=15,command=root.destroy)
btn2.grid(row=1,column=3,padx=20)
root.mainloop()