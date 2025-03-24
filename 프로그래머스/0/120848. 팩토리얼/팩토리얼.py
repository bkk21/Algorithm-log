def solution(n):
    answer = 1
    result = 1
    
    while result <= n:
        answer += 1
        result *= answer
        
    return answer - 1