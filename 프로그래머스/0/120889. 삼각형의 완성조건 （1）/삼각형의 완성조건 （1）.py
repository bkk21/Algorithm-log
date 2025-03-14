def solution(sides):
    answer = 0
    sides.sort()
    if sides[-1] < sum(sides[:2]):
        answer = 1
    else:
        answer = 2
    return answer