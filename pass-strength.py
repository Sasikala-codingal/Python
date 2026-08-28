from tkinter import *

def check_strength():
    password = password_entry.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Please enter a password", foreground="black")
    elif length < 6:
        result_label.config(text="Password Strength: Weak", foreground="red")
    elif length < 10:
        result_label.config(text="Password Strength: Medium", foreground="orange")
    else:
        result_label.config(text="Password Strength: Strong", foreground="green")


root = Tk()
root.title("Password Strength Checker")
root.geometry("350x200")

title_label = Label(root, text="Enter Password:", font=("Arial", 12))
title_label.pack(pady=10)

password_entry = Entry(root, width=30, show="*")
password_entry.pack(pady=5)

check_button = Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=10)


result_label = Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)


root.mainloop()