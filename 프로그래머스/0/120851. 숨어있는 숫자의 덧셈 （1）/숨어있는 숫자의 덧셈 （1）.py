def solution(my_string):
    answer = 0
    
    tmp = [ x for x in my_string if not x.isalpha() ]
    
    answer = sum([int(x) for x in tmp])
    return answer