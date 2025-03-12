import numpy as np
def solution(array):
    answer = 0
#     array.sort()
    
#     answer = array[len(array) // 2]
    
    answer = np.median(array)

    return answer