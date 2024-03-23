def solution(arr1, arr2):
    answer = 0
    tmp_x = 0
    tmp_y = 0
    
    for i in arr1:
        tmp_x += i
        
    for i in arr2:
        tmp_y += i

    if len(arr1) != len(arr2):
        if len(arr1) < len(arr2):
            answer = -1
        else:
            answer = 1
    else:
        if tmp_x > tmp_y:
            answer = 1
        elif tmp_x < tmp_y:
            answer = -1
        else:
            answer = 0
            
    return answer