"""
        Day1: Print and input functions exercises

        Notes: see the string conversion of the input() function
    """

if __name__ == "__main__":
    print("Day 1 - Python Print Function")
    print("Day", 1, '-', "Python", "Print", "Function")
    print("Day", 1, '-', "Python", "Print", "Function", sep='-')
    print("Day", 1, '-', "Python", "Print", "Function", sep='-', end='\t')
    print("Next line")

    your_name = str(input("What is your name? "))
    print("Hello", your_name)
    print(f"Your name's length is: {len(your_name)}")
