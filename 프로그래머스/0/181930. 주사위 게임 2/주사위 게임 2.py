def solution(a, b, c):
    answer = 0
    tmp = []
    tmp.append(a)
    tmp.append(b)
    tmp.append(c)   
    tmp = set(tmp)
    
    if len(tmp) == 3:
        answer = a + b + c
    elif len(tmp) == 2:
        answer = (a + b + c) * (a*a + b*b + c*c)
    else:
        answer = (a + b + c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c)
    return answer