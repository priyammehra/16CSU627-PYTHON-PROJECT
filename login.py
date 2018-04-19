import tkinter
from tkinter import *
import os

w=Tk()
w.geometry("720x355")
w.title("PAWN SHOP")
w.configure(background="#F4F3F4")


s1=StringVar()
s2=StringVar()
s3=StringVar()


lab1=Label(w,text="USERNAME",font='impact 20' ,fg='#B9C406',anchor='w',relief="solid",padx=32,bg="white",pady=10)
lab2=Label(w,text="PASSWORD",font='impact 20',fg='#B9C406',anchor='w',bd=2,bg='white',relief="solid",padx=26,pady=10)

e1=Entry(w,bg='gray',textvariable=s1,font="impact 20 ",fg='white',bd=10,justify='center')
e2=Entry(w,bg='gray',textvariable=s2,show='*',font="impact 20 ",fg='white',bd=10,justify='center')
e3=Entry(w,bg='gray',textvariable=s3,font="impact 20 ",fg='white',bd=10,justify='center', width=30)

lab1.grid(row=3,column=2,pady=10,padx=15)
lab2.grid(row=4,column=2,pady=10,padx=10)
e1.grid(row=3,column=3,padx=5)
e2.grid(row=4,column=3,padx=5)
e3.grid(row=5,column=3,padx=15,pady=20)

def login():
    
    username=s1.get()
    password=s2.get()
    if (username=="16csu267" or username=="16CSU267") and (password=="abc"):
        s3.set("WELCOME BACK")
        os.system('python project.py')
    else:
        s1.set("")
        s2.set("")
        s3.set("SORRY TRY AGAIN")
        
    
login=Button(w,text="LOGIN",font="impact 20 ",bd=15,fg='#522E75',command=login,width=30).grid(row=6,column=3,sticky="s")
w.mainloop()
