from tkinter import *

window = Tk()
window.title("Calculator")

keys = list(range(10)) + ["+","-","*","/"] #List of all buttons except Clear and =. I created them seperately at the end of the code.

def buttonTrigger(value): #Number and operator button functions.
    entryText.set(entryText.get() + value)

def clearLabel(): #Clear button function.
    entryText.set("")

def evaluate(): #= button function.
    try:
        entryText.set(eval(entryText.get()))
    except SyntaxError:
        entryText.set("Wrong Syntax!!!")

entryText = StringVar()
hesapEkrani = Entry(window, textvariable=entryText, state="readonly")
hesapEkrani.grid(row=0, columnspan=4,pady=10)

for i in range(len(keys)): #Number and operator buttons.
    j = keys[i]
    buton = Button(window, text=str(j), command=lambda v=str(j): buttonTrigger(v), width=5) #I don't know how lambda works. ChatGPT did that. 💀
    buton.grid(row=1 + i // 4, column=i % 4, padx=5, pady=5)

clearButton = Button(window,text="C",command=clearLabel,width=5) #Clear button
clearButton.grid(row=4,column=2,padx=5,pady=5)

calculateButton = Button(window,text="=",command=evaluate,width=5) #= button
calculateButton.grid(row=4,column=3,padx=5,pady=5)

window.mainloop()