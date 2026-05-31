import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def decide_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

def play(user_choice):
    computer_choice = random.choice(choices)

    user_label.config(text="Your Choice: " + user_choice)
    computer_label.config(text="Computer Choice: " + computer_choice)

    result = decide_winner(user_choice, computer_choice)
    result_label.config(text=result)

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
title_label.pack(pady=10)
user_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
user_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer Choice: ", font=("Arial", 12))
computer_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack(pady=20)
rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)
paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)
root.mainloop()