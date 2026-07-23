"""
Rock-Paper-Scissors Game
--------------------------------
CodSoft Python Internship - Task 4

A command-line Rock-Paper-Scissors game where the player competes
against the computer. Includes score tracking, input validation,
replay functionality, and graceful error handling.

Author: [Your Name]
"""

import random


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CHOICES = {
    "1": "Rock",
    "2": "Paper",
    "3": "Scissors"
}

# Defines which choice beats which: KEY beats VALUE
WINNING_RULES = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}


# ---------------------------------------------------------------------------
# Display Functions
# ---------------------------------------------------------------------------

def display_banner():
    """Prints the welcome banner for the game."""
    print("=" * 50)
    print("      ROCK - PAPER - SCISSORS GAME")
    print("      CodSoft Python Internship - Task 4")
    print("=" * 50)


def display_rules():
    """Prints the rules of the game."""
    print("\nGAME RULES:")
    print("  1. Rock crushes Scissors")
    print("  2. Scissors cuts Paper")
    print("  3. Paper covers Rock")
    print("  4. Same choice by both players results in a Draw")
    print("-" * 50)


def display_menu():
    """Prints the choice menu for the player."""
    print("\nMake your choice:")
    print("  1. Rock")
    print("  2. Paper")
    print("  3. Scissors")
    print("  4. Exit Game")


def display_result(player_choice, computer_choice, result):
    """Displays the choices made and the round result."""
    print(f"\nYou chose   : {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if result == "draw":
        print(">> It's a DRAW!")
    elif result == "player":
        print(">> You WIN this round!")
    else:
        print(">> Computer WINS this round!")


def display_scoreboard(player_score, computer_score, draws, total_rounds):
    """Displays the current scoreboard after each round."""
    print("-" * 50)
    print("SCOREBOARD")
    print(f"  Player Score   : {player_score}")
    print(f"  Computer Score : {computer_score}")
    print(f"  Draws          : {draws}")
    print(f"  Total Rounds   : {total_rounds}")
    print("-" * 50)


def display_final_summary(player_score, computer_score, draws, total_rounds):
    """Displays the final summary when the player exits the game."""
    print("\n" + "=" * 50)
    print("             FINAL GAME SUMMARY")
    print("=" * 50)
    print(f"  Total Rounds Played : {total_rounds}")
    print(f"  Player Score        : {player_score}")
    print(f"  Computer Score      : {computer_score}")
    print(f"  Draws               : {draws}")

    if player_score > computer_score:
        print("\n  RESULT: Congratulations! You won the game! 🎉")
    elif computer_score > player_score:
        print("\n  RESULT: Computer won the game. Better luck next time!")
    else:
        print("\n  RESULT: The game ended in a tie!")

    print("=" * 50)
    print("Thank you for playing! Goodbye.")


# ---------------------------------------------------------------------------
# Core Game Logic Functions
# ---------------------------------------------------------------------------

def get_player_choice():
    """
    Prompts the player for a valid menu choice and validates the input.
    Returns the corresponding choice name, "EXIT", or None if invalid.
    """
    display_menu()
    user_input = input("Enter your choice (1-4): ").strip()

    if user_input == "":
        print("Error: Input cannot be empty. Please try again.")
        return None

    if user_input == "4":
        return "EXIT"

    if user_input not in CHOICES:
        print("Error: Invalid choice. Please enter a number between 1 and 4.")
        return None

    return CHOICES[user_input]


def get_computer_choice():
    """Randomly generates and returns the computer's choice."""
    return random.choice(list(CHOICES.values()))


def determine_winner(player_choice, computer_choice):
    """
    Determines the winner of the round.
    Returns "draw", "player", or "computer".
    """
    if player_choice == computer_choice:
        return "draw"

    if WINNING_RULES[player_choice] == computer_choice:
        return "player"

    return "computer"


def ask_play_again():
    """
    Asks the player if they want to play another round.
    Validates the input and returns True or False.
    """
    while True:
        try:
            choice = input("\nDo you want to play again? (y/n): ").strip().lower()

            if choice == "":
                print("Error: Input cannot be empty. Please enter 'y' or 'n'.")
                continue

            if choice in ("y", "yes"):
                return True
            elif choice in ("n", "no"):
                return False
            else:
                print("Error: Invalid input. Please enter 'y' or 'n'.")

        except KeyboardInterrupt:
            print("\n\nGame interrupted by user.")
            return False


# ---------------------------------------------------------------------------
# Main Game Loop
# ---------------------------------------------------------------------------

def play_game():
    """Runs the main game loop, handling rounds, scoring, and replay."""
    player_score = 0
    computer_score = 0
    draws = 0
    total_rounds = 0

    display_banner()
    display_rules()

    playing = True

    while playing:
        try:
            player_choice = get_player_choice()

            # Invalid input - restart the loop and ask again
            if player_choice is None:
                continue

            # Player chose to exit
            if player_choice == "EXIT":
                print("\nExiting the game...")
                break

            computer_choice = get_computer_choice()
            result = determine_winner(player_choice, computer_choice)

            # Update scores based on round result
            if result == "player":
                player_score += 1
            elif result == "computer":
                computer_score += 1
            else:
                draws += 1

            total_rounds += 1

            display_result(player_choice, computer_choice, result)
            display_scoreboard(player_score, computer_score, draws, total_rounds)

            playing = ask_play_again()

        except KeyboardInterrupt:
            # Gracefully handle Ctrl+C during the round
            print("\n\nGame interrupted by user.")
            break

        except Exception as error:
            # Catch-all safety net so the app never crashes unexpectedly
            print(f"\nAn unexpected error occurred: {error}")
            print("Please try again.")
            continue

    display_final_summary(player_score, computer_score, draws, total_rounds)


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nGame terminated by user. Goodbye!")
    except Exception as e:
        print(f"\nA critical error occurred: {e}")
        print("The application will now close.")