from tkinter import *


# define the GUI application



window = Tk()

my_frame = Frame()
my_frame.pack()

labeltx1 = Label(my_frame, text ="top bar", bg="red")

labeltx1.pack(fill=X)

label_left = Label(my_frame, text="left", bg="yellow")
label_left.pack(side=LEFT)


label_mid = Label(my_frame, text="middle", bg="green")
label_mid.pack(side=LEFT)


label_right = Label(my_frame, text="right", bg="blue")
label_right.pack()




window.mainloop()
