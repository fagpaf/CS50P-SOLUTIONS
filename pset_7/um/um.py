import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    cnt = 0
    # re.IGNORECASE faz ignorar maiúsculas/minúsculas
    # \b garante que é uma palavra inteira
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)

    for _ in matches:
        cnt += 1

    return cnt

if __name__ == "__main__":
    main()
