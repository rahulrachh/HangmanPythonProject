import random
from words import words
from string import ascii_uppercase

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(ascii_uppercase)
    used_letters = set()

    lives = len(word_letters) + 1

    while len(word_letters)>0 and lives:

        # Tells you the used letters
        print('You have used these letters: ',' '.join(used_letters))

        #tells the user the word and the ltters to be guessed replace by '-'
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ', ' '.join(word_list))

        user_letter = input('Guess the letter: ').upper()
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                print('Lives Left: ', lives)
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('Letter not in word')
                print('Lives left: ', lives)
        elif user_letter in used_letters:
            print('You have guessed that letter!!!')
        else:
            print('Invalid character. Please try again')


    print('The final word you have guessed is: ', ''.join([letter if letter in used_letters else '-' for letter in word]))
    if lives:
        print('You did it You did it!!')
    else:
        print("You couldn't complete the word in number of chances available to you")


hangman()


