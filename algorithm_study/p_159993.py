from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(maps, visited, start, target):
    q = deque([start])
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps) and maps[ny][nx] != 'X' and visited[ny][nx] == -1:
                q.append([nx, ny])
                visited[ny][nx] = visited[y][x] + 1
                

def solution(maps):
    start = []
    lever = []
    end = []
    
    for m in range(len(maps)):
        if 'S' in maps[m]:
            start = [maps[m].index('S'), m]
        if 'L' in maps[m]:
            lever = [maps[m].index('L'), m]
        if 'E' in maps[m]:
            end = [maps[m].index('E'), m]
            
    # print(f'start: {start}, lever: {lever}, end: {end}')
    
    time = 0
    visited = [ [ -1 for _ in range(len(m))] for m in maps ]
    visited[start[1]][start[0]] = 0
    bfs(maps, visited, start, lever)
            
    if visited[lever[1]][lever[0]] == -1:
        return -1

    time += visited[lever[1]][lever[0]]
    
    visited = [ [ -1 for _ in range(len(m))] for m in maps ]
    visited[lever[1]][lever[0]] = 0
    
    bfs(maps, visited, lever, end)
    
    if visited[end[1]][end[0]] == -1:
        return -1

    time += visited[end[1]][end[0]]
    
    return time