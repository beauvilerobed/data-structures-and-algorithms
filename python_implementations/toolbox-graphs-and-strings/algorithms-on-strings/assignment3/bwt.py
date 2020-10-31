# python3
import sys

# Problem: Construct the Burrows–Wheeler Transform of a String

# Task. Construct the Burrows–Wheeler transform of a string

def BWT(text):
    n = len(text)
    texts = [text]
    for i in range(n - 1):
        text1 = text[:i + 1]
        text2 = text[i + 1:]
        texts.append(text2 + text1)
    
    texts.sort()
    result = ''.join([texts[i][n - 1] for i in range(n)])
    return result

def main():
    text = sys.stdin.readline().strip()
    print(BWT(text))

if __name__ == '__main__':
    main()