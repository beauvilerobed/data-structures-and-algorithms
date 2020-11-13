# python3

# Binary tree traversals

# Task. You are given a rooted binary tree. 
# Build and output its in-order, pre-order and 
# post-order traversals.

# example:

# Input: 

# Each of these lines contains three integers 
# key_i, left_i and right_i.
# 
# key_i is the key of the i-th 
# vertex, left_i is the index of the left child of 
# the i-th vertex, and right_i is the index of the right 
# child of the i-th vertex. If i doesn’t have left or 
# right child (or both), the corresponding left_i or right_i 
# (or both) will be equal to −1. 

#   5
#   4 1 2                           4
#   2 3 4                          / \
#   5 -1 -1           ====>       2   5
#   1 -1 -1                      / \
#   3 -1 -1                     1   3

#   Output:
#   1 2 3 4 5 
#   4 2 1 3 5 
#   1 3 2 5 4


import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
  def read(self, n, key=None, left=None, right=None):
    self.n = n
    self.key = key or [0 for i in range(self.n)]
    self.left = left or [0 for i in range(self.n)]
    self.right = right or [0 for i in range(self.n)]
    if not key:
      for i in range(self.n):
        [a, b, c] = map(int, sys.stdin.readline().split())
        self.key[i] = a
        self.left[i] = b
        self.right[i] = c

  def inOrder(self):
    self.result = []
    def in_order_traversal(index):
      if index == -1:
        return

      in_order_traversal(self.left[index])
      self.result.append(self.key[index])
      in_order_traversal(self.right[index])

    index = 0   
    in_order_traversal(index)

    return self.result

  def preOrder(self):
    self.result = []
    def pre_order_traversal(index):
      if index == -1:
        return

      self.result.append(self.key[index])
      pre_order_traversal(self.left[index])
      pre_order_traversal(self.right[index])

    index = 0   
    pre_order_traversal(index)

    return self.result

  def postOrder(self):
    self.result = []
    def post_order_traversal(index):
      if index == -1:
        return

      post_order_traversal(self.left[index])
      post_order_traversal(self.right[index])
      self.result.append(self.key[index])

    index = 0   
    post_order_traversal(index)

    return self.result

def main():
  tree = TreeOrders()
  n = int(input())
  tree.read(n)
  print(" ".join(str(x) for x in tree.inOrder()))
  print(" ".join(str(x) for x in tree.preOrder()))
  print(" ".join(str(x) for x in tree.postOrder()))

# threading.Thread(target=main).start()


if __name__ == '__main__':
  main()