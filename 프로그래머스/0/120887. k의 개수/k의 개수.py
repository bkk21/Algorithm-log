def solution(i, j, k):
    answer = sum([str(x).count(str(k)) for x in range(i, j+1) if str(k) in str(x)])
    print(answer)
    return answer