def solution(diffs, times, limit):
    
    def check_level(level):
        total_time = []
        
        for d, t, index in zip(diffs, times, range(len(diffs))):
            
            if d <= level:
                total_time.append(t)
            
            else:
                total_time.append((d - level) * (t + times[index-1]) + t)

        return sum(total_time) <= limit
        
    
    l_level = 1
    r_level = 100000
    
    while r_level >= l_level:
        
        if r_level == l_level:
            if check_level(l_level):
                return l_level
            else:
                return l_level + 1
        
        level = (l_level + r_level) // 2 + 1
        
        if check_level(level):
            r_level = level - 1
        else:
            l_level = level + 1
    
    return l_level