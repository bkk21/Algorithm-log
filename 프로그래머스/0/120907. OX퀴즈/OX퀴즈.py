def solution(quiz):
    answer = []
    for i in quiz:
        tmp = i.split()
        
        if tmp[1] == '+':
            answer.append("O" if int(tmp[0]) + int(tmp[2]) == int(tmp[4]) else "X")
        else:
            answer.append("O" if int(tmp[0]) - int(tmp[2]) == int(tmp[4]) else "X")
        

        
    return answer