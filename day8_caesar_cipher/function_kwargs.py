def greet():
    print("Welcome to Caesar-cipher...")
    print("Version: v1.0")
    print("")


def greet_with_name(name, **kwargs):
    print("Hello", name)
    print("Welcome to Caesar-cipher...")
    print("Version: v1.0")
    print("Keyword parameters:")
    for key in kwargs:
        print(F"Name: {key}; value: {kwargs[key]}")
    print("")


def greet_with(name, location):
    print("Welcome to Caesar-cipher")
    print("Version: 1.0")
    print(F"Hello {name} from {location}")
    print("")

if __name__ == "__main__":
    greet()
    greet_with_name("Bob", name2="Zoltan")
    greet_with("Zoltan", "Hungary")
