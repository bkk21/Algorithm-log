def solution(n):
    answer = []

    for i in range(2, n+1):
        while n % i == 0:
            if n % i == 0:
                if i not in answer: 
                    answer.append(i)
                    
                n = n // i
                print(n)
        if n == 1:
            break
            
    return answer