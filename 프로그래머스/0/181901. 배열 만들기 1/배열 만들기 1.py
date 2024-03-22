def solution(n, k):
    answer = []
    for j in range(n+1):
        if j == 0:
            continue
        elif j % k == 0:
            answer.append(j)
    return answer