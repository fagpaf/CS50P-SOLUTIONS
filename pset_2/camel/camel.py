def main():
    convert(input("camelCase: "))


def convert(prompt):
    print("snake_case: ", end="")
    for char in prompt:
        if char == char.upper():
            print("_", end="")
            print(char.lower(), end="")
        else:
            print(char, end="")

main()
