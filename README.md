 🎮 Rock-Paper-Scissors Game

A clean, beginner-friendly command-line Rock-Paper-Scissors game built in Python.
Created as part of the "CodSoft Python Internship – Task 4"

---

 📌 Project Description

This project is an interactive terminal-based Rock-Paper-Scissors game where the
player competes against the computer. The computer's choice is generated randomly,
and the game keeps track of scores across multiple rounds until the player decides
to exit. The code follows PEP 8 standards, is fully modular using functions, and
handles all invalid inputs and exceptions gracefully so the app never crashes.

---

 ✨ Features

- Welcome banner and clear on-screen game rules
- Numbered menu for Rock / Paper / Scissors / Exit
- Random computer choice using the `random` module
- Automatic winner determination each round
- Live scoreboard: Player Score, Computer Score, Draws, Total Rounds
- Replay prompt after every round (`y/n`)
- Final game summary shown on exit
- Full input validation (empty input, invalid menu choice, invalid y/n)
- Exception handling for `KeyboardInterrupt` and unexpected errors
- Single-file, dependency-free implementation

---

 🛠️ Technologies Used

- Language: Python 3
- Modules: `random` (built-in, no external libraries required)
- Interface: Command-Line Interface (CLI)

---

 📂 Project Structure

```
RockPaperScissors/
├── main.py        # Complete game source code
└── README.md       # Project documentation
```

*(No `requirements.txt` is needed since only Python's built-in `random` module is used.)*

---

 ⚙️ Installation

1. Make sure **Python 3** is installed on your system.
   ```bash
   python3 --version
   ```
2. Clone or download this repository.
   ```bash
   git clone https://github.com/<your-username>/RockPaperScissors.git
   cd RockPaperScissors
   ```

---

 ▶️ How to Run

Run the game using the following command in your terminal:

```bash
python3 main.py
```

Then follow the on-screen menu to play.

---

 🧾 Sample Input

```
Enter your choice (1-4): 1
Do you want to play again? (y/n): y
Enter your choice (1-4): 3
Do you want to play again? (y/n): n
```

---

 🖥️ Sample Output

```
==================================================
      ROCK - PAPER - SCISSORS GAME
      CodSoft Python Internship - Task 4
==================================================

GAME RULES:
  1. Rock crushes Scissors
  2. Scissors cuts Paper
  3. Paper covers Rock
  4. Same choice by both players results in a Draw
--------------------------------------------------

Make your choice:
  1. Rock
  2. Paper
  3. Scissors
  4. Exit Game
Enter your choice (1-4): 1

You chose   : Rock
Computer chose: Scissors
>> You WIN this round!
--------------------------------------------------
SCOREBOARD
  Player Score   : 1
  Computer Score : 0
  Draws          : 0
  Total Rounds   : 1
--------------------------------------------------

Do you want to play again? (y/n): n

==================================================
             FINAL GAME SUMMARY
==================================================
  Total Rounds Played : 1
  Player Score        : 1
  Computer Score      : 0
  Draws               : 0

  RESULT: Congratulations! You won the game! 🎉
==================================================
Thank you for playing! Goodbye.
```

---

 🧠 Algorithm

1. Display the welcome banner and game rules.
2. Loop until the player exits:
   1. Show the menu and get the player's validated choice.
   2. If the player selects "Exit", break out of the loop.
   3. Generate a random choice for the computer.
   4. Compare both choices using the winning rules:
      - Rock beats Scissors
      - Scissors beats Paper
      - Paper beats Rock
      - Equal choices result in a Draw
   5. Update the score (Player / Computer / Draws).
   6. Display the round result and scoreboard.
   7. Ask the player if they want to continue.
3. Display the final score summary and exit gracefully.

---

🚀 Future Enhancements

- Add a Rock-Paper-Scissors-Lizard-Spock variant
- Add difficulty levels with a smarter computer AI
- Add a GUI version using Tkinter or PyQt
- Store game history and statistics in a file or database
- Add multiplayer mode (Player vs Player)
- Add sound effects and colored terminal output

---

 ✅ Conclusion

This project demonstrates core Python programming concepts such as functions,
loops, conditionals, exception handling, and the `random` module, while
delivering a polished and reliable command-line gaming experience. It fulfills
all requirements of **CodSoft Python Internship – Task 4** and is ready to be
showcased on GitHub and LinkedIn.

---

 👤 Author

"C.SIRISHA"
Python Developer Intern @ CodSoft
