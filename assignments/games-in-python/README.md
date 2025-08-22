# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman game in Python to practice string manipulation, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️	Hangman Game Logic

#### Description
Create a Hangman game where the player tries to guess a hidden word by suggesting letters, with a limited number of incorrect guesses allowed.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Display the current progress with underscores for unguessed letters (e.g., `_ _ a _ _`)
- Accept single-letter guesses from the user
- Track and display the number of incorrect guesses remaining
- End the game when the word is fully guessed or attempts run out
- Show a win or lose message at the end

**Example:**
```plaintext
Word: _ _ _ _ _
Guess a letter: a
Incorrect! Attempts left: 5
Word: _ a _ _ _
Guess a letter: t
Correct!
...
Congratulations, you won!
```

### 🛠️	Replay and User Experience

#### Description
Enhance your Hangman game to allow the player to play multiple rounds and improve the user interface.

#### Requirements
Completed program should:

- Ask the player if they want to play again after each game
- Reset the game state for each new round
- Clearly display instructions and feedback for each guess
- Handle invalid input gracefully (e.g., non-single letter inputs, empty guesses)
