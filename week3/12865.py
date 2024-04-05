import sys

input = sys.stdin.readline

N, K = map(int, input().split())

w = []
v = []

for _ in range(N):
  v1, v2 = map(int, input().split())
  w.append(v1)
  v.append(v2)

dp = [ [ 0 ] * ( K + 1 ) for _ in range( N + 1 ) ] # 메모지에이션할 데이터 구조 생성
max_value = 0

for i in range(1, N + 1):
  for j in range(1, K + 1):
    if w[i - 1] <= j:
      dp[i][j] = max(v[i-1] + dp[i-1][j - w[i -1]], dp[i-1][j])
    else:
      dp[i][j] = dp[i - 1][j]
    
    max_value = max(dp[i][j], max_value)
  
print(max_value)