def solution(n, k):
    answer = []
    for j in range(1, n+1):
        if j % k == 0:
            answer.append(j)
    return answer