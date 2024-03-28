import sys
from itertools import combinations

input = sys.stdin.readline

N, S = map(int, input()[:-1].split(' ')) # 정수의 개수(N), 정수 합 조건 (S)

numbers = list(map(int, input()[:-1].split(' ')))

count = 0
for i in range(1, N+1):
  pm = list(combinations(numbers, i))

  for p in pm:
    if sum(p) == S:
      count += 1


print(count)


## 조합만드는 반복, 조합을 순회하는 반복, 조합 내 값을 모두 더하는 반복까지
## 3중 for문인 것 같아 맞추긴 했지만 잘못된 정답 풀이라고 생각합니다..!

## 이렇게 푸는게 문제 의도(?)에 맞지 않는 것 같은데 의견 남겨주시면 감사합니다!
## 안남겨주셔도 됩니다!🙇🏻‍♂️