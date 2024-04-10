import sys

input = sys.stdin.readline

T = int(input())

test_case = []

for _ in range(T):
  N = int(input())
  coins = list(map(int, input().split()))
  price = int(input())

  test_case.append([
    N,
    coins,
    price,
  ])

total = 0

for c in test_case:
  N, coins, price = c

  dp = [ [ 1 ] + [ 0 ] * price for _ in range(len(coins)) ]

  dp = [ 1 ] + [ 0 ] * price

  for i in range(len(coins)):
    for j in range(1, price + 1):
      if j - coins[i] >= 0:
        dp[j] += dp[j - coins[i]]

  print(dp[-1])
  # print(*dp, sep='\n')


