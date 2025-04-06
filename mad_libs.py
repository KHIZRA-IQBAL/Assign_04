import random

def get_word(type):
    """Helper function to get user input for different word types"""
    return input(f"Enter a {type}: ")

def mad_libs_story1():
    """First mad libs story"""
    print("\nStory 1: The Crazy Adventure")
    adjective1 = get_word("adjective")
    noun1 = get_word("noun")
    verb_past = get_word("verb (past tense)")
    adverb = get_word("adverb")
    adjective2 = get_word("adjective")
    noun2 = get_word("noun")
    noun3 = get_word("noun")
    adjective3 = get_word("adjective")
    verb = get_word("verb")
    noun4 = get_word("noun")
    celebrity = get_word("celebrity name")
    
    story = f"""
    One {adjective1} day, a {noun1} decided to {verb_past} {adverb} down the street.
    Suddenly, a {adjective2} {noun2} appeared with a {noun3} in its hand!
    "{adjective3.capitalize()}!" it shouted while trying to {verb} the {noun4}.
    Just then, {celebrity} showed up and saved the day!
    """
    print(story)

def mad_libs_story2():
    """Second mad libs story"""
    print("\nStory 2: At the Restaurant")
    adjective1 = get_word("adjective")
    noun1 = get_word("noun")
    food_plural = get_word("food (plural)")
    verb_ing = get_word("verb ending with -ing")
    emotion = get_word("emotion")
    food = get_word("food")
    number = get_word("number")
    adjective2 = get_word("adjective")
    
    story = f"""
    The {adjective1} {noun1} restaurant is my favorite place to eat.
    They serve the best {food_plural} while {verb_ing} to music.
    Eating there always makes me feel {emotion}.
    Today I ordered the {food} pizza with {number} toppings.
    It was absolutely {adjective2}!
    """
    print(story)

def mad_libs_story3():
    """Third mad libs story"""
    print("\nStory 3: Space Adventure")
    planet = get_word("planet name")
    alien_name = get_word("alien name")
    number = get_word("number")
    vehicle = get_word("vehicle")
    adjective = get_word("adjective")
    verb = get_word("verb")
    food = get_word("food")
    
    story = f"""
    On the planet {planet}, there lived an alien named {alien_name}.
    They had {number} eyes and traveled by {vehicle}.
    One day, they found a {adjective} Earthling who was trying to {verb}.
    "Would you like some {food}?" asked the Earthling.
    And thus began an intergalactic friendship!
    """
    print(story)

def main():
    print("Welcome to Mad Libs!")
    print("Choose a story or get a random one:")
    print("1. The Crazy Adventure")
    print("2. At the Restaurant")
    print("3. Space Adventure")
    print("4. Random Story")
    
    while True:
        choice = input("\nEnter your choice (1-4) or 'q' to quit: ")
        
        if choice.lower() == 'q':
            print("Thanks for playing!")
            break
            
        if choice == '1':
            mad_libs_story1()
        elif choice == '2':
            mad_libs_story2()
        elif choice == '3':
            mad_libs_story3()
        elif choice == '4':
            story = random.choice([mad_libs_story1, mad_libs_story2, mad_libs_story3])
            story()
        else:
            print("Invalid choice. Please try again.")
            
        play_again = input("\nWould you like to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
