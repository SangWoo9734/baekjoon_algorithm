# from collections import deque
# def solution(land):
#     M = len(land[0])
#     N = len(land)
    
#     oil_dict = {}
    
#     for m in range(M):
#         oil_dict[m] = 0
        
#         visited = [ [ False for _ in range(M) ] for _ in range(N) ]
#         for n in range(N):
            
#             if land[n][m] == 1 and  visited[n][m] == False:
#                 visited[n][m] = True
#                 count = bfs(land, visited, m, n)
#                 oil_dict[m] += count
    
#     return max(oil_dict.values())

# def bfs(land, visited, x, y):
#     M = len(land[0])
#     N = len(land)
    
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
    
#     q = deque([[x, y]])
#     count = 1
    
#     while q:
#         x, y = q.popleft()
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if 0 <= nx < M and 0 <= ny < N and land[ny][nx] == 1 and visited[ny][nx] == False:
#                 visited[ny][nx] = True
#                 q.append([nx, ny])
#                 count += 1
    
#     return count

from collections import deque
def solution(land):
    global visited
    M = len(land[0])
    N = len(land)
    
    visited = [ [ -1 for _ in range(M) ] for _ in range(N) ]
    
    oil_dict = []
    oil_index = 0
    
    for m in range(M):
        for n in range(N):
            if land[n][m] == 1 and  visited[n][m] == -1:
                visited[n][m] = oil_index
                count = bfs(land, m, n, oil_index)                
                oil_dict.append(count)
                oil_index += 1
                
    oil_total = []
    for m in range(M):
        oil_count = set()
        for n in range(N):
            if visited[n][m] != -1:
                oil_count.add(visited[n][m])
        
        oil_total.append(sum([oil_dict[k] for k in oil_count ]))
    return max(oil_total)

def bfs(land, x, y, oil_index):
    M = len(land[0])
    N = len(land)
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    q = deque([[x, y]])
    count = 1
    visited_col = [x]
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N and land[ny][nx] == 1 and visited[ny][nx] == -1:
                visited[ny][nx] = oil_index
                q.append([nx, ny])
                count += 1
    
    return count