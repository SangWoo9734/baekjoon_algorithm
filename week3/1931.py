import sys

# input = sys.stdin.readline

N = int(input())

room_schedule = []
for _ in range(N):
  s, e = map(int, input().split())
  room_schedule.append([e, s])

room_schedule.sort()

# room_schedule = [ list(map(int, input().split())) for _ in range(N) ]
# room_schedule = sorted(room_schedule, key=lambda x: [x[1], x[0]])

cur = room_schedule[0]
count = 1
for r in room_schedule[1:]:
  if cur[0] <= r[1]:
    count += 1
    cur = r

print(count)