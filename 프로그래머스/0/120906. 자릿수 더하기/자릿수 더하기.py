def solution(n):
    answer = 0
    
    #print(str(n))
    answer = sum(int(i) for i in str(n))
    return answer