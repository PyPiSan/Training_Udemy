from tkinter import *

window = Tk()
window.title("Test")
window.minsize(width= 500, height= 500)

# label
label_one = Label(text = "I am Sanjeev", font = ("Arial", 25, "bold"))
label_one.pack()
# Button
def button_clicked():
    # print("I am Sanjeev")
    new_text = input.get()
    label_one.config(text = new_text)

button_one = Button(text = "click", command= button_clicked)
button_one.pack()
# Entry
input = Entry(width=10)
input.pack()
print(input.get())

window.mainloop()