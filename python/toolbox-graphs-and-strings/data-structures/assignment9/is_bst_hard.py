#!/usr/bin/python3

# Is it a binary search tree? Hard version.


# Task. You are given a binary tree with integers as its keys. 
# You need to test whether it is a correct binary search tree. 
# Note that there can be duplicate integers in the tree, and this 
# is allowed. The definition of the binary search tree in such 
# case is the following: for any node of the tree, if its key 
# is 𝑥, then for any node in its left subtree its key must be 
# strictly less than 𝑥, and for any node in its right subtree
# its key must be greater than or equal to 𝑥. In other words, 
# smaller elements are to the left, bigger elements are to the right, 
# and duplicates are always to the right. You need to check whether 
# the given binary tree structure satisfies this condition. You are 
# guaranteed that the input contains a valid binary tree. That is, 
# it is a tree, and each node has at most two children.

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