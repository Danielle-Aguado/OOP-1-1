from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry("400x300+20+10")

class MyWindow:
    def __init__(self,window):
        self.lbl1 = Label(window,text= "Simple Calculator")
        self.lbl1.grid(row=0, columnspan=6, pady = 10)

        self.lbl2 = Label(window, text = "Enter the 1st Number:")
        self.lbl2.grid(row=2,column=1)
        self.txt2 = Entry(window,bd=3)
        self.txt2.grid(row=2,column= 2)
        self.lbl3 = Label(window,text="Enter the 2nd Number:")
        self.lbl3.grid(row=3,column=1)
        self.txt3 = Entry(window,bd=3)
        self.txt3.grid(row=3,column=2)

        self.btn1 = Button(window, text="Addition", command=self.add)
        self.btn1.grid(row=5, column=0, padx=10)
        self.btn2 = Button(window, text="Subtraction", command=self.sub)
        self.btn2.grid(row=5, column=1, padx=10)
        self.btn3 = Button(window, text="Multiplication", command=self.mul)
        self.btn3.grid(row=5, column=2, pady = 10)
        self.btn4 = Button(window, text="Division", command=self.div)
        self.btn4.grid(row=5, column=3, padx=10)
        self.btn5 = Button(window, text="Clear", fg="red",command=self.btnclear)
        self.btn5.grid(row=8, column=2, pady= 5)

        self.lbl4 = Label(window, text="Result: ")
        self.lbl4.grid(row=7, column=1)
        self.txt4 = Entry(window,bd= 3, state="readonly")
        self.txt4.grid(row=7, column=2)

    def add(self):
        self.txt4.configure(state="normal")
        self.txt4.delete('0', END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1 + num2
        self.txt4.insert(END, str(answer))
        self.txt4.configure(state="disabled")
        return

    def sub(self):
        self.txt4.configure(state="normal")
        self.txt4.delete('0', END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1 - num2
        self.txt4.insert(END, str(answer))
        self.txt4.configure(state="disabled")
        return

    def mul(self):
        self.txt4.configure(state="normal")
        self.txt4.delete('0', END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1 * num2
        self.txt4.insert(END, str(answer))
        self.txt4.configure(state="disabled")
        return

    def div(self):
        self.txt4.configure(state="normal")
        self.txt4.delete('0', END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1 / num2
        self.txt4.insert(END, str(answer))
        self.txt4.configure(state="disabled")
        return

    def btnclear(self):
        self.txt4.configure(state="normal")
        self.txt4.delete(0,END)
        self.txt4.configure(state="disabled")
        self.txt2.delete(0,END)
        self.txt3.delete(0,END)
        return



mywin = MyWindow(window)

window.mainloop()
