import random
words = ["python", "program", "hangman", "coding", "developer"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎯 Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")

while attempts > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print("Attempts left:", attempts)


    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word correctly.")
        break

    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("❌ Wrong guess!")

if attempts == 0:
    print("\n💀 Game Over!")

    print("The correct word was:", word)
