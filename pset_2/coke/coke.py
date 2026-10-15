def main():
    due()

def due():
    value = 50
    while value > 0:
        print("Amount Due:", value)
        coin = int(input("Insert Coin: "))
        if coin in [25, 10, 5]:
            value -= coin
    print("Change Owed:", abs(value))

main()

#-----------------------------------------

# Não  aceita

# def main():
#     due()


# def due():
#     ls_coins = [25, 10, 5]
#     value = 50

#     while value > 0:
#         print("Amount Due: ", value)
#         coin = int(input("Insert Coin: "))
#         if coin in ls_coins:
#             value -= coin
#     print("Change Owed: ", abs(value))


# main()
