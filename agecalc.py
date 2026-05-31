import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        year = int(entry_year.get())
        today = date.today()

        
        if year > today.year:
            messagebox.showerror("Invalid Year", "Year cannot be in the future.")
            return

        age = today.year - year
        result_label.config(text=f"Present Age: {age} years")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric year.")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("350x250")
root.resizable(False, False)

title_label = tk.Label(root, text="Age Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

tk.Label(root, text="Enter Birth Year:").pack()
entry_year = tk.Entry(root)
entry_year.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()