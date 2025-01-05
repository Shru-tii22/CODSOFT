import tkinter as tk
import random

def play(user_choice):
    options = ['Rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie"
    elif (user_choice == "Rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "Rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "Congratulations, you win!!"
    else:
        result = "You lose!!"

    result_label.config(text=f"You choose: {user_choice}\nComputer chooses: {computer_choice}\n{result}")


root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")


label = tk.Label(root, text="Choose your option", font=("arial", 16))
label.pack(pady=20)


stone_button = tk.Button(root, text="Rock", font=("arial", 14), command=lambda: play("Rock"))
stone_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", font=("arial", 14), command=lambda: play("paper"))
paper_button.pack(pady=10)

scissor_button = tk.Button(root, text="Scissors", font=("arial", 14), command=lambda: play("scissors"))
scissor_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("arial", 14), fg="#213555")
result_label.pack(pady=20)

root.mainloop()
