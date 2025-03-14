def solution(n):
    answer = 0
    
    answer = sum([x for x in range(n + 1) if x % 2 == 0])
    return answer