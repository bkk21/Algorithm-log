def solution(M, N):
    answer = 0
    
    if M == 1 and N == 1:
        answer = 0
    else:
        answer = (M - 1) + (M * (N - 1))
    return answer