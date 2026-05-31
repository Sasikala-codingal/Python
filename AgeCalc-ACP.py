import tkinter as tk
from datetime import date
import tkinter.messagebox as messagebox

# Function to calculate age
def calculate_age():
    try:
        birth_year = int(year_entry.get())
        current_year = date.today().year
        age = current_year - birth_year
        if age < 0:
             messagebox.showerror("Error", "Birth year cannot be in the future")
        else:
            messagebox.showinfo("Result", f"You are approximately {age} years old.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid year")

# Create the main application window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x150")

# Add a label
label = tk.Label(root, text="Enter your birth year:", font=("Arial", 12))
label.pack(pady=10)

# Add an entry box for the year
year_entry = tk.Entry(root, width=10)
year_entry.pack(pady=5)

# Add a calculate button
calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=10)

# Run the application
root.mainloop()
