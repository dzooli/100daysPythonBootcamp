name1 = input("What is your name? ")
name2 = input("What is their name? ")

love_count = true_count = 0

for love_char in "love":
    love_count = love_count + (name1 + name2).lower().count(love_char)

for true_char in "true":
    true_count = true_count + (name1 + name2).lower().count(true_char)

score = love_count * 10 + true_count

if score < 10 or score > 90:
    print(F"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(F"Your score is {score}, you are alright together.")
else:
    print(F"Your score is {score}")