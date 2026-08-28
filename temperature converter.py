import tkinter as tk
from tkinter import messagebox

# Conversion Logic
def convert_temperature():
    try:
        input_value = float(entry_temp.get())
        selected_mode = conversion_mode.get()
        
        if selected_mode == "C_to_F":
            # Celsius to Fahrenheit formula: (C * 9/5) + 32
            result = (input_value * 9/5) + 32
            label_result.config(text=f"{result:.2f} °F", fg="#1b5e20")
        
        elif selected_mode == "F_to_C":
            # Fahrenheit to Celsius formula: (F - 32) * 5/9
            result = (input_value - 32) * 5/9
            label_result.config(text=f"{result:.2f} °C", fg="#1b5e20")
            
    except ValueError:
        # Displays an error if the user inputs text instead of a number
        messagebox.showerror("Invalid Input", "Please enter a valid numerical temperature.")
        label_result.config(text="Error", fg="#d32f2f")

# Main Window Setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x250")
root.config(bg="#f5f5f5")
root.resizable(False, False)

# App Title
label_title = tk.Label(root, text="Temperature Converter", font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#333333")
label_title.pack(pady=10)

# Entry Field for Temperature
entry_temp = tk.Entry(root, font=("Arial", 14), width=10, justify="center")
entry_temp.pack(pady=5)
entry_temp.insert(0, "0")  # Default placeholder value

# Variable to track chosen conversion direction
conversion_mode = tk.StringVar(value="C_to_F")

# Radio Buttons for Selection
frame_radio = tk.Frame(root, bg="#f5f5f5")
frame_radio.pack(pady=5)

rb_c_to_f = tk.Radiobutton(frame_radio, text="Celsius to Fahrenheit", variable=conversion_mode, 
                           value="C_to_F", bg="#f5f5f5", font=("Arial", 10))
rb_c_to_f.pack(anchor="w")

rb_f_to_c = tk.Radiobutton(frame_radio, text="Fahrenheit to Celsius", variable=conversion_mode, 
                           value="F_to_C", bg="#f5f5f5", font=("Arial", 10))
rb_f_to_c.pack(anchor="w")

# Convert Button
btn_convert = tk.Button(root, text="Convert", font=("Arial", 11, "bold"), bg="#2196F3", fg="white", 
                        padx=10, pady=5, command=convert_temperature)
btn_convert.pack(pady=10)

# Result Label
label_result = tk.Label(root, text="-- °F", font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#555555")
label_result.pack(pady=5)

# Keep the window running
root.mainloop()
