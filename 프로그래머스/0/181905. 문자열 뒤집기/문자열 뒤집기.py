def solution(my_string, s, e):
    answer = ''
    
    answer = my_string[:s] + ''.join(reversed(my_string[s:e+1])) + my_string[e+1:]

    #answer = my_string[:s] + my_string[e:s-1:-1] + my_string[e+1:]
    #answer = my_string[e+1:s:-1]
    return answer