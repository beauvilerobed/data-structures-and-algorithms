# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next not in "()[]{}":
            pass
        elif next in "([{":
            opening_brackets_stack.append((next,i))
        else:
            if len(opening_brackets_stack) == 0:
                return str(i + 1)
            top = opening_brackets_stack.pop()[0]
            if not are_matching(top, next):
                return str(i + 1)
    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return str(opening_brackets_stack[0][1] + 1)
    

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch  == 0:
        print("success")
    else: 
        print(mismatch)


if __name__ == "__main__":
    main()
