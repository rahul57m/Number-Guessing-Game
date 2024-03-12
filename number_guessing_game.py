import random

def generate_random_number():
    """Generate a random number between 1 and 100."""
    return random.randint(1, 100)

def get_user_guess():
    """Get user input for a guessed number."""
    try:
        guess = int(input("Enter your guess (between 1 and 100): "))
        return guess
    except ValueError:
        print("Invalid in1put. Please enter a number.")
        return get_user_guess()

def play_game():
    """Main function to play the number guessing game."""
    print("Welcome to the Number Guessing Game!")
    secret_number = generate_random_number()
    attempts = 0

    while True:
        user_guess = get_user_guess()
        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    play_game()
