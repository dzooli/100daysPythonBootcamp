age = input("What is your current age: ")
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = 365 * years_remaining
months_remaining = 12 * years_remaining
weeks_remaining = 4 * months_remaining

message = F"You have {days_remaining} days, {weeks_remaining} weeks and {years_remaining} year(s) left."
print(message)
