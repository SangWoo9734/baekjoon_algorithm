from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = {}
    for w in words:
        visited[w] = False
    
    q = deque([(begin, 0)])
    
    while q:
        cur, count = q.popleft()
        
        if cur == target:
            return count
        
        visited_word = [ w for w in words if visited[w] == False ]
        
        for nw in visited_word:
            match_count = 0
            for i in range(len(nw)):
                if nw[i] == cur[i]:
                    match_count += 1
                    
            if match_count == len(nw) - 1:
                visited[nw] = True
                q.append((nw, count + 1))
                
    return 0