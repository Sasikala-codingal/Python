import tkinter as tk
from tkinter import messagebox

def convert_to_cm():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text="Length in cm: " + str(cm))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")


root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("300x200")

label = tk.Label(root, text="Enter Length in Inches:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_to_cm)
convert_button.pack(pady=10)


result_label = tk.Label(root, text="Length in cm:")
result_label.pack(pady=5)

root.mainloop()