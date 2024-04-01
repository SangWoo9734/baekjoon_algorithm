import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
plus, minus, multi, divide = map(int, input().split())
results = []

ea = {
  'plus': plus,
  'minus': minus,
  'multi': multi,
  'divide': divide,
}

inital_value = numbers.pop(0)
index = 0

def dfs(arr, index, ea, res):
  if index >= N - 1:
    results.append(res)
    return

  p = arr[index]
  index += 1

  if ea['plus']:
    ea['plus'] -= 1
    dfs(arr, index, ea, res + p)
    ea['plus'] += 1

  if ea['minus']:
    ea['minus'] -= 1
    dfs(arr,  index, ea, res - p)
    ea['minus'] += 1

  if ea['multi']:
    ea['multi'] -= 1
    dfs(arr, index, ea, res * p)
    ea['multi'] += 1

  if ea['divide']:
    ea['divide'] -= 1
    dfs(arr,  index, ea, (abs(res) // p) * ( - 1 if res < 0 else 1))
    ea['divide'] += 1

dfs(numbers, index, ea, inital_value)

print(max(results))
print(min(results))