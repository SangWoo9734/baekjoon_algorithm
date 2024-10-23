import sys

input = sys.stdin.readline

T, W = map(int, input().split())

position = [0] + [ int(input()) for _ in range(T) ]

dp = [ [ 0 for _ in range(W + 1) ] for _ in range(T + 1)]

dp[1][0], dp[1][1] = position[1] % 2, position[1] // 2

for t in range(2, T + 1):
  for w in range(W + 1):
    j = position[t] % 2 if w % 2 == 0 else position[t] // 2 # 이동 횟수가 짝수면 1번 나무에, 홀수면 2번 나무에 있음
    print(w, j)
    dp[t][w] = max(dp[t-1][:w + 1]) + j

  print(*dp, sep='\n')
  print()
print(max(dp[-1]))