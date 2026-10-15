def main():
    kramer = input("Greeting: ").lower()
    print(kramer)
    if "hello" in kramer:
        print("$0")
    elif kramer[0] == "h":
        print("$20")
    else:
        print("$100")

main()
