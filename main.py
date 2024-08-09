import random
from art import stages

word_list = ['hello', 'goodbye', 'thankyou', 'adios']

stage_images = stages

user_lives = 6

welcome_note = 'Welcome to Hangman, created by Robert L. Norwood!'
print(welcome_note)
print(f'You currently have {user_lives} lives! Try to make each of them count. Good luck!')
print('*************************************')

random_word = random.choice(word_list)

underscores = ''

for position in range(len(random_word)):
    underscores += '_'
print(f'The word to guess has this many letters in it: {len(underscores)} ')
print(underscores)

correct_letters = []

game_running = True

while game_running:

    user_guess = input("Guess a letter: ").lower()

    if user_guess in correct_letters:
        print(f"You've already guessed {user_guess}, please guess again!")

    letter_display = ''

    for letter in random_word:
        if letter == user_guess:
            letter_display += letter
            correct_letters.append(user_guess)
        elif letter in correct_letters:
            letter_display += letter
        else:
            letter_display += '_'
    print(letter_display)

    if '_' not in letter_display:
        print("You WIN! You guessed the word correctly, great job!")
        game_running = False

    if user_guess not in random_word:
        user_lives -= 1
        if user_lives == 1:
            print(f"Wrong, try again. You have {user_lives} life left.")
        elif user_lives == 0:
            print(f"You ran out of lives, you LOSE!")
            print(f"The correct word was '{random_word}'")
            game_running = False
        else:
            print(f"Wrong, try again. You have {user_lives} lives left.")

    print(stage_images[user_lives])