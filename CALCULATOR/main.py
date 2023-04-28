from tkinter import *
import tkinter.font as font

root = Tk()
numOne = Label(root, text="Enter First Number:", font=("Serif", 11))
numTwo = Label(root, text="Enter Second Number:",font=("Monospace", 11))
enterOne = Entry(root)
enterTwo = Entry(root)


#main function
def add():
	x = int(enterOne.get())
	y = int(enterTwo.get())
	result["text"] = x+y

def sub():
	x = int(enterOne.get())
	y = int(enterTwo.get())
	result["text"] = x-y

def div():
	x = int(enterOne.get())
	y = int(enterTwo.get())
	result["text"] = x/y

def mul():
	x = int(enterOne.get())
	y = int(enterTwo.get())
	result["text"] = x*y


# design
add = Button(root, text="Add", bg ='black', fg= 'white', width=10, command=add )

sub = Button(root, text="Subtract", bg= 'red', fg = 'blue' ,width=10, command=sub)

div = Button(root, text="Divide",bg ='green', fg= 'yellow', width=10, command=div)

mul = Button(root, text="Multiply",bg ='purple', fg= 'pink' ,width=10, command=mul)


result = Label(root, bg = 'pink')

#formation
numOne.grid(row=0, column=0)
enterOne.grid(row=0, column=1)
numTwo.grid(row=1, column=0)
enterTwo.grid(row=1, column=1)
add.grid(row=2, column=0)
sub.grid(row=2, column=1)
div.grid(row=3, column=0)
mul.grid(row=3, column=1),

result.grid(row=4, column=1)

root.mainloop()