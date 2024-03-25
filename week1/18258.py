import sys
from collections import deque

class CustomQueue():
  def __init__(self):
    self.queue = deque()
  
  def push(self, value):
    self.queue.append(value)

  def pop(self):
    if self.empty():
      return -1

    return self.queue.popleft()

  def size(self):
    return len(self.queue)

  def empty(self):
    return int(len(self.queue) == 0)
  
  def front(self):
    if self.empty():
      return -1

    return self.queue[0]
  
  def back(self):
    if self.empty():
      return -1

    return self.queue[-1]

order_count = int(sys.stdin.readline())
orders = [ sys.stdin.readline()[:-1].split(' ') for _ in range(order_count)]

q = CustomQueue()

for order in orders:
  if 'push' in order:
    word, value = order
  
  else:
    word = order[0]

  match word:
    case 'push':
      q.push(value)
    case "pop":
      print(q.pop())
    case "size":
      print(q.size())
    case "empty":
      print(q.empty())
    case "front":
      print(q.front())
    case "back":
      print(q.back())

