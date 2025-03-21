def solution(sizes):
    answer = 0
    
    x = []
    y = []
    
    for i in sizes:
        
        x.append(max(i))
        y.append(min(i))
            
    answer = max(x) * max(y)
    return answer