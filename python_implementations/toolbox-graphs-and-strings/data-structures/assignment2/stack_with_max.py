#python3

# Extending stack interface

# Task. Implement a stack supporting the operations 
# Push(), Pop(), and Max().

import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.maximum = None

    def Push(self, a):
        if len(self.__stack) == 0:
            self.__stack.append(a)
            self.maximum = a
        
        elif a > self.maximum:
            temp = 2 * a - self.maximum
            self.__stack.append(temp)
            self.maximum = a
        else:
            self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        if len(self.__stack) == 0:
            pass
        else:
            removed_value = self.__stack[-1]
            self.__stack.pop()
            if removed_value > self.maximum:
                self.maximum = (2 * self.maximum) - removed_value

    def Max(self):
        assert(len(self.__stack))
        if len(self.__stack) > 0:
            return self.maximum


def main():
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)


if __name__ == '__main__':
    main()
