import emoji


def main():
    print("Input: ", end="")
    phrase = input()
    print("Output:", emoji.emojize(phrase, language="alias"))


if __name__ == "__main__":
    main()
