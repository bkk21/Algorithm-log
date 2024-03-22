def solution(a, b):
    answer = 0
    if 2 * a * b < int(str(a) + str(b)):
        answer = int(str(a) + str(b))
    else:
        answer = 2 * a * b
    return answer