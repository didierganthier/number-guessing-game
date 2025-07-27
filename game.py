import random

def show_welcome_message():
    print("🎉 Welcome to the Number Guessing Game! 🎉")
    name = input("What's your name? ")
    print(f"Hello, {name}! Let's play a game.")
    print("I'm thinking of a number between 1 and 100.")
    print("Your task is to guess the number in as few attempts as possible.")
    print("Choose a difficulty level to determine how many chances you get.")
    print("Good luck!\n")

def select_difficulty():
    print("Please select a difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (5 attempts)")
    print("3. Hard (3 attempts)")

    while True:
        choice = input ("Enter your choice (1 / 2 / 3): ").strip()

        if choice == '1':
            print("🟢 You selected Easy mode. You have 10 attempts.\n")
            return 10
        elif choice == '2':
            print("🟡 You selected Medium mode. You have 5 attempts.\n")
            return 5
        elif choice == '3':
            print("🔴 You selected Hard mode. You have 3 attempts.\n")
            return 3
        else:
            print("❌ Invalid choice. Please type 1, 2, or 3.")

def generate_secret_number():
    return random.randint(1, 100)

def play_round(secret_number, max_attempts):
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Enter your guess ({max_attempts - attempts} attempts left): "))
        except ValueError:
            print("❌ Please enter a valid integer.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"🎉 Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
            return attempts
        elif guess < secret_number:
            print("🔽 Too low! Try again.")
        else:
            print("🔼 Too high! Try again.")

    print(f"❌ Sorry, you've used all your attempts. The secret number was {secret_number}.")
    print(f"Thanks for playing! 🎮")
    return None

def play_game():
    show_welcome_message()
    max_attempts = select_difficulty()
    secret_number = generate_secret_number()
    return play_round(secret_number, max_attempts)

def main():
    best_score = float('inf')
    while True:
        attempts = play_game()
        if attempts is not None and attempts < best_score:
            best_score = attempts
            print(f"🏆 New best score: {best_score} attempts!")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye! 👋")
            if best_score != float('inf'):
                print(f"Your best score was {best_score} attempts.")
            break

if __name__ == "__main__":
    main()
