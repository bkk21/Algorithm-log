def solution(numbers, k):
    answer = 0

    now = 1
    count = 0
    
    while count != k - 1:
        if now + 2 > len(numbers):
            now = now + 2 - len(numbers)
            answer = now
            count += 1
        else:
            now += 2
            answer = now
            count += 1
        
    return answer