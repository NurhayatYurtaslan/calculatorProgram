#Importing the necessary modules
from tkinter import *
import parser
from math import factorial

root = Tk()
root.title('NurLife Calculator')
root.configure(background="gray")
#root.geometry("720x450")

#It keeps the track of current position on the input text field
i = 0
# Receives the digit as parameter and display it on the input field
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1
 
# Calculate function scans the string to evaluates and display it
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
 
# Function which takes operator as input and displays it on the input field
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length
 
#Function to clear the input field 
def clear_all():
    display.delete(0,END)
 
#Function which works like backspace
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")

#Function to calculate the factorial and display it
def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

#--------------------------------------UI Design ---------------------------------------------

#adding the input field
display = Entry(root)
display.grid(row=1,columnspan=100,ipady=10,sticky=N+E+W+S)
display.configure(background="thistle") 

#Code to add buttons to the Calculator
bc="mediumorchid"
x=0
w=10
h=3
b=3

Button(root,text="1",width = w, height = h, bd = b,bg=bc,command = lambda :get_variables(1)).grid(row=2,column=0,pady=x,sticky=N+S+E+W)
Button(root,text="2",width = w, height = h, bd = b,bg=bc,command = lambda :get_variables(2)).grid(row=2,column=1,pady=x,sticky=N+S+E+W)
Button(root,text="3",width = w, height = h, bd = b,bg=bc,command = lambda :get_variables(3)).grid(row=2,column=2,pady=x,sticky=N+S+E+W)
 
Button(root,text="4",width = w, height = h, bd = b,bg=bc,command = lambda :get_variables(4)).grid(row=3,column=0,pady=x, sticky=N+S+E+W)
Button(root,text="5",width = w, height = h, bd = b,bg=bc,command = lambda :get_variables(5)).grid(row=3,column=1,pady=x, sticky=N+S+E+W)
Button(root,text="6",width = w, height = h, bd = b,bg=bc,command = lambda :get_variables(6)).grid(row=3,column=2,pady=x, sticky=N+S+E+W)
 
Button(root,text="7",width = w, height = h, bd = b,bg=bc,command = lambda :get_variables(7)).grid(row=4,column=0,pady=x, sticky=N+S+E+W)
Button(root,text=" 8",width = w, height = h, bd = b,bg=bc,command = lambda :get_variables(8)).grid(row=4,column=1,pady=x, sticky=N+S+E+W)
Button(root,text=" 9",width = w, height = h, bd = b,bg=bc,command = lambda :get_variables(9)).grid(row=4,column=2,pady=x, sticky=N+S+E+W)
 
#adding other buttons to the calculator
Button(root,text="AC",width = w, height = h, bd = b,bg=bc,command=lambda :clear_all()).grid(row=5,column=0,pady=x, sticky=N+S+E+W)
Button(root,text=" 0",width = w, height = h, bd = b,bg=bc,command = lambda :get_variables(0)).grid(row=5,column=1,pady=x, sticky=N+S+E+W)
Button(root,text=" .",width = w, height = h, bd = b,bg=bc,command=lambda :get_variables(".")).grid(row=5, column=2,pady=x, sticky=N+S+E+W)
 
 
Button(root,text="+",width = w, height = h, bd = b,bg=bc,command= lambda :get_operation("+")).grid(row=2,column=3,pady=x, sticky=N+S+E+W)
Button(root,text="-",width = w, height = h, bd = b,bg=bc,command= lambda :get_operation("-")).grid(row=3,column=3,pady=x, sticky=N+S+E+W)
Button(root,text="*",width = w, height = h, bd = b,bg=bc,command= lambda :get_operation("*")).grid(row=4,column=3,pady=x, sticky=N+S+E+W)
Button(root,text="/",width = w, height = h, bd = b,bg=bc,command= lambda :get_operation("/")).grid(row=5,column=3,pady=x, sticky=N+S+E+W)
 
# adding new operations
Button(root,text="pi",width = w, height = h, bd = b,bg=bc,command= lambda :get_operation("*3.14")).grid(row=2,column=4,pady=x, sticky=N+S+E+W)
Button(root,text="%",width = w, height = h, bd = b,bg=bc,command= lambda :get_operation("%")).grid(row=3,column=4,pady=x, sticky=N+S+E+W)
Button(root,text="(",width = w, height = h, bd = b,bg=bc,command= lambda :get_operation("(")).grid(row=4,column=4,pady=x, sticky=N+S+E+W)
Button(root,text="exp",width = w, height = h, bd = b,bg=bc,command= lambda :get_operation("**")).grid(row=5,column=4,pady=x, sticky=N+S+E+W)
 
Button(root,text="<-",width = w, height = h, bd = b,bg=bc,command= lambda :undo()).grid(row=2,column=5,pady=x, sticky=N+S+E+W)
Button(root,text="x!",width = w, height = h, bd = b,bg=bc, command= lambda: fact()).grid(row=3,column=5,pady=x, sticky=N+S+E+W)
Button(root,text=")",width = w, height = h, bd = b,bg=bc,command= lambda :get_operation(")")).grid(row=4,pady=x,column=5, sticky=N+S+E+W)
Button(root,text="^2",width = w, height = h, bd = b,bg=bc,command= lambda :get_operation("**2")).grid(row=5,pady=x,column=5, sticky=N+S+E+W)
Button(root,text="^2",width = w, height = h, bd = b,bg=bc,command= lambda :get_operation("**2")).grid(row=5,pady=x,column=5, sticky=N+S+E+W)
Button(root,text="=",width = w, height = h, bd = b,bg=bc,command= lambda :calculate()).grid(columnspan=100,pady=x, sticky=N+S+E+W)

root.mainloop()
