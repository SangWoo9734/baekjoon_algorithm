# K개의 랜선
# N개의 같은 길이 랜선
import sys

K, N = list(map(int, sys.stdin.readline().split(' ')))

lans = [ int(sys.stdin.readline()) for _ in range(K) ]

low = 1
high = max(lans)
max_len = 0

while low <= high:
  params = (low + high) // 2

  count = 0
  for lan in lans:
    count += lan // params

  print(f'low: {low}, params:{params}, high:{high}, count:{count}')
  
  # 결정함수
  # 매개변수(Params의 위치 조정)
  if count >= N:
    max_len = params
    low = params + 1
  else:
    high = params - 1
  
print(max_len)