import random

def guess_the_number():
    print("\nWelcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Game setup
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    
    # Set difficulty
    if difficulty == "easy":
        max_attempts = 15
        print("Easy mode: You get 15 attempts.")
    elif difficulty == "medium":
        max_attempts = 10
        print("Medium mode: You get 10 attempts.")
    elif difficulty == "hard":
        max_attempts = 5
        print("Hard mode: You get 5 attempts.")
    else:
        print("Invalid choice. Defaulting to medium (10 attempts).")
    
    # Game loop
    while attempts < max_attempts:
        print(f"\nAttempt {attempts + 1} of {max_attempts}")
        
        try:
            guess = int(input("Your guess (1-100): "))
        except ValueError:
            print("Please enter a valid number!")
            continue
            
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100!")
            continue
            
        attempts += 1
        
        # Check guess
        if guess == secret_number:
            print(f"\nCongratulations! You guessed it in {attempts} attempts!")
            print(f"The number was indeed {secret_number}.")
            return
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
            
        # Give hints after certain attempts
        if attempts == max_attempts // 2:
            if secret_number % 2 == 0:
                print("Hint: The number is even.")
            else:
                print("Hint: The number is odd.")
        elif attempts == max_attempts - 2:
            diff = abs(guess - secret_number)
            if diff > 30:
                print("Hint: You're very far from the number!")
            elif diff > 15:
                print("Hint: You're getting warmer!")
            else:
                print("Hint: You're really close!")
    
    print(f"\nGame over! You've used all {max_attempts} attempts.")
    print(f"The secret number was {secret_number}.")

def main():
    while True:
        guess_the_number()
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
