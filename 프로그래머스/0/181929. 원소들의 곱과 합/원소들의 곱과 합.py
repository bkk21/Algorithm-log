def solution(num_list):
    g = 1
    h = 0
    
    for i in num_list:
        g =  g*i
        h += i

    
    if h**2 > g:
        return 1
    else:
         return 0