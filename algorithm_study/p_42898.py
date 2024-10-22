from collections import deque

def check_puddles(puddles, target):
    tx, ty = target
    
    for p in puddles:
        px, py = p
        if tx == px - 1 and ty == py - 1:
            return True
    
    return False

def solution(m, n, puddles):
    
    dx = [0, 1]
    dy = [1, 0]
    
    dp = [ [ [0, 0] for _ in range(m) ] for _ in range(n) ]
    
    q = deque([[0, 0]])
    
    while q:
        x, y = deque.popleft(q)
        
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and not check_puddles(puddles, [nx, ny]):
                cur_cost, cur_count = dp[y][x]
                next_cost, next_count = dp[ny][nx]
                
                if (dp[ny][nx][0] == 0 or dp[ny][nx][0] > dp[y][x][0] + 1):
                    dp[ny][nx] = [cur_cost + 1, cur_count if cur_count else 1]
                    deque.append(q, [nx, ny])
                elif dp[ny][nx][0] == dp[y][x][0] + 1:
                    dp[ny][nx] = [ next_cost,  (next_count + cur_count) % 1000000007]
                else:
                    continue
                    
    
    return dp[n - 1][m - 1][1]