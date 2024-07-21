import sys
sys.setrecursionlimit(10**5)

def dfs(k, visit, board):
    for i in board[k]:
        if (visit[i] == False):
            visit[i] = True

            dfs(i, visit, board)


def solution(n, computers):
    board = [ [] for _ in range( n + 1 )]
    
    for i in range(n):
        for j in range(n):
            if (i != j and computers[i][j] == 1):
                board[i + 1].append(j + 1)
                
    print(*board, sep='\n')
    
    visit = [ False for _ in range(n + 1) ]
        
    answer = 0

    for i in range (1, n + 1):
        if (visit[i] == False):
            answer += 1
            visit[i] = True
            dfs(i, visit, board)
            
    
    return answer