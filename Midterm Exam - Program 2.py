from tkinter import *
window = Tk()

lbl = Label( window, text ="Enter your fullname: ", fg = "red")
lbl.place(x = 80, y = 150)

txtfld = Entry(window, bd = 3, font = ("Arial", 16))
txtfld.place(x = 300, y = 150)

def display ():
    dp = txtfld.get()
    txtfld2.insert(END, str(dp))

btn = Button(window, text = "Click to display your Fullname", fg = "red", command = display  )
btn.place(x = 80, y = 200)

txtfld2 = Entry(window, bd=3, font=("Arial", 16))
txtfld2.place(x = 300, y = 200)


window.geometry("700x400+30+20")
window.title("Midterm in OOP")
window.mainloop()