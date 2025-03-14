def solution(order):
    answer = len([x for x in str(order) if x in '369' ])
    return answer