from collections import deque

def solution(maps):
    
    global visited
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    m = len(maps[0])
    n = len(maps)

    answer = []
    
    visited = [ [ False for _ in range(m) ] for _ in range(n) ]
    
    def count_day(x, y, total):
        q = deque([[x, y]])
        
        while q:
            x, y = deque.popleft(q)
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] != 'X' and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    total += int(maps[ny][nx])
                    deque.append(q, [nx, ny])
                    
        return total
    
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j] == False:
                visited[i][j] = True
                total_day = count_day(j, i, int(maps[i][j]))
                answer.append(total_day)
            
    return sorted(answer) if len(answer) != 0 else [-1]