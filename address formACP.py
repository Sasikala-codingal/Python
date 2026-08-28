import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def submit_address():
    # Retrieve data from all fields using .get()
    address_data = {
        "Full Name": entry_name.get(),
        "Address Line 1": entry_line1.get(),
        "Address Line 2": entry_line2.get(),
        "City": entry_city.get(),
        "State/Province": entry_state.get(),
        "Postal/ZIP Code": entry_zip.get(),
        "Country": combo_country.get()
    }
    
    # Simple validation check: ensure required fields are not empty
    required_fields = ["Full Name", "Address Line 1", "City", "Postal/ZIP Code"]
    missing = [field for field in required_fields if not address_data[field].strip()]
    
    if missing:
        messagebox.showwarning("Missing Data", f"Please fill out required fields:\n{', '.join(missing)}")
        return
        
    # Successfully retrieved data
    summary = "\n".join([f"{key}: {val}" for key, val in address_data.items() if val])
    messagebox.showinfo("Address Submitted", f"Successfully Saved:\n\n{summary}")
    
    # Optional: Clear the form after submission
    clear_form()

def clear_form():
    entry_name.delete(0, tk.END)
    entry_line1.delete(0, tk.END)
    entry_line2.delete(0, tk.END)
    entry_city.delete(0, tk.END)
    entry_state.delete(0, tk.END)
    entry_zip.delete(0, tk.END)
    combo_country.set("")

# 1. Main Window Setup
root = tk.Tk()
root.title("Address Entry Form")
root.geometry("450x400")
root.resizable(False, False)

# 2. Main Container (Frame with padding)
main_frame = ttk.Frame(root, padding="15")
main_frame.pack(fill=tk.BOTH, expand=True)

# 3. LabelFrame for Visual Grouping
form_frame = ttk.LabelFrame(main_frame, text=" Postal Address Details ", padding="15")
form_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

# Configure layout weights for responsive column stretching
form_frame.columnconfigure(1, weight=1)

# 4. Form Fields Layout (Labels & Entry Widgets)
# Row 0: Full Name
ttk.Label(form_frame, text="Full Name: *").grid(row=0, column=0, sticky=tk.W, pady=5)
entry_name = ttk.Entry(form_frame)
entry_name.grid(row=0, column=1, columnspan=2, sticky=tk.EW, pady=5)

# Row 1: Address Line 1
ttk.Label(form_frame, text="Address Line 1: *").grid(row=1, column=0, sticky=tk.W, pady=5)
entry_line1 = ttk.Entry(form_frame)
entry_line1.grid(row=1, column=1, columnspan=2, sticky=tk.EW, pady=5)

# Row 2: Address Line 2
ttk.Label(form_frame, text="Address Line 2:").grid(row=2, column=0, sticky=tk.W, pady=5)
entry_line2 = ttk.Entry(form_frame)
entry_line2.grid(row=2, column=1, columnspan=2, sticky=tk.EW, pady=5)

# Row 3: City & State (Side by side)
ttk.Label(form_frame, text="City: *").grid(row=3, column=0, sticky=tk.W, pady=5)
entry_city = ttk.Entry(form_frame, width=15)
entry_city.grid(row=3, column=1, sticky=tk.EW, padx=(0, 5), pady=5)

ttk.Label(form_frame, text="State/Prov:").grid(row=3, column=2, sticky=tk.W, padx=(5, 0), pady=5)
entry_state = ttk.Entry(form_frame, width=12)
entry_state.grid(row=3, column=3, sticky=tk.EW, pady=5)

# Row 4: ZIP Code & Country (Side by side)
ttk.Label(form_frame, text="ZIP/Postal: *").grid(row=4, column=0, sticky=tk.W, pady=5)
entry_zip = ttk.Entry(form_frame, width=15)
entry_zip.grid(row=4, column=1, sticky=tk.EW, padx=(0, 5), pady=5)

ttk.Label(form_frame, text="Country:").grid(row=4, column=2, sticky=tk.W, padx=(5, 0), pady=5)
combo_country = ttk.Combobox(form_frame, values=["United States", "Canada", "United Kingdom", "Australia", "India"], width=12)
combo_country.grid(row=4, column=3, sticky=tk.EW, pady=5)

# 5. Bottom Action Buttons Panel
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill=tk.X)

btn_clear = ttk.Button(button_frame, text="Clear", command=clear_form)
btn_clear.pack(side=tk.LEFT, padx=5)

btn_submit = ttk.Button(button_frame, text="Submit Address", command=submit_address)
btn_submit.pack(side=tk.RIGHT, padx=5)

# 6. Start Application Loop
root.mainloop()
