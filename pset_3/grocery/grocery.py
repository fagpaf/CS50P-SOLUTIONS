def main():
    dic = grocery_list()
    for key in sorted(dic):
        print(dic[key], key)


def grocery_list():
    count = {}
    while True:
        try:
            item = input().upper()
            if item in count:
                count[item] += 1
            else:
                count[item] = 1
        except EOFError:
            return count


main()
