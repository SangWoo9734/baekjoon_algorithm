import sys

input = sys.stdin.readline

K = int(input())

lh, lw, sq = 0, 0, 0
direction_history = {}
sq_target = []
is_curved = False

direction = {
  1: 4,
  2: 3,
  3: 1,
  4: 2,
} # 남 -> 동 -> 북 -> 서 -> 남

order = [list(map(int, input().split())) for _ in range(6)]
order.append(order[0])

for index in range(6):
  cur_dir, length = order[index]

  if cur_dir == 1 or cur_dir == 2:
    lw = max(lw, length)

  else:
    lh = max(lh, length)

  if direction[cur_dir] != order[index + 1][0]:
    sq = length * order[index + 1][1]

total_square = lh * lw - sq

print( K * total_square )
