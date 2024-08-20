def solution(edges):
    graph = {}
    circle = 0
    eight = 0
    stick = 0
    
    for e in edges:
        a, b = e
        
        if a not in graph.keys():
            graph[a] = [[], [b]]
        else :
            graph[a][1].append(b)
            
        if b not in graph.keys():
            graph[b] = [[a], []]
        else :
            graph[b][0].append(a)
    
    point = 1
            
    for node in graph.keys():
        if len(graph[node][1]) == 0:
            stick += 1
        elif len(graph[node][1]) == 1:
            continue
        elif len(graph[node][1]) == 2:
            if len(graph[node][0]) > 0:
                eight += 1
            else:
                point = node
        else:
            point = node
        
    answer = [point, len(graph[point][1]) - stick - eight, stick, eight]
    return answer