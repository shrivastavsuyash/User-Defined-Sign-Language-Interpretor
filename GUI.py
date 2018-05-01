from tkinter import *
from tkinter import messagebox
import subprocess
import os
import time

f=open("instructions.txt","r+")
def option1():
    subprocess.Popen("m1.bat")
def option2():
    subprocess.Popen("m2.bat")
def option3():
    subprocess.Popen("m3.bat")
def option4():
    subprocess.Popen("m4.bat")
    messagebox.showinfo("Instructions", f.read())
def option5():
    subprocess.Popen("m5.bat")

def menu():
    def hello():
       messagebox.showinfo("MENU", "Do nothing!")
    def kill():
        exit()
    top = Tk()
    #background_image=messagebox.PhotoImage("D:\\iip\\images")
    #background_label = tk.Label(parent, image=background_image)
    #background_label.place(x=0, y=0, relwidth=1, relheight=1)
    top.geometry("1500x1500")
    var = StringVar()
    label = Message(top, textvariable=var, relief=RAISED)
    var.set("User Defined Sign Language Interpreter")
    label.configure(width='500',justify=CENTER,bg='light blue',font='Algerian 18 bold',bd='8px',padx='10',pady='20',fg='black')
    label.pack()
    labelframe = LabelFrame(top, text="MENU")
    labelframe.configure(bg='light green',font='Arial 15 bold',fg='green',bd='5px')
    B1 = Button(top, text = "Instructions", command = option4)
    B1.configure(bg='brown',fg='white',font='Arial 15 bold')
    B1.place(x = 35,y = 180)
    B2 = Button(top, text = "Gesture Recognition", command = option1,fg='white')
    B2.configure(bg='green',font='Arial 15 bold')
    B2.place(x = 35,y = 250)
    B3 = Button(top, text ="Text to Speech Convertor" , command = option2,fg='white')
    B3.configure(bg='brown',font='Arial 15 bold')
    B3.place(x = 35,y = 320)
    B4 = Button(top, text = "Text scrapper From Audio", command = option3,fg='white')
    B4.configure(bg='green',font='Arial 15 bold')
    B4.place(x = 35,y = 390)
    B5 = Button(top, text = "Talk to me", command = option5,fg='white')
    B5.configure(bg='brown',font='Arial 15 bold')
    B5.place(x = 35,y = 460)
    B6 = Button(top, text = "EXIT", command = kill,fg='white')
    B6.configure(bg='green',font='Arial 15 bold')
    B6.place(x = 650,y = 530)
    left = Label(labelframe, text="Select any option!")
    left.configure(bg='green',font='Arial 16 bold',bd='4px',padx='3',pady='3',fg='white')
    left.place(x=580,y=10)
    labelframe.pack(fill="both", expand="yes")
    top.mainloop()
menu()
f.close()
    
