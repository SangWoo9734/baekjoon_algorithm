import sys
from collections import deque

input = sys.stdin.readline

S = int(input())


def bfs():
  count = 0
  q = deque([[1, 0, 0]])

  visited = [ [False] * 1001 for _ in range(1001) ]
  visited[1][0] = True

  while q:
    emotion_count, clip_board, count = q.popleft()

    if emotion_count == S:
      print(count)
      return
    
    # 저장
    if visited[emotion_count][emotion_count] == False:
      visited[emotion_count][emotion_count] = True
      q.append([emotion_count, emotion_count, count + 1])


    # 지우기
    if emotion_count - 1 > 0 and visited[emotion_count - 1][clip_board] == False:
      visited[emotion_count - 1][clip_board] = True
      q.append([emotion_count - 1, clip_board, count + 1])

    # 붙여넣기
    if 0 < emotion_count + clip_board < 1001 and visited[emotion_count + clip_board][clip_board] == 0 :
      visited[emotion_count + clip_board][clip_board] = True
      q.append([emotion_count + clip_board, clip_board, count + 1])

bfs()