from collections import Counter

def solution(points, routes):
    
    answer = 0
    route_detail = []
    max_length = 0
    
    for r in routes:
        path = []
        

        for p in range(len(r) - 1):
            sr, sc = points[r[p] - 1]
            er, ec = points[r[p + 1] - 1]

            while sr != er:
                path.append((sr, sc))
                sr = sr - 1 if sr > er else sr + 1
                
            while sc != ec:
                path.append((sr, sc))
                sc = sc - 1 if sc > ec else sc + 1
            
        path.append((sr, sc))
        route_detail.append(path)
        max_length = max(max_length, len(path))

    for i in range(max_length):
        cur_points = [ ]
        for x in route_detail: 
            if len(x) > i:
                cur_points.append(x[i])
                
        pointer_counter = Counter(cur_points)
        
        
        for c in pointer_counter.values():
            if c > 1:
                answer += 1
        
    return answer