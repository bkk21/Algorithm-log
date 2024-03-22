def solution(num_list):
    answer = 0
    if len(num_list) < 11:
        for i in range(len(num_list)):
            if i == 0:
                answer = num_list[i]
            else:
                answer *= num_list[i]
                
    else:
        for i in num_list:
            answer += i
    return answer