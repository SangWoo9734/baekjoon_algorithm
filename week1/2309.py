import sys

tinys = [ int(sys.stdin.readline()) for _ in range(9)]
answer = []

def nCr(n, ans, r):
    if n == len(tinys):
        if len(ans) == r:
            temp = [i for i in ans]
            answer.append(temp)
        return

    ans.append(tinys[n])
    nCr(n+1, ans, r)
    ans.pop()
    nCr(n+1, ans, r)


nCr(0, [], 7)

for a in answer:
  if sum(a) == 100:
    for i in sorted(a):
      print(i)
    break
