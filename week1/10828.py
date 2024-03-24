import sys

class Stack:
  def __init__(self):
    self.stack = []

  def push(self, value):
    self.stack.append(value)

  def pop(self):
    if len(self.stack) == 0:
      return -1

    return self.stack.pop()

  def size(self):
    return len(self.stack)
  
  def empty(self):
    return int(len(self.stack) == 0)
  
  def top(self):
    if len(self.stack) == 0:
      return -1
      
    return self.stack[-1]

N = int(sys.stdin.readline())
order_lines = [ sys.stdin.readline()[:-1].split(' ') for _ in range(N) ]

stack = Stack()

for order in order_lines:
  if 'push' in order:
    order_word, value = order
  else:
    order_word = order[0]
  

  if order_word == 'push':
    stack.push(value)
  
  elif order_word == 'pop':
    print(stack.pop())

  elif order_word == 'top':
    print(stack.top())

  elif order_word == 'size':
    print(stack.size())

  elif order_word == 'empty':
    print(stack.empty())