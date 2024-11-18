import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, -1 ,1]

while (True):
  L, R, C = map(int, input().split())
  if sum([L, R, C]) == 0: break

  building = []
  floor = []
  s_position = []
  e_position = []

  time = []
  for l in range(L):
    f = [ [ 0 for _ in range(C) ] for _ in range(R) ]
    time.append(f)

  while True:
    row = input().rstrip()

    if row == '': 
      building.append(floor)
      floor = []
    else:
      if 'S' in row:
        s_position = [len(building), len(floor), row.index('S')]
      if 'E' in row:
        e_position = [len(building), len(floor), row.index('E')]
      floor.append(row)

    if len(building) == L:
      break

  q = deque([ s_position ])

  while q:
    z, y, x = deque.popleft(q)

    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]

      if 0 <= nx < C and 0 <= ny < R and 0 <= nz < L and time[nz][ny][nx] == 0 and building[nz][ny][nx] != "#":
        time[nz][ny][nx] = time[z][y][x] + 1
        deque.append(q,[nz, ny, nx])

  ez, ey, ex = e_position

  if time[ez][ey][ex] == 0:
    print('Trapped!')
  else :
    print(f'Escaped in {time[ez][ey][ex]} minute(s).')