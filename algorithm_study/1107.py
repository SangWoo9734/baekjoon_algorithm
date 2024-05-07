import sys

def check_channel (channel, bbtns):

  while 1:
    c = channel % 10
    channel //= 10

    if c in bbtns:
      return False

    if channel == 0 : break
  
  return True

def check_high_channel (bbtns):
  high = N
  while(1):
    if high > 999999:
      return high

    if check_channel(high, bbtns):
      return high

    high += 1

def check_low_channel (bbtns):
  low = N
  
  while(1):
    if low < 0:
      return -1

    if check_channel(low, bbtns):
      return low
      
    low -= 1

input = sys.stdin.readline

N = int(input())

M = int(input())

btns = list(map(int, input().split()))

if N == 100: print(0)
else :
  high = check_high_channel(btns)
  low = check_low_channel(btns)

  # print(f"high: {high}, low: {low}")

  cur_channel = high if abs(high - N) < abs(low - N) or low == -1 else low
  a = len(str(cur_channel)) + abs(cur_channel - N)
  b = abs(N - 100)


  # print(f"a: {a}, b: {b}")

  print( a if a < b else b )

