import random

print("Welcome to the Number Guessing Game! 🎲")
print("I'm thinking of a number between 1 and 20...")

# generate a random number
secret_number = random.randint(1, 20)

# give the player 5 chances
for i in range(5):
    guess = int(input(f"Attempt {i+1}/5: Enter your guess: "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
else:
    print(f"😢 Sorry, you're out of tries. The number was {secret_number}.")
