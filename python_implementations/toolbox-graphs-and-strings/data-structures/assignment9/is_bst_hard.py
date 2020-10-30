#!/usr/bin/python3

import sys, threading


sys.setrecursionlimit(2*10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
  if len(tree) <= 1:
    return True

  result = [True]
  def pre_order_traversal(index, minimum, maximum):
    if index == -1:
      return

    if key[index] >= maximum or key[index] < minimum:
      result.append(False) 

    pre_order_traversal(left[index], minimum, key[index])
    pre_order_traversal(right[index], key[index], maximum)

  nodes = len(tree)
  key = [0 for _ in range(nodes)]
  left = [0 for _ in range(nodes)]
  right = [0 for _ in range(nodes)]

  for i in range(nodes):
    key[i] = tree[i][0]
    left[i] = tree[i][1]
    right[i] = tree[i][2]

  index = 0
  pre_order_traversal(index, float('-inf'), float('inf'))
  return len(result) == 1


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for _ in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()


if __name__ == '__main__':
  main()