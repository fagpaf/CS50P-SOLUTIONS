from random import choice
from pyfiglet import Figlet
import sys


def main():
    solve()

# Era melhor ter feito tudo na main, que eu não precisaria fazer duas vezes o mesmo código
def solve():
    argv = sys.argv
    font = argv[-1]

    if len(argv) == 3 and "-f" in argv and font in Figlet().getFonts():
        choice_font(argv)

    elif len(argv) == 1:
        random_font()

    else:
        sys.exit(1)


def random_font():
    f = Figlet(font=choice(Figlet().getFonts()))  # pega uma fonte aleatória
    text = input("Input: ")
    print("Output: ", f.renderText(text))


def choice_font(prompt):
    f = Figlet(font=prompt[2])
    text = input("Input: ")
    print("Output: ", f.renderText(text))


if __name__ == "__main__":
    main()
