def main():
    change(input("Input: "))

def change(prompt):
    print("Output: ", end="")
    for _, char in enumerate(prompt):
        if char in "aeiou" or char in "AEIOU":
            print("", end="")
        else:
            print(char, end="")


main()
