def solution(arr, queries):
    answer = []
    
    for num1 in range(len(queries)):
        
        for num2 in range(queries[num1][0], queries[num1][1] + 1):
            if num2 % queries[num1][2] == 0:
                arr[num2] += 1
                
    answer = arr
    return answer