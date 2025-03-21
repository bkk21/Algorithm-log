from itertools import permutations
import math

def solution(numbers):
    answer = 0
    
    num_list = []
    
    # 조합 만들기
    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            if int(''.join(j)) not in num_list:
                num_list.append(int(''.join(j)))

    # 소수 개수 판별 추가
    for num in num_list:
        if num > 1 and all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            answer += 1

    return answer
