from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    
    cost = [ [ 0 for _ in range(m) ] for _ in range(n) ]
    
    q = deque([[0, 0]])
    cost[0][0] = maps[0][0]
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1 and ( cost[ny][nx] == 0 or cost[ny][nx] + 1 < cost[y][x]):
                cost[ny][nx] = cost[y][x] + 1
                deque.append(q, [nx, ny])
    
    
    return cost[n - 1][m - 1] if  cost[n - 1][m - 1] != 0 else -1