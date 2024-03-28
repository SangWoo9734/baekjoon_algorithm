import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

numbers = []
ans = []

while True:
    try:
        x = int(input())
        numbers.append(x)
    except:
        break


def pre_to_post(numbers):
  if len(numbers) == 1:
    ans.append(numbers[0])
    return
  if len(numbers) == 0:
    return

  vertex = numbers[0]

  index = 1
  while True:
    if index >= len(numbers) or numbers[index] > vertex:
      break
    index += 1

  pre = pre_to_post(numbers[1: index])
  post = pre_to_post(numbers[index:])
  ans.append(vertex)


pre_to_post(numbers)

for n in ans:
  print(n)

# 현재 리스트가 전위 순회 되어있다면,
# 이진 검색 리스트의 규칙에 따라서 [ (vertex), (left), (right) ]로 구성되어있다.abs
# vertex 기준으로 left와 right의 기준점을 찾고 재귀 함수를 통해
# 후위 순회 방식 [ (left), (right), (vertex) ]로 바꾸어주면 해결 가능하다.