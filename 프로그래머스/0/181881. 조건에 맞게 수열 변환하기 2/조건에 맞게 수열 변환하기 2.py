def solution(arr):
    answer = 0
    x = 0
    
    #이전 꺼
    tmp = arr.copy()
    
    while True:
        
        #실행한 거
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] / 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
        x += 1
        
        if tmp == arr:
            break
        
        tmp = arr.copy()
    
            
    return x - 1