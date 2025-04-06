import random

class GuessMyNumber:
    def __init__(self):
        self.min = 1
        self.max = 100
        self.guesses = 0
        self.last_guess = None
        self.possible_cheat = False

    def reset_game(self):
        self.min = 1
        self.max = 100
        self.guesses = 0
        self.last_guess = None
        self.possible_cheat = False

    def get_computer_guess(self):
        self.last_guess = random.randint(self.min, self.max)
        self.guesses += 1
        return self.last_guess

    def update_range(self, feedback):
        if feedback == 'L':
            self.min = self.last_guess + 1
        elif feedback == 'H':
            self.max = self.last_guess - 1

        # Check if the user is giving impossible hints
        if self.min > self.max:
            self.possible_cheat = True

    def play(self):
        print("\n🔮 **Guess the Number (User Version)** 🔮")
        print("Think of a number between 1 and 100.")
        print("I'll try to guess it!")
        input("Press Enter when you're ready...")

        while True:
            self.reset_game()
            print("\n🔢 **New Game Started!** 🔢")

            while True:
                guess = self.get_computer_guess()
                print(f"\n🤖 My guess: {guess}")

                feedback = input("Was it (L) Too Low, (H) Too High, or (C) Correct? ").upper()

                while feedback not in ['L', 'H', 'C']:
                    print("❌ Invalid input! Please enter L, H, or C.")
                    feedback = input("(L) Too Low, (H) Too High, or (C) Correct? ").upper()

                if feedback == 'C':
                    print(f"\n🎉 **I guessed it in {self.guesses} tries!** 🎉")
                    break
                else:
                    self.update_range(feedback)

                    if self.possible_cheat:
                        print("\n🤨 **Hey! You're changing the number, aren't you?**")
                        print("Let's play fair next time! 😉")
                        break

            play_again = input("\nPlay again? (Y/N): ").upper()
            if play_again != 'Y':
                print("\nThanks for playing! Goodbye! 👋")
                break

if __name__ == "__main__":
    game = GuessMyNumber()
    game.play()
