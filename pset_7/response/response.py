import validators

def main():
    email = input("What's your email address? ")
    if is_valid(email):
        print("Valid")
    else:
        print("Invalid")

def is_valid(email):
    if validators.email(email):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
