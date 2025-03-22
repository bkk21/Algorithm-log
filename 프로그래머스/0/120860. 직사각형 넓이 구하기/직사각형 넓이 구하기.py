def solution(dots):
    answer = 0
    x_list = []
    y_list = []
    for x in dots:
        x_list.append(x[0])
        y_list.append(x[1])
        
    answer = (max(x_list) - min(x_list)) * (max(y_list) - min(y_list))
    return answer