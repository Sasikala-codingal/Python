import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        p = float(entry_p.get())
        t = float(entry_t.get())
        r = float(entry_r.get())

       
        si = (p * t * r) / 100
        ci = p * ((1 + r/100) ** t) - p

        result_si.config(text="Simple Interest: " + str(round(si, 2)))
        result_ci.config(text="Compound Interest: " + str(round(ci, 2)))

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


root = tk.Tk()
root.title("Interest Calculator")
root.geometry("550x550")

tk.Label(root, text="Principal Amount:").pack()
entry_p = tk.Entry(root)
entry_p.pack()

tk.Label(root, text="Time (years):").pack()
entry_t = tk.Entry(root)
entry_t.pack()

tk.Label(root, text="Rate of Interest (%):").pack()
entry_r = tk.Entry(root)
entry_r.pack()

tk.Button(root, text="Calculate", command=calculate_interest).pack(pady=10)

result_si = tk.Label(root, text="Simple Interest: ")
result_si.pack()

result_ci = tk.Label(root, text="Compound Interest: ")
result_ci.pack()

root.mainloop()