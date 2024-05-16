'''
Problem Statement:
Design a GUI based Calculator, using Tkinter.
'''

#import tkinter
from tkinter import *

#1-Creating window, and buttons.

root = Tk() 
root.title("Simple Calculator")

e = Entry(root, font=('Arial',20), width = 20, borderwidth = 5)
e.grid(row = 0 , column = 0 , columnspan = 3 , padx = 20, pady = 20)


#2-Defining 7 functions;(click,clear,add,sub,mul,div,equal).

def click(number):
     current = e.get()
     e.delete(0,END)
     e.insert(0, str(current) + str(number))

def clear():
     e.delete(0,END)

def add():
     f_n = e.get()
     global f_num
     global math
     math = "addition"
     f_num = int(f_n)
     e.delete(0,END)

def sub():
     f_n = e.get()
     global f_num
     global math
     math = "subtraction"
     f_num = int(f_n)
     e.delete(0,END)

def mul():
     f_n = e.get()
     global f_num
     global math
     math = "multiplication"
     f_num = int(f_n)
     e.delete(0,END)

def div():
     f_n = e.get()
     global f_num
     global math
     math = "division"
     f_num = int(f_n)
     e.delete(0,END)
     
def equal():
     s_num = int(e.get())
     e.delete(0, END)
     if math == "addition":
          e.insert(0 , f_num + s_num)
     elif math == "subtraction":
          e.insert(0 , f_num - s_num)
     elif math == "multiplication":
          e.insert(0 , f_num * s_num)
     elif math == "division":
          e.insert(0 , f_num / s_num)
     



     
#3- Defining 16 buttons, by using 'callback' (for each button).
          
bt1 = Button(root, text = "1", padx = 40 , pady = 20, command = lambda : click(1)) #callback
bt2 = Button(root, text = "2", padx = 40 , pady = 20, command = lambda : click(2)) #callback
bt3 = Button(root, text = "3", padx = 40 , pady = 20, command = lambda : click(3)) #callback
bt4 = Button(root, text = "4", padx = 40 , pady = 20, command = lambda : click(4)) #callback
bt5 = Button(root, text = "5", padx = 40 , pady = 20, command = lambda : click(5)) #callback
bt6 = Button(root, text = "6", padx = 40 , pady = 20, command = lambda : click(6)) #callback
bt7 = Button(root, text = "7", padx = 40 , pady = 20, command = lambda : click(7)) #callback
bt8 = Button(root, text = "8", padx = 40 , pady = 20, command = lambda : click(8)) #callback
bt9 = Button(root, text = "9", padx = 40 , pady = 20, command = lambda : click(9)) #callback
bt0 = Button(root, text = "0", padx = 40 , pady = 20, command = lambda : click(0)) #callback
btadd = Button(root, text = "+", padx = 39 , pady = 20, command = add) #callback
btsub = Button(root, text = "-", padx = 41 , pady = 20, command = sub) #callback
btmul = Button(root, text = "*", padx = 40 , pady = 20, command = mul) #callback
btdiv = Button(root, text = "/", padx = 41 , pady = 20, command = div) #callback

btEquals = Button(root, text = "=", padx = 90 , pady = 20, command = equal) #callback
btClear = Button(root, text = "Clear", padx = 79 , pady = 20, command = clear) #callback




#4- Positioning the buttons.


bt1.grid(row = 3, column = 0)
bt2.grid(row = 3, column = 1)
bt3.grid(row = 3, column = 2)

bt4.grid(row = 2, column = 0)
bt5.grid(row = 2, column = 1)
bt6.grid(row = 2, column = 2)

bt7.grid(row = 1, column = 0)
bt8.grid(row = 1, column = 1)
bt9.grid(row = 1, column = 2)

bt0.grid(row = 4, column = 0 )
btadd.grid(row = 5, column = 0 )
btEquals.grid(row = 5, column = 1, columnspan = 2)
btClear.grid(row = 4, column = 1, columnspan = 2)
btsub.grid(row = 6, column = 0 )
btmul.grid(row = 6, column = 1 )
btdiv.grid(row = 6, column = 2 )

root.mainloop()

