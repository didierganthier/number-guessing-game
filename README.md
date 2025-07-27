# Number Guessing Game

🎉 **Welcome to the Number Guessing Game!** 🎉

A fun and interactive Python game where you try to guess a randomly chosen number between 1 and 100. Challenge yourself by selecting different difficulty levels and aim for your best score!

## Project Links

- **Problem Statement:** [ROADMAP Project Page](https://roadmap.sh/projects/number-guessing-game)
- **Solution Repository:** [GitHub - didierganthier/number-guessing-game](https://github.com/didierganthier/number-guessing-game)

## Features

- **Difficulty Levels:** Easy (10 attempts), Medium (5 attempts), Hard (3 attempts)
- **Personalized Welcome:** Enter your name for a custom greeting
- **Best Score Tracking:** Try to beat your previous best!
- **Input Validation:** Handles invalid inputs gracefully
- **Replay Option:** Play as many rounds as you like

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Running the Game

1. Clone or download this repository.
2. Open a terminal and navigate to the project directory.
3. Run the game:

    ```bash
    python number_guessing_game.py
    ```

### How to Play

1. Enter your name when prompted.
2. Select a difficulty level:
    - **Easy:** 10 attempts
    - **Medium:** 5 attempts
    - **Hard:** 3 attempts
3. Try to guess the secret number between 1 and 100.
4. After each guess, you'll receive feedback:
    - 🔽 Too low
    - 🔼 Too high
    - 🎉 Correct!
5. Your best score is tracked across rounds.
6. Choose to play again or exit.

## Example Gameplay

```
🎉 Welcome to the Number Guessing Game! 🎉
What's your name? Alice
Hello, Alice! Let's play a game.
I'm thinking of a number between 1 and 100.
Your task is to guess the number in as few attempts as possible.
Choose a difficulty level to determine how many chances you get.
Good luck!

Please select a difficulty level:
1. Easy (10 attempts)
2. Medium (5 attempts)
3. Hard (3 attempts)
Enter your choice (1 / 2 / 3): 2
🟡 You selected Medium mode. You have 5 attempts.

Enter your guess (5 attempts left): 50
🔼 Too high! Try again.
...
```

## Code Overview

- `show_welcome_message()`: Greets the player and explains the rules.
- `select_difficulty()`: Lets the player choose the difficulty.
- `generate_secret_number()`: Picks a random number between 1 and 100.
- `play_round()`: Handles the guessing logic and feedback.
- `play_game()`: Runs a single game session.
- `main()`: Manages replay and best score tracking.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

## Author

Created by Didier Ganthier.

---
Enjoy the game and happy guessing! 🎮