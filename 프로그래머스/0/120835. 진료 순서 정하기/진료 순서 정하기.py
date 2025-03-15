def solution(emergency):
    tmp = sorted(emergency, reverse=True)
    answer = [tmp.index(x) + 1 for x in emergency]
    return answer