import sys

input = sys.stdin.readline

N, M = map(int, input().split())

r, c, d = map(int, input().split())

room = [ list(map(int, input().split())) for _ in range(N) ]
clean_map = [ [False for _ in range(M) ] for _ in range(N) ]

clean = 0

dx = [ 0, 1, 0, -1 ]
dy = [ -1, 0, 1, 0 ]


def is4WayDirty(r, c, room):
  for i in range(4):
    nr = r + dy[i]
    nc = c + dx[i]
    if  0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0 and clean_map[nr][nc] == False:
      return True
    
  return False

while True:
  if (clean_map[r][c] == False):
    clean_map[r][c] = True
    clean += 1

  if (is4WayDirty(r, c, room)): 
      d = 3 if d == 0 else d - 1 #반시계 90도 회전
      nr = r + dy[d]
      nc = c + dx[d]
    
      if(room[nr][nc] == 0 and clean_map[nr][nc] == False):
        r = nr
        c = nc
      
  
  else: # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    move_direction = (d + 2) % 4 
    nr = r + dy[move_direction]
    nc = c + dx[move_direction]

    # # 바라보는 방향을 유지한 채로 한 칸 후진
    if  0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0: 
      r = nr
      c = nc

    else:
      break


print(clean)