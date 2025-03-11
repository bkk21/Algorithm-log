def solution(arr):
    answer = []
    
    for i in range(len(arr), 10000000):
        if i & (i-1) == 0:
            break
        else:
            arr.append(0)
    return arr