import random  # Import the random module to generate a random number

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Initialize the variable for the user's guess
user_guess = 0

# Use a while loop to repeatedly prompt the user until they guess the correct number
while user_guess != secret_number:
    # Prompt the user to enter a guess
    user_guess = int(input("Guess the number between 1 and 10: "))

    # Check if the guess is correct
    if user_guess == secret_number:
        print("Congratulations! You guessed the correct number.")
    else:
        # Provide feedback to the user based on their guess
        if user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# End of the script



