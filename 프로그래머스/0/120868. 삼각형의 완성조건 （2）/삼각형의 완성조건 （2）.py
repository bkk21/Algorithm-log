def solution(sides):
    answer = 0
    
    #case1 - 긴 변 없음
    for i in range(max(sides), sum(sides)):
        answer += 1
    
    #case2 - 긴 변 있음
    for i in range(max(sides) - min(sides) + 1, max(sides)):
        answer += 1
    
    
    return answer