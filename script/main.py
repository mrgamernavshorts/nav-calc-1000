import tkinter
from tkinter import *
root = Tk()
root.title("nav calculator 1000")
root.geometry("800x600")
root.maxsize(800,600)

num1_var = IntVar()
num2_var = IntVar()
calc = 0

show_calc_type_label = Label(root, text="",font="arial 15 bold")
ans_label = Label(root,text="",font="arial 15 bold")

def calc_sum():
    global calc
    show_calc_type_label.config(text="+")
    calc = 0
def calc_sub():
    global calc
    show_calc_type_label.config(text="-")
    calc = 1
def calc_multi():
    global calc
    show_calc_type_label.config(text="x")
    calc = 2
def calc_div():
    global calc
    show_calc_type_label.config(text="/")
    calc = 3
def calc_init():
    num1 = num1_var.get()
    num2 = num2_var.get()
    if 0 == calc:
        ans = num1 + num2
    elif 1 == calc:
        ans = num1 - num2
    elif 2 == calc:
        ans = num1 * num2
    elif 3 == calc:
        ans = num1 / num2
    ans_label.config(text=str(ans))

Label(text="NAV CALCULATOR 1000", font="arial 15 bold").pack()
Label(root, text="what do you want to do :", font="arial 10 bold").pack()
Button(text="+", font="arial 15 bold", command=calc_sum).pack()
Button(text="-", font="arial 15 bold", command=calc_sub).pack()
Button(text="x", font="arial 15 bold", command=calc_multi).pack()
Button(text="/", font="arial 15 bold", command=calc_div).pack()
Label(text="first number :", font="arial 15 bold").pack()
Entry(root, font="arial 15 bold",textvariable=num1_var).pack()
show_calc_type_label.pack()
Label(text="second number :",font="arial 15 bold").pack()
Entry(root, font="arial 15 bold",textvariable=num2_var).pack()
Button(text="calculate!",font="arial 12 bold",command=calc_init).pack(pady="5px")
Label(text="answer :",font="arial 15 bold").pack()
ans_label.pack()

root.mainloop()
