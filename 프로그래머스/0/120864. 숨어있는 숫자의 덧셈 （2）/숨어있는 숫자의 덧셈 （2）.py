def solution(my_string):
    answer = 0
    
    tmp = ''
    for i in my_string:
        if i.isalpha():
            tmp += '_'
        else:
            tmp += i
    
    tmp = tmp.split('_')
    
    answer = sum([int(x) for x in tmp if x != ''])

    
    return answer