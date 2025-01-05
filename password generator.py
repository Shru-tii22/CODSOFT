from tkinter import *
import string
import random

root=Tk()
root.geometry("360x350")
root.title("Password Generator")

l1=Label(root,font="time 15 bold")
l1.place(x=30,y=30)
l2=Label(root,text="Enter Password Length",font="time 15 bold")
l2.place(x=30,y=90)

e1=Entry(root,font=("arial",10),width=23, bd=3)
e1.place(x=25,y=133)

def gen():
    num=int(e1.get())
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation

    S=[]
    S.extend(list(s1))
    S.extend(list(s2))
    S.extend(list(s3))
    S.extend(list(s4))

    random.shuffle(S)
    Password=S[0:num]
    l3=Label(root,text="Password: ",font="time 15 bold")
    l3.place(x=30,y=250)
    l4=Label(root,text = Password ,font="time 15 bold",width=25 , bg="white")
    l4.place(x=150,y=250)


button=Button(root,text="Generate Password",fg="white",bg="gray",font="time 15 bold",width=25,command=gen)
button.place(x=30,y=180)

root.mainloop()
