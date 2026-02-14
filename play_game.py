import random
def play_game():
    # 1. Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # 2. Loop until the user guesses the number
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            # 3. Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break # Exit the loop
        except ValueError:
            print("Invalid input. Please enter a number.")
if __name__ ==  "__main__":
    play_game()
