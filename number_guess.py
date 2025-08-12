import random

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 20...")

# Random number generate karo
secret_number = random.randint(1, 20)
attempts = 0

while True:
    guess = input("Enter your guess: ")

    # Number check karo valid hai ya nahi
    if not guess.isdigit():
        print("❌ Please enter a valid number!")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("📉 Too low! Try again.")
    elif guess > secret_number:
        print("📈 Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed the number in {attempts} tries.")
        break