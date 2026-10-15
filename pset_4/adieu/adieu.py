import inflect


def main():
    p = inflect.engine()
    name_list = treatment()
    print()
    print("Adieu, adieu, to", p.join(name_list))


def treatment():
    name_list = []
    while True:
        try:
            name = input("Name: ")
            name_list.append(name)

        except EOFError:
            return name_list


if __name__ == "__main__":
    main()
