import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    # Loop until the user guesses correctly
    while True:
        guess = input("Enter your guess: ")

        try:
            guess = int(guess)  # Convert the guess to an integer
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break  # Exit the loop when the correct number is guessed
        except ValueError:
            print("Please enter a valid number.")

# Run the guessing game
if __name__ == "__main__":
    guessing_game()
