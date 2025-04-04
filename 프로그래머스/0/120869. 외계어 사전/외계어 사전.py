def solution(spell, dic):
    answer = 2
    
    for i in dic:
        if set(i) == set(spell) and len(i) == len(spell):
            answer = 1
            break

    return answer