import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_images = [rock, paper, scissors]

user_choice: int = int(input("Enter your choice (0: rock, 1: paper, 2: scissors): "))
computer_choice = random.choice(choice_images)
computer_value = choice_images.index(computer_choice)

lose_msg = "You lose"
win_msg = "You win"

if 0 <= user_choice <=2:
    print(computer_choice)
    if user_choice == computer_value:
        print("In pair")
    else:
        if user_choice == 0:
            if computer_value == 1:
                print(lose_msg)
            else:
                print(win_msg)
        if user_choice == 1:
            if computer_value == 0:
                print(win_msg)
            else:
                print(lose_msg)
        if user_choice == 2:
            if computer_value == 1:
                print(win_msg)
            else:
                print(lose_msg)
else:
    print("Invalid user choice!")

