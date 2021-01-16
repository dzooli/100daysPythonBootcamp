import random

"""
Desc: 
 Function to convert List of strings to a string with a separator
"""
def converttostr(input_seq, seperator):
   final_str = seperator.join(input_seq)
   return final_str

word_list = ["baboon", "camel", "chimera", "leopard",
             "jaguar", "lion", "tiger", "monkey",
             "adwaark", "penguin"]

game_over = False
player_wins = False
chosen_word = random.choice(word_list)
placeholder = [ '_' for x in range(0, len(chosen_word))]
print(chosen_word)

lives = 6
while not game_over:
    # read a new guess
    guess = input("Enter your guess character:\n").lower()
    # check and update the placeholder
    i = 0
    found_char = False
    for curr_char in chosen_word:
        if curr_char == guess:
            placeholder[i] = guess
            found_char = True
        i += 1
    # decrease lives of check the remaining placeholders
    if not found_char:
        lives -= 1
        print(F"You have lost a life :( Remains {lives}")
    else:
        print(''.join(placeholder))
        if '_' not in placeholder:
            player_wins = True
    # check if the player wins or no more lives
    if player_wins:
        game_over = True
        print("Congratulations!! You are the winner!")
    elif lives == 0:
        game_over = True
        print("You have died! Try it again.")
