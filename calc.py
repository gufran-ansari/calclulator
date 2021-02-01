import tkinter as tk

cal = tk.Tk()
cal.title("Calculator")
variable = tk.StringVar()
operator = ""

def click(number):
    global operator
    operator = operator + str(number)
    variable.set(operator)


def clear():
    global operator
    operator = " "
    variable.set(operator)


def sum():
    global operator
    operator = str(eval(operator))
    variable.set(operator)

button1 = tk.Button(cal, text="1", font=("arial", 20, "bold"), bd=5, padx=10, command=lambda: click(1))
button1.grid(row=3, column=0)

button2 = tk.Button(cal, text="2", font=("arial", 20, "bold"), bd=5, padx=10, command=lambda: click(2))
button2.grid(row=3, column=1)

button3 = tk.Button(cal, text="3", font=("arial", 20, "bold"), bd=5, padx=10, command=lambda: click(3))
button3.grid(row=3, column=2)

button4 = tk.Button(cal, text="4", font=("arial", 20, "bold"), bd=5, padx=10, command=lambda: click(4))
button4.grid(row=2, column=0)

button5 = tk.Button(cal, text="5", font=("arial", 20, "bold"), bd=5, padx=10, command=lambda: click(5))
button5.grid(row=2, column=1)

button6 = tk.Button(cal, text="6", font=("arial", 20, "bold"), bd=5, padx=10, command=lambda: click(6))
button6.grid(row=2, column=2)

button7 = tk.Button(cal, text="7", font=("arial", 20, "bold"), bd=5, padx=10, command=lambda: click(7))
button7.grid(row=1, column=0)

button8 = tk.Button(cal, text="8", font=("arial", 20, "bold"), bd=5, padx=10, command=lambda: click(8))
button8.grid(row=1, column=1)

button9 = tk.Button(cal, text="9", font=("arial", 20, "bold"), bd=5, padx=10, command=lambda: click(9))
button9.grid(row=1, column=2)

button0 = tk.Button(cal, text="0", font=("arial", 20, "bold"), bd=5, padx=10, command=lambda: click(0))
button0.grid(row=4, column=0)

buttonPoint = tk.Button(cal, text=" .", font=("arial", 20, "bold"), bd=5, padx=10, command=lambda: click("."))
buttonPoint.grid(row=4, column=1)

buttonClear = tk.Button(cal, text="C", font=("arial", 20, "bold"), bd=5, padx=10, command=clear())
buttonClear.grid(row=4, column=2)

buttonAdd = tk.Button(cal, text="+", font=("arial", 18, "bold"), bd=5, padx=20, command=lambda: click("+"))
buttonAdd.grid(row=1, column=4)

buttonMinus = tk.Button(cal, text="-", font=("arial", 20, "bold"), bd=5, padx=20, command=lambda: click("-"))
buttonMinus.grid(row=2, column=4)

buttonDivide = tk.Button(cal, text="/", font=("arial", 20, "bold"), bd=5, padx=20, command=lambda: click("/"))
buttonDivide.grid(row=3, column=4)

buttonMultiply = tk.Button(cal, text="*", font=("arial", 18, "bold"), bd=5, padx=20, command=lambda: click("*"))
buttonMultiply.grid(row=4, column=4)

buttonEqual = tk.Button(cal, text="=", font=("arial", 20, "bold"), bd=5, padx=100, command=sum)
buttonEqual.grid(row=5, column=5)

display = tk.Button(cal, font=("arial", 20, "bold"), bd=30, textvariable=variable, justify="left")
display.grid(columnspan=5)

cal.mainloop()
