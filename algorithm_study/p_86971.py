from collections import deque

def bfs(graph, visited, x, count):
    q = deque([x])
    
    while q:
        idx = q.popleft()
        
        for i in graph[idx]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)
                count += 1
    
    return count
    
    
def solution(n, wires):
    answer = 100
    
    for i in range(len(wires)):
        new_wires = []
        for j in range(len(wires)):
            if i != j:
                new_wires.append(wires[j])
        
        visited = [ False ] * (n + 1)
        count = []
        
        graph = [ [] for _ in range(n + 1) ]
            
        for w in new_wires:
            x, y = w
            graph[x].append(y)
            graph[y].append(x)

        for x in range(1, n + 1):
            if visited[x] == False:
                visited[x] = True
                count.append(bfs(graph, visited, x, 1))

        answer = min(answer, abs(count[0] - count[1]))
    return answer