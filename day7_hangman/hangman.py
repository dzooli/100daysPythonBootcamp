import random
import hangman_stages
import hangman_words

max_lives = 6

game_over = False
player_wins = False
chosen_word = random.choice(hangman_words.word_list)
placeholder = [ '_' for x in range(0, len(chosen_word))]

lives = 6
while not game_over:
    guess = input("Enter your guess character:\n").lower()
    i = 0
    found_char = False
    for curr_char in chosen_word:
        if curr_char == guess:
            placeholder[i] = guess
            found_char = True
        i += 1
    if not found_char:
        lives -= 1
        print(F"You have lost a life :( Remains {lives}")
    else:
        print(''.join(placeholder))
        if '_' not in placeholder:
            player_wins = True
    print(hangman_stages.stages[lives])
    if player_wins:
        game_over = True
        print("Congratulations!! You are the winner!")
    elif lives == 0:
        game_over = True
        print("You have died! Try it again.")
