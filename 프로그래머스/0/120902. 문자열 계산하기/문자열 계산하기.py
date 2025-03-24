def solution(my_string):
    answer = 0
    new = my_string.split()
    
    print(new)
    
    answer += int(new[0])
    
    for i in range(1, len(new), 2):
        if new[i] == '+':
            answer += int(new[i+1])
        else:
            answer -= int(new[i+1])
        
    return answer