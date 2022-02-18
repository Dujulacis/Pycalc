from tkinter import*
def temp():
    MainWindow=Tk()
    MainWindow.title("Pycalc")
    btn0=Button(MainWindow, text="0", padx="40", pady="20")
    btn1=Button(MainWindow, text="1", padx="40", pady="20")
    btn2=Button(MainWindow, text="2", padx="40", pady="20")
    btn3=Button(MainWindow, text="3", padx="40", pady="20")
    btn4=Button(MainWindow, text="4", padx="40", pady="20")
    btn5=Button(MainWindow, text="5", padx="40", pady="20")
    btn6=Button(MainWindow, text="6", padx="40", pady="20")
    btn7=Button(MainWindow, text="7", padx="40", pady="20")
    btn8=Button(MainWindow, text="8", padx="40", pady="20")
    btn9=Button(MainWindow, text="9", padx="40", pady="20")
    
    btn7.grid(row=1, column=0)
    btn8.grid(row=1, column=1)
    btn9.grid(row=1, column=2)

    btn5.grid(row=2, column=1)
    btn6.grid(row=2, column=2)

    btn1.grid(row=3, column=0)
    btn2.grid(row=3, column=1)
    btn3.grid(row=3, column=2)

    btn0.grid(row=4, column=0)
    MainWindow.mainloop()
temp()
