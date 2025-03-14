def solution(n):
    answer = 0
    
    num1 = n ** 0.5
    if num1 - int(num1) == 0:
        answer = 1
    else:
        answer = 2
        
    return answer