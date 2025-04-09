def solution(dots):
    #초기 설정
    answer = 0
    
    #1번 case
    if (dots[1][0] - dots[0][0]) / (dots[1][1] - dots[0][1]) == (dots[3][0] - dots[2][0]) / (dots[3][1] - dots[2][1]):
        answer = 1
        
    #2번 case
    elif (dots[2][0] - dots[0][0]) / (dots[2][1] - dots[0][1]) == (dots[3][0] - dots[1][0]) / (dots[3][1] - dots[1][1]):
        answer = 1
        
    #3번 case
    elif (dots[3][0] - dots[0][0]) / (dots[3][1] - dots[0][1]) == (dots[2][0] - dots[1][0]) / (dots[2][1] - dots[1][1]):
        answer = 1

    return answer