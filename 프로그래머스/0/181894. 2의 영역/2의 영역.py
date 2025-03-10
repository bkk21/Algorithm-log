def solution(arr):
    answer = []
    
    if 2 in arr:
        index_list = [i for i, value in enumerate(arr) if value == 2]
        if len(index_list) > 1:
            answer = arr[index_list[0]:index_list[-1] + 1]
        else:
            answer = [arr[index_list[0]]]
    else:
        answer = [-1]
    
    return answer