from random import randint

def main():
    score = solve()
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n not in [1, 2, 3]:
                raise ValueError
            return n

        except ValueError:
            continue

def generate_integer(level):
    match level:
        case 1:
            return randint(0, 9)
        case 2:
            return randint(10, 99)
        case 3:
            return randint(100, 999)

def ask_question(x, y):
    """Retorna True se acertou, False se errou todas"""
    for _ in range(3):
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == x + y:
                return True
            else:
                print("EEE")
        except ValueError:
            print("EEE")
    # Errou todas
    print(f"{x} + {y} = {x+y}")
    return False

def solve():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        if ask_question(x, y):
            score += 1
    return score

if __name__ == "__main__":
    main()
