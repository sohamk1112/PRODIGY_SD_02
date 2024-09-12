import tkinter as tk
import random
from tkinter import messagebox

class GuessingGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        # Create the GUI elements
        self.label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 14))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, width=10, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(root, text="Submit Guess", font=("Arial", 12), command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.", fg="red")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.", fg="red")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number {self.number_to_guess} in {self.attempts} attempts!")
                self.reset_game()

        except ValueError:
            self.result_label.config(text="Please enter a valid number.", fg="red")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)

# Run the GUI guessing game
if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameApp(root)
    root.mainloop()
