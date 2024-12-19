from tkinter import *
from datetime import date

root = Tk()
root.title("Getting started with widgets")
root.geometry("400x300")
lbl = Label(root,text="Lets multiply two numbers", fg = "white", bg = "#072F5F", height = 2,width = 300)
lbl.pack(pady=10)

n1_lbl = Label(root,text = "Enter Number 1", bg = "#3895D3", fg="white")
n1_lbl.pack()

n1_entry = Entry(root, width = 20)
n1_entry.pack(pady=5)

n2_lbl = Label(root,text = "Enter Number 2", bg = "#3895D3")
n2_lbl.pack()


n2_entry = Entry(root, width = 20)
n2_entry.pack(pady=5)

def multiply():

    text_box.delete(1.0,END)

    try:
        n1 = int(n1_entry.get())
        n2 = int(n2_entry.get())
        product = n1 * n2

        text_box.insert(END, "heres the final product... \n")
        text_box.insert(END,f"{n1}x{n2} = {product}\n")

    except ValueError:
        text_box.insert(END, "please enter valid numbers")
        
text_box = Text(root,height = 4,width = 40,wrap = WORD)
text_box.pack(pady = 10)

btn = Button(root,text = "calculate", command = multiply, height = 1, bg = "#1261A0", fg='white')
btn.pack()
root.mainloop()


