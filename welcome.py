# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 16:12:43 2020

@author: Parnisha
"""

from tkinter.ttk import *
from tkinter import *
import mysql.connector
from PIL import ImageTk
from tkinter import messagebox
import os
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="poulami@2",
    database="candidate"
)
mycursor=mydb.cursor()
def callNext():
    root.destroy()
    os.system('python RECRUITMENT1.py')


def callNewscreen():
    root.destroy()
    os.system('python RELoginscreen.py')

class Welcome:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x600+100+40")
        #for colour bg----
        #self.root.configure(bg="#008080")
        self.root.resizable(False,False)
        # for image----
        self.bg=ImageTk.PhotoImage(file="E:/New folder/bussiness.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        Frame_welcome=Frame(self.root,bg="white")
        Frame_welcome.place(x=150,y=150,height=340,width=500)
        title=Label(Frame_welcome,text="LOGIN HERE",font=("Impact",35),fg="#008080",bg="white").place(x=90,y=30)
        desc=Label(Frame_welcome,text="Exister Login Area",font=("Goudy old style",15),fg="#16ABB8",bg="white").place(x=90,y=100)

        lbl_user=Label(Frame_welcome,text="USERID",font=("Goudy old style",15),fg="black",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_welcome,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)
        
        lbl_pass=Label(Frame_welcome,text="PASSWORD",font=("Goudy old style",15),fg="black",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_welcome,font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)
        
        btn=Button(Frame_welcome,text="LOGIN",font=("Bahnschrift",15),width=10,bg="#008080",fg="white",command=self.WelcomeFunc).place(x=40,y=285)
        btn=Button(Frame_welcome,text="NEW USER?",font=("Bahnschrift",15),width=10,bg="#008080",fg="white",command=callNext).place(x=195,y=285)
        btn=Button(Frame_welcome,text="RECRUITER",font=("Bahnschrift",15),width=10,bg="#008080",fg="white",command=callNewscreen).place(x=350,y=285)
        
        
        
    def WelcomeFunc(self):
        CANDIDATEID_page=self.txt_user.get()
        PASSWORD_page=self.txt_pass.get()
        Select="Select CANDIDATEID, PASSWORD from student where CANDIDATEID='%s'" %(CANDIDATEID_page)
        mycursor.execute(Select)
        result=mycursor.fetchall()
        if self.txt_user.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("ERROR","All Fields Are Required",parent=self.root)
        elif CANDIDATEID_page!=str(result[0][0]):
            messagebox.showerror("ERROR","Invalid USERID",parent=self.root)
        elif self.txt_pass.get()!=str(result[0][1]):
            messagebox.showerror("ERROR","Invalid PASSWORD",parent=self.root)
        else:
            root.destroy()
            os.system('python existinguser.py')
        
        
root=Tk()
obj=Welcome(root)
root.mainloop()
        
        
        
        
        
        
        