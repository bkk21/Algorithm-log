def solution(a, b):
    answer = 0
    tmp = str(a) + str(b)
    if 2 * a * b < int(tmp):
        answer = int(tmp)
    else:
        answer = 2 * a * b
    return answer