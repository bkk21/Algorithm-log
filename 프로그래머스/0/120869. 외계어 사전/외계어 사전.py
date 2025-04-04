def solution(spell, dic):
    answer = 2
    
    for i in dic:
        if set(i) == set(spell):
            answer = 1
            break

    return answer