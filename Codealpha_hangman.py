import random

def play_hangman():
    
    words = ["python", "coding", "loop", "random", "logic"]
    
    
    secret_word = random.choice(words)
    
    
    guessed_letters = []  # List to store user guesses
    attempts = 6          # Max incorrect guesses
    
    print("Welcome to Hangman!")
    print(f"I have picked a word. You have {attempts} incorrect guesses allowed.")

    
    while attempts > 0:
        
        
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nCurrent Word: {display_word}")
        print(f"Attempts left: {attempts}")
        
       
        if "_" not in display_word:
            print(f"\n🎉 CONGRATULATIONS! You guessed the word: {secret_word}")
            return # Exit the function/game

        
        guess = input("Guess a letter: ").lower()

        
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different one.")
            continue

       
        guessed_letters.append(guess)

        
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"❌ Sorry, '{guess}' is not there.")

    
    print(f"\n💀 GAME OVER! The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()