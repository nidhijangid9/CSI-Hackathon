from tkinter import *
from tkinter import messagebox
import healthy
import weight_loss
import weight_gain

root = Tk()
root.geometry("400x400")
root.title("FITNESS PAL")

# Function to call healthy function
def healthyFunc():
    age = e1.get()
    weight = e2.get()
    height = e3.get()
    healthy.Healthy(age, weight, height)

# Function to call weight loss function
def weightLossFunc():
    age = e1.get()
    weight = e2.get()
    height = e3.get()
    weight_loss.WeightLoss(age, weight, height)

# Function to call weight gain function
def weightGainFunc():
    age = e1.get()
    weight = e2.get()
    height = e3.get()
    weight_gain.WeightGain(age, weight, height)

# Labels and entry widgets
l1 = Label(root, text="Age")
l2 = Label(root, text="Weight")
l3 = Label(root, text="Height")
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)

# Placing labels and entry widgets on the grid
l1.grid(row=0)
l2.grid(row=1)
l3.grid(row=2)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

# Buttons to call respective functions
b1 = Button(root, text="Get Healthy", command=healthyFunc)
b1.grid(row=4, column=0)
b2 = Button(root, text="Lose Weight", command=weightLossFunc)
b2.grid(row=4, column=1)
b3 = Button(root, text="Gain Weight", command=weightGainFunc)
b3.grid(row=4, column=2)

root.mainloop()
