import sys
from collections import deque

input = sys.stdin.readline

dx = [ 1, 0, 0, -1, 0, 0]
dy = [ 0, 1, 0, 0, -1, 0]
dz = [ 0, 0, 1, 0, 0, -1]

while True:
  user_input = input().rstrip()

  if user_input == '0 0 0':
    break

  L, R, C = map(int, user_input.split())
  S = [0, 0, 0]
  E = [0, 0, 0]

  building = [[] for _ in range(L)]
  f_index = 0
  while f_index < L:
    building_row = input().rstrip()
    
    if building_row == '':
      f_index += 1
    else:
      if 'S' in building_row:
        S = [building_row.index('S'), len(building[f_index]), f_index]
      if 'E' in building_row:
        E = [building_row.index('E'), len(building[f_index]), f_index]

      building[f_index].append(building_row)

  timer = []
  for _ in range(L):
    t_floor = []
    for _ in range(R):
      t_floor.append([ 0 for _ in range(C) ])
    
    timer.append(t_floor)

  q = deque([S])
  sx, sy, sz = S

  while q:
    x, y, z = deque.popleft(q)

    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]

      if 0 <= nx < C and 0 <= ny < R and 0 <= nz < L and ( timer[nz][ny][nx] == 0 or timer[nz][ny][nx] > timer[z][y][x] + 1 )  and (building[nz][ny][nx] == '.' or building[nz][ny][nx] == 'E'): 
        timer[nz][ny][nx] = timer[z][y][x] + 1
        deque.append(q, [nx, ny, nz])

  ex, ey, ez = E

  if timer[ez][ey][ex] > 0:
    print(f'Escaped in {timer[ez][ey][ex]} minute(s).')
  else:
    print('Trapped!')

