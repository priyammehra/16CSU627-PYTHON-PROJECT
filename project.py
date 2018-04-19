import tkinter
from tkinter import *
import time

w=Tk()
w.geometry("1730x750")
w.title("PAWN SHOP")
w.configure(background="#F4F3F4")

flag=0


def update(): 
    x1=s1.get() 
    x2=s2.get() 
    x3=s3.get() 
    x4=s4.get() 
    x5=s5.get() 
    f=open("file1.txt","r") 
    k=f.readlines() 
    f.close()                               # f.writelines(itemid.ljust(40)+itemname.ljust(20)+date.ljust(20)+price.ljust(20)+customer.ljust(20)+\n '''
    f=open("file1.txt","w") 
    x=0
    for i in k: 
        j=i.split() 
        if(j[0]!=x1): 
            f.writelines(j[0].ljust(20)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(5)+"\n") 
     
        else: 
            f.writelines(j[0].ljust(20)+x2.ljust(20)+x3.ljust(20)+x4.ljust(20)+x5.ljust(5)+"\n") 
            z=1
            s6.set("SUCCESSFULLY UPDATED")

    if(z==0):
            s6.set("CANNOT BE UPDATED")     




def first():

        global flag
        f=open("file1.txt","r")
        l=f.readlines()
        y=l[0].split()
        s1.set(y[0])
        s2.set(y[1])
        s3.set(y[2])
        s4.set(y[3])
        s5.set(y[4])
        s6.set("FIRST RECORD")    
        flag=1      
        f.close()


def last():
 
        global flag
        f=open("file1.txt","r")
        l=f.readlines()
        a=len(l)
        y=l[a-1].split()
        s1.set(y[0])
        s2.set(y[1])
        s3.set(y[2])
        s4.set(y[3])
        s5.set(y[4])
        s6.set("LAST RECORD")
        flag=a-1
        f.close()

def prev():
    global flag 
    a=""
    s6.set(a)
    i=0 
    f=open("file1.txt","r") 
    try: 
         
        while(flag-1>i): 
            li=f.readline()
            i=i+1 
 
        y=li.split() 
        s1.set(y[0]) 
        s2.set(y[1]) 
        s3.set(y[2]) 
        s4.set(y[3]) 
        s5.set(y[4]) 
        flag=flag-1

    except: 
        s1.set(" ") 
        s2.set(" ") 
        s3.set(" ") 
        s4.set(" ") 
        s5.set(" ")
        s6.set("NO MORE RECORD FOUND") 
        flag=0
         


def nextrec(): 
    global flag 
    a=""
    s6.set(a)
    i=0 
    f=open("file1.txt","r") 
    
    try: 
         
        while(i<=flag): 
            li=f.readline() 
            i=i+1
 
        m=li.split() 
        s1.set(m[0]) 
        s2.set(m[1]) 
        s3.set(m[2]) 
        s4.set(m[3]) 
        s5.set(m[4]) 
        flag=flag+1
        
    except: 
        m=""
        s1.set(m) 
        s2.set(m) 
        s3.set(m) 
        s4.set(m) 
        s5.set(m)
        s6.set("NO MORE RECORD FOUND") 
        f.close() 

def search(): 
    k=s1.get() 
    f=open("file1.txt","r") 
    h=f.readlines() 
    
    try:
     for i in h: 
        j=i.split() 
       
        if(j[0]==k): 
              
            s1.set(j[0]) 
            s2.set(j[1]) 
            s3.set(j[2]) 
            s4.set(j[3]) 
            s5.set(j[4]) 
            s6.set("CUSTOMER FOUND")
        
            f.close()   
    except:    
        
            s6.set("CUSTOMER NOT FOUND")           
            f.close()



def input():

    f=open("file1.txt","a")
    itemid=s1.get()
    itemname=s2.get()
    date=s3.get()
    price=s4.get()
    customer=s5.get()
    s6.set("ENTRY SUCCESS")
    f.writelines(itemid.ljust(20)+itemname.ljust(20)+date.ljust(20)+price.ljust(20)+customer.ljust(20)+"\n")
    f.close()








def delrec(): 

    k=[s1.get(),s2.get(),s3.get(),s4.get(),s5.get()] 
    f=open("file1.txt","r") 
    lines=f.readlines() 
    print(lines) 
    print(k) 
    f.close() 
    f=open("file1.txt","w") 
    for i in lines: 
        m=i.split() 
        print(m) 
        if(m!=k): 
             f.writelines(m[0].ljust(20)+m[1].ljust(20)+m[2].ljust(20)+m[3].ljust(20)+m[4].ljust(5)+"\n") 
             clear()
             s6.set("RECORD DELETED")
    f.close() 


def clear(): 
     
    s1.set("") 
    s2.set("") 
    s3.set("") 
    s4.set("") 
    s5.set("") 
    s6.set("")



t=time.asctime(time.localtime(time.time()))
mainlabel=Label(w,text=" Pawn Shop Managment System ",font=('impact 40 bold underline'),fg='#D50B53', bd=10,anchor='w',bg='#F4F3F4')
mainlabel2=Label(w,text=t ,font=('impact 40 bold underline'),fg='#D50B53',bd=10,bg='#F4F3F4',anchor='w')
lab1=Label(w,text="ITEM ID",font='impact 20' ,fg='#B9C406',anchor='w',relief="solid",padx=32,bg="white",pady=10)
lab2=Label(w,text="ITEM NAME",font='impact 20',fg='#B9C406',anchor='w',bd=2,bg='white',relief="solid",padx=16,pady=10)
lab3=Label(w,text="DATE",font='impact 20',fg='#B9C406',anchor='w',bd=2,bg='white',relief="solid",padx=49,pady=10)
lab4=Label(w,text="PRICE",font='impact 20',fg='#B9C406',anchor='w',bd=2,bg='white',relief="solid",padx=45,pady=10)
lab5=Label(w,text="CUSTOMER",font='impact 20',fg='#B9C406',anchor='w',bd=2,bg='white',relief="solid",padx=17,pady=10)

mainlabel.grid(row=0,column=5,padx=0)
mainlabel2.grid(row=1,column=5,padx=75)
lab1.grid(row=3,column=2,pady=10,padx=15)
lab2.grid(row=4,column=2,pady=10,padx=15)
lab3.grid(row=5,column=2,pady=10,padx=15)
lab4.grid(row=6,column=2,pady=10,padx=15)
lab5.grid(row=7,column=2,pady=10,padx=15)

s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()

e1=Entry(w,bg='gray',textvariable=s1,font="impact 20 ",fg='white',bd=10,justify='center')
e2=Entry(w,bg='gray',font="impact 20 ",textvariable=s2,fg='white',bd=10,justify='center')
e3=Entry(w,bg='gray',font="impact 20 ",textvariable=s3,fg='white',bd=10,justify='center')
e4=Entry(w,bg='gray',textvariable=s4,font="impact 20 ",fg='white',bd=10,justify='center')
e5=Entry(w,bg='gray',textvariable=s5,font="impact 20 ",fg='white',bd=10,justify='center')
e6=Entry(w,bg='gray',textvariable=s6,font="impact 20 ",fg='white',bd=10,justify='center',width=40)

e1.grid(row=3,column=3,padx=5)
e2.grid(row=4,column=3,padx=5)
e3.grid(row=5,column=3,padx=5)
e4.grid(row=6,column=3,padx=5)
e5.grid(row=7,column=3,padx=5)
e6.grid(row=4,column=5,columnspan=2, padx=10)

addbutton=Button(w,text="ADD",font="impact 20 ",fg='#522E75',anchor='center',bd=10,command=input,padx=18,pady=5).grid(row=3,column=25)
deletebutton=Button(w,text="DELETE",font="impact 20 ",bd=10,command=delrec,fg='#522E75',pady=5).grid(row=4,column=25)
ebutton=Button(w,text="UPDATE",font="impact 20 ",bd=10,fg='#522E75',pady=5,command=update).grid(row=5,column=25)
searchbutton=Button(w,text="SEARCH",font="impact 20 ",bd=10,command=search,fg='#522E75',pady=5).grid(row=6,column=25)
clearbutton=Button(w,text="CLEAR",font="impact 20",bd=10,command=clear,fg='#522E75',pady=8,padx=9).grid(row=7,column=25)

nextr=Button(w,text=">>",font="impact 20 ",anchor='center',bd=15,command=nextrec,fg='#522E75').grid(row=8,column=4,sticky='s',pady=20)
prev=Button(w,text="<<",font="impact 20 ",bd=15,command=prev,fg='#522E75').grid(row=8,column=1,sticky='s',pady=20)
first=Button(w,text="FIRST",font="impact 20 ",bd=15,fg='#522E75',command=first).grid(row=8,column=2,sticky="s",pady=20)
last=Button(w,text="LAST",font="impact 20 ",bd=15,fg='#522E75',command=last).grid(row=8,column=3,sticky="s",pady=20,padx=20)


w.mainloop()