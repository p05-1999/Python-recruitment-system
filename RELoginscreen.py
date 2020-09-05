# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 10:16:28 2020

@author: Parnisha
"""


from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import os
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN SYSTEM")
        self.root.geometry("900x600+100+40")
        self.root.resizable(False,False)
        # for colour----
        #self.root.configure(bg="#DC7633")
        #for image------
        self.bg=ImageTk.PhotoImage(file="E:/New folder/bussiness1.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        #frame
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)
        
        title=Label(Frame_login,text="LOGIN HERE",font=("Impact",35),fg="#d77337",bg="white").place(x=90,y=30)
        desc=Label(Frame_login,text="Recruiter Login Area",font=("Goudy old style",15),fg="orange",bg="white").place(x=90,y=100)
        
        lbl_user=Label(Frame_login,text="USERNAME",font=("Goudy old style",15),fg="black",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)
        
        lbl_pass=Label(Frame_login,text="PASSWORD",font=("Goudy old style",15),fg="black",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)
        
        btn=Button(Frame_login,text="LOGIN",font=("Bahnschrift",15),width=10,bg="#d77337",fg="white",command=self.loginFunc).place(x=90,y=285)
        
    def loginFunc(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("ERROR","All Fields Are Required",parent=self.root)
        elif self.txt_pass.get()!="123456":   
            messagebox.showerror("ERROR","Invalid PASSWORD",parent=self.root)
        elif self.txt_user.get()!="Parnisha":
            messagebox.showerror("ERROR","Invalid USERNAME",parent=self.root)
        else:
            root.destroy()
            os.system('python candidate.py')
        
        
root=Tk()
obj=Login(root)
root.mainloop()