def solution(n):
    answer = 0
    
    #n까지 중에서 소수 개수 찾기
    for i in range(n+1):
        if len([x for x in range(1, i+1) if i % x == 0]) == 2:
            answer += 1
    
    #전체에서 소수의 개수를 빼면 합성수의 개수 (1도 제외해야 하기 때문에 -1)
    return n - answer - 1