scores = input("Enter your student scores separated by space: ").split()

max_score = 0
for score in scores:
    score_int = int(score)
    if int(score) > max_score:
        max_score = int(score)

print(F"Highest score is {max_score}")