from setuptools import command
import numbers
from tkinter import*
from math import*

def temp():
    MainWindow = Tk()
    MainWindow.title("pycalc")

# Func ------------------------------------------------

    def btnClick(number):
        current = e.get()
        e.delete(0, END)
        newNumber = str(current)+str(number)
        e.insert(0, newNumber)
        return 0

    def btnCommand(command):
        global number
        global num1  # remember number
        global mathOp
        mathOp = command  # +,-,*,/
        num1 = float(e.get())
        e.delete(0, END)
        return 0

    def btnEquals():
        num2 = float(e.get())
        result=0
        if mathOp=="+":
            result=num1+num2
        elif mathOp=="-":
            result=num1-num2
        elif mathOp=="*":
            result=num1*num2
        elif mathOp=="/":
            result=num1/num2
        elif mathOp=="%":
            result=0.01*num1*num2
        else:
            result=0
        e.delete(0, END)
        e.insert(0, str(result))
        return 0
    
    def btnClear():
        e.delete(0, END)
        num1=0
        mathOp=""
        return 0

    def btnSqroot():
        global num1
        global mathOp
        mathOp = command
        num1=float(e.get())
        num1=sqrt(num1)
        e.delete(0, END)
        e.insert(0, num1)

    def btnSqrrd():
        global num1
        global mathOp
        mathOp = command
        num1=int(e.get())
        num2=num1*num1
        e.delete(0, END)
        e.insert(0, num2)

    def btnDott():
        if e.get()==".":
            pass
        else:
            e.insert(END, ".")

    def btnSinn():
        global num1
        global mathOp
        mathOp = command
        num1=float(e.get())
        num1=sin(radians(num1))
        e.delete(0, END)
        e.insert(0, num1)

    def btnLogg():
        global num1
        global mathOp
        mathOp = command
        num1=float(e.get())
        num1=log(num1, 10)
        e.delete(0, END)
        e.insert(0, num1)


# Buttons ---------------------------------------------

    e = Entry(MainWindow, width=16, font=("Verdana", 20), bd=12)

    btnSin= Button(MainWindow, width=8, text="sin", pady="20", padx="43", command=btnSinn, bg="#FFE873", activebackground="#FFD43B")
    btnLog= Button(MainWindow, width=8, text="log", pady="20", padx="43", command=btnLogg, bg="#FFE873", activebackground="#FFD43B")

    btnProc = Button(MainWindow, width=4, text="%", pady="35", padx="20", bg="#FFE873", activebackground="#FFD43B")
    btnSqrt = Button(MainWindow, width=4, text="√", pady="35", padx="20", command=btnSqroot, bg="#FFE873", activebackground="#FFD43B") 
    btnSqr = Button(MainWindow, width=4, text="x^", pady="35", padx="20", command=btnSqrrd, bg="#FFE873", activebackground="#FFD43B")
    btnClr = Button(MainWindow, width=4, text="C", pady="35", padx="20", command=btnClear, bg="#FFE873", activebackground="#FFD43B")
    btnDiv = Button(MainWindow, width=4, text="/", pady="35", padx="20", command=lambda: btnCommand("/"), bg="#FFE873", activebackground="#FFD43B")
    btnMult = Button(MainWindow, width=4, text="*", pady="35", padx="20", command=lambda: btnCommand("*"), bg="#FFE873", activebackground="#FFD43B")
    btnMinus = Button(MainWindow, width=4, text="-", pady="35", padx="20", command=lambda: btnCommand("-"), bg="#FFE873", activebackground="#FFD43B")
    btnPlus = Button(MainWindow, width=4, text="+", pady="35", padx="20", command=lambda: btnCommand("+"), bg="#FFE873", activebackground="#FFD43B")
    btnEq = Button(MainWindow, width=4, text="=", pady="35", padx="20", command=btnEquals, bg="#4B8BBE", activebackground="#306998")
    btnDot = Button(MainWindow, width=4, text=".", pady="35", padx="20", command=btnDott, activebackground="gray70")

    btn0 = Button(MainWindow, width=4, text="0", pady="35", padx="20", command=lambda: btnClick(0), activebackground="gray70")
    btn1 = Button(MainWindow, width=4, text="1", pady="35", padx="20", command=lambda: btnClick(1), activebackground="gray70")
    btn2 = Button(MainWindow, width=4, text="2", pady="35", padx="20", command=lambda: btnClick(2), activebackground="gray70")
    btn3 = Button(MainWindow, width=4, text="3", pady="35", padx="20", command=lambda: btnClick(3), activebackground="gray70")
    btn4 = Button(MainWindow, width=4, text="4", pady="35", padx="20", command=lambda: btnClick(4), activebackground="gray70")
    btn5 = Button(MainWindow, width=4, text="5", pady="35", padx="20", command=lambda: btnClick(5), activebackground="gray70")
    btn6 = Button(MainWindow, width=4, text="6", pady="35", padx="20", command=lambda: btnClick(6), activebackground="gray70")
    btn7 = Button(MainWindow, width=4, text="7", pady="35", padx="20", command=lambda: btnClick(7), activebackground="gray70")
    btn8 = Button(MainWindow, width=4, text="8", pady="35", padx="20", command=lambda: btnClick(8), activebackground="gray70")
    btn9 = Button(MainWindow, width=4, text="9", pady="35", padx="20", command=lambda: btnClick(9), activebackground="gray70")

# Grid ------------------------------------------------

    e.grid(row=0, column=0, columnspan=4)

    btnSin.grid(row=1, column=0, columnspan=2)
    btnLog.grid(row=1, column=2, columnspan=2)

    btnProc.grid(row=2, column=0)
    btnSqrt.grid(row=2, column=1)
    btnSqr.grid(row=2, column=2)
    btnClr.grid(row=2, column=3)

    btn7.grid(row=3, column=0)
    btn8.grid(row=3, column=1)
    btn9.grid(row=3, column=2)
    btnDiv.grid(row=3, column=3)

    btn4.grid(row=4, column=0)
    btn5.grid(row=4, column=1)
    btn6.grid(row=4, column=2)
    btnMult.grid(row=4, column=3)

    btn1.grid(row=5, column=0)
    btn2.grid(row=5, column=1)
    btn3.grid(row=5, column=2)
    btnMinus.grid(row=5, column=3)

    btn0.grid(row=6, column=0)
    btnDot.grid(row=6, column=1)
    btnEq.grid(row=6, column=2)
    btnPlus.grid(row=6, column=3)


    MainWindow.mainloop()
temp()
