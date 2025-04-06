import random
import time
from collections import Counter

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0
        self.round = 1
        self.history = []
        self.computer_learning = True  # Enable adaptive AI
        
    def get_computer_choice(self):
        """Computer chooses randomly or adapts to player patterns"""
        if not self.computer_learning or len(self.history) < 3:
            return random.choice(self.choices)
        
        # Analyze player's most frequent moves
        freq = Counter(self.history)
        player_favorite = max(freq, key=freq.get)
        
        # Counter the player's favorite move
        if player_favorite == "rock":
            return "paper"
        elif player_favorite == "paper":
            return "scissors"
        else:
            return "rock"

    def determine_winner(self, player, computer):
        """Decide round winner with enhanced rules"""
        if player == computer:
            return "tie"
        
        rules = {
            "rock": ["scissors", "lizard"],
            "paper": ["rock", "spock"],
            "scissors": ["paper", "lizard"],
            "lizard": ["paper", "spock"],
            "spock": ["rock", "scissors"]
        }
        
        return "player" if computer in rules[player] else "computer"

    def display_result(self, player_choice, computer_choice, result):
        """Show animated battle result"""
        print(f"\n{'⚔️ BATTLE ⚔️':^30}")
        time.sleep(0.5)
        print(f"You: {player_choice.upper():<10} vs {computer_choice.upper():>10} :Computer")
        time.sleep(1)
        
        if result == "tie":
            print("\n🤝 It's a tie!")
        else:
            winner = "YOU WIN!" if result == "player" else "COMPUTER WINS!"
            print(f"\n🔥 {winner:^26} 🔥")
            
            # Show why you won/lost
            verbs = {
                "rock": {"scissors": "crushes", "lizard": "crushes"},
                "paper": {"rock": "covers", "spock": "disproves"},
                "scissors": {"paper": "cuts", "lizard": "decapitates"},
                "lizard": {"paper": "eats", "spock": "poisons"},
                "spock": {"rock": "vaporizes", "scissors": "smashes"}
            }
            if result == "player":
                action = verbs[player_choice][computer_choice]
                print(f"{player_choice.title()} {action} {computer_choice}!")
            else:
                action = verbs[computer_choice][player_choice]
                print(f"{computer_choice.title()} {action} {player_choice}!")

    def play_round(self):
        """Handle one round of gameplay"""
        print(f"\n{' ROUND ' + str(self.round) + ' ':=^30}")
        print(f"SCORE: You {self.player_score} - {self.computer_score} Computer")
        
        # Get valid player input
        while True:
            choice = input("\nChoose:\n(R)ock  (P)aper  (S)cissors\n(L)izard  (V)Spock\n(Q)uit\n> ").lower()
            if choice in ['r', 'rock']:
                player_choice = "rock"
                break
            elif choice in ['p', 'paper']:
                player_choice = "paper"
                break
            elif choice in ['s', 'scissors']:
                player_choice = "scissors"
                break
            elif choice in ['l', 'lizard'] and "lizard" in self.choices:
                player_choice = "lizard"
                break
            elif choice in ['v', 'spock'] and "spock" in self.choices:
                player_choice = "spock"
                break
            elif choice in ['q', 'quit']:
                return "quit"
            else:
                print("Invalid choice! Try again.")
        
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(player_choice, computer_choice)
        
        # Update scores and history
        if result == "player":
            self.player_score += 1
        elif result == "computer":
            self.computer_score += 1
        self.history.append(player_choice)
        self.round += 1
        
        self.display_result(player_choice, computer_choice, result)
        return result

    def play_game(self):
        """Main game loop"""
        print("\n" + "✊ ✋ ✌️ WELCOME TO ROCK-PAPER-SCISSORS-LIZARD-SPOCK ✌️ ✋ ✊".center(50))
        print("First to win 3 rounds wins the match!".center(50))
        
        # Game mode selection
        mode = input("\nChoose mode:\n1) Classic (Rock/Paper/Scissors)\n2) Extended (Adds Lizard/Spock)\n> ")
        if mode == "2":
            self.choices.extend(["lizard", "spock"])
        
        while True:
            result = self.play_round()
            
            if result == "quit":
                print("\nThanks for playing!")
                break
                
            # Check for match winner
            if self.player_score >= 3 or self.computer_score >= 3:
                print("\n" + "="*40)
                if self.player_score > self.computer_score:
                    print(f"🏆 YOU WON THE MATCH {self.player_score}-{self.computer_score}! 🏆")
                else:
                    print(f"💻 COMPUTER WON THE MATCH {self.computer_score}-{self.player_score} 💻")
                print("="*40)
                
                # Show game statistics
                print("\n📊 Game Statistics:")
                print(f"Total rounds: {self.round-1}")
                print(f"Your most frequent move: {Counter(self.history).most_common(1)[0][0]}")
                
                # Ask to play again
                if input("\nPlay again? (y/n): ").lower() != 'y':
                    print("\nThanks for playing! Goodbye 👋")
                    break
                else:
                    self.player_score = 0
                    self.computer_score = 0
                    self.round = 1
                    self.history = []

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
