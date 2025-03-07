def solution(arr, queries):
    answer = []
    
    for num1 in range(len(queries)):

        min = 1000000
        for num2 in range(queries[num1][0], queries[num1][1]+1):
            if arr[num2] > queries[num1][2] and arr[num2] < min:
                min = arr[num2]
            
        if min == 1000000:
            answer.append(-1)
        else:
            answer.append(min)
        
    return answer