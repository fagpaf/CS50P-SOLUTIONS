def main():
    list = ["42", "forty-two", "forty two"]
    prompt = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strcdip()
    if prompt in list:
        print("Yes")
    else:
        print("No")

main()
