import random

# List of words to choose from
word_list = ['python', 'hangman', 'challenge', 'project', 'developer']

# Choose a random word
word = random.choice(word_list)
word_letters = set(word)  # Unique letters in the word
guessed_letters = set()   # Correct guesses
wrong_guesses = set()     # Incorrect guesses
lives = 6

print("🎮 Welcome to Hangman!")

while lives > 0 and word_letters:
    print("\nWord: ", ' '.join([letter if letter in guessed_letters else '_' for letter in word]))
    print(f"💀 Lives left: {lives}")
    print(f"❌ Wrong guesses: {', '.join(sorted(wrong_guesses))}")

    guess = input("🔠 Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabet.")
        continue

    if guess in guessed_letters or guess in wrong_guesses:
        print("⛔ You already guessed that.")
        continue

    if guess in word_letters:
        guessed_letters.add(guess)
        word_letters.remove(guess)
        print("✅ Good guess!")
    else:
        wrong_guesses.add(guess)
        lives -= 1
        print("❌ Wrong guess!")

# Game Over
if lives == 0:
    print(f"\n💥 You lost! The word was: {word}")
else:
    print(f"\n🎉 You won! The word was: {word}")

