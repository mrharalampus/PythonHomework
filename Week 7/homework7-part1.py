import requests

def get_random_word():
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0].lower()
    return "python"  # fallback word


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "-"
    return display


def hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts = 6

    print("🎮 Welcome to Hangman!")

    while attempts > 0:
        current_display = display_word(word, guessed_letters)
        print("\nWord:", current_display)
        print("Attempts left:", attempts)

        if "-" not in current_display:
            print("🎉 You guessed the word!")
            break

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print("❌ Wrong guess!")

    if attempts == 0:
        print(f"\n💀 You lost! The word was: {word}")


if __name__ == "__main__":
    hangman()