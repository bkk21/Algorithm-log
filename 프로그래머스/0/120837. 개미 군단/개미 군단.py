def solution(hp):
    answer = 0
    hp_list = [5, 3, 1]
    
    for i in hp_list:
        answer += hp // i
        hp = hp % i
    return answer