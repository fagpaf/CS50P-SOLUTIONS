from random import randint
import sys

def main():
    level = treatment()
    guess(level)


def treatment():
    while True:
        try:
            print("Level: ", end="")
            n = int(input())
            if n <= 0:
                raise ValueError
            return n

        except ValueError:
            continue


def guess(level):
    number = randint(1, level)
    while True:
        try:
            chosen = int(input("Guess: "))
            if chosen <= 0:
                raise ValueError

            if chosen > number:
                print("Too large!")
            elif chosen < number:
                print("Too small!")
            else:
                print("Just right!")
                sys.exit()

        except ValueError:
            continue


if __name__ == "__main__":
    main()
