import sys

input = sys.stdin.readline

N = int(input())

eggs = [ list(map(int, input().split())) for _ in range(N) ]
max_crack = 0

def crack(n, eggs):
  global max_crack

  if n == N: # 계란 끝까지 처리했을때 깨진 계란 세기
    max_crack = max(max_crack, sum(1 for egg in eggs if egg[0] <= 0))
    return

  if eggs[n][0] <= 0: # 이미 깨진 계란에 대한 처리
    crack(n + 1, eggs)

  else :
    hit = False

    for i in range(N): # 백트레킹 하며 계란 깨기
      if n != i and eggs[i][0] > 0:
        hit = True
        eggs[i][0] -= eggs[n][1]
        eggs[n][0] -= eggs[i][1]

        crack(n + 1, eggs)

        eggs[i][0] += eggs[n][1]
        eggs[n][0] += eggs[i][1]

    if not hit: # 계란을 칠 수 없는 경우 다음 계란으로 이동
      crack(n + 1, eggs)
  
crack(0, eggs)
print(max_crack)