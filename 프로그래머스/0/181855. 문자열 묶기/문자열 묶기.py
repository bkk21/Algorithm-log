def solution(strArr):
    answer = 0
    
    str_list = [0] * 31
    
    for i in strArr:
        str_list[len(i)] += 1
        #print(len(i))
        
    answer = max(str_list)
    return answer