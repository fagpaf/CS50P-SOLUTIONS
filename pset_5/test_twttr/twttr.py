def main():
    text = input("Input: ")
    print("Output:", shorten(text))


def shorten(prompt):
    result = ""
    for char in prompt:
        if char not in "aeiouAEIOU":
            result += char
    return result


if __name__ == "__main__":
    main()
