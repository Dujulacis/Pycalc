import numbers
from tkinter import*

def temp():
    MainWindow = Tk()
    MainWindow.title("Pycalc")

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
        num1 = int(e.get())
        e.delete(0, END)
        return 0

    def btnEquals():
        num2 = int(e.get())
        result=0
        if mathOp=="+":
            result=num1+num2
        elif mathOp=="-":
            result=num1-num2
        elif mathOp=="*":
            result=num1*num2
        elif mathOp=="/":
            result=num1/num2
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
        
# Buttons ---------------------------------------------

    e = Entry(MainWindow, width=16, font=("Arial Black", 20))
    btntemp = Button(MainWindow, width=4, text="temp", pady="35", padx="20")
    btnClr = Button(MainWindow, width=4, text="C", pady="35", padx="20", command=btnClear)
    btnMinus = Button(MainWindow, width=4, text="-", pady="35", padx="20", command=lambda: btnCommand("-"))
    btnMult = Button(MainWindow, width=4, text="*", pady="35", padx="20", command=lambda: btnCommand("*"))
    btnDiv = Button(MainWindow, width=4, text="/", pady="35", padx="20", command=lambda: btnCommand("/"))
    btnPlus = Button(MainWindow, width=4, text="+", pady="35", padx="20", command=lambda: btnCommand("+"))
    btnEq = Button(MainWindow, width=4, text="=", pady="35", padx="20", command=btnEquals)
    btnDot = Button(MainWindow, width=4, text=".", pady="35", padx="20")
    btn0 = Button(MainWindow, width=4, text="0", pady="35", padx="20", command=lambda: btnClick(0))
    btn1 = Button(MainWindow, width=4, text="1", pady="35", padx="20", command=lambda: btnClick(1))
    btn2 = Button(MainWindow, width=4, text="2", pady="35", padx="20", command=lambda: btnClick(2))
    btn3 = Button(MainWindow, width=4, text="3", pady="35", padx="20", command=lambda: btnClick(3))
    btn4 = Button(MainWindow, width=4, text="4", pady="35", padx="20", command=lambda: btnClick(4))
    btn5 = Button(MainWindow, width=4, text="5", pady="35", padx="20", command=lambda: btnClick(5))
    btn6 = Button(MainWindow, width=4, text="6", pady="35", padx="20", command=lambda: btnClick(6))
    btn7 = Button(MainWindow, width=4, text="7", pady="35", padx="20", command=lambda: btnClick(7))
    btn8 = Button(MainWindow, width=4, text="8", pady="35", padx="20", command=lambda: btnClick(8))
    btn9 = Button(MainWindow, width=4, text="9", pady="35", padx="20", command=lambda: btnClick(9))

# Grid ------------------------------------------------

    e.grid(row=0, column=0, columnspan=4)

    btntemp.grid(row=1, column=0,)
    btnClr.grid(row=1, column=3)

    btn7.grid(row=2, column=0)
    btn8.grid(row=2, column=1)
    btn9.grid(row=2, column=2)
    btnDiv.grid(row=2, column=3)

    btn4.grid(row=3, column=0)
    btn5.grid(row=3, column=1)
    btn6.grid(row=3, column=2)
    btnMult.grid(row=3, column=3)

    btn1.grid(row=4, column=0)
    btn2.grid(row=4, column=1)
    btn3.grid(row=4, column=2)
    btnMinus.grid(row=4, column=3)

    btn0.grid(row=5, column=0)
    btnDot.grid(row=5, column=1)
    btnEq.grid(row=5, column=2)
    btnPlus.grid(row=5, column=3, rowspan=2)


    MainWindow.mainloop()
temp()
