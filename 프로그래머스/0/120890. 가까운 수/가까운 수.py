def solution(array, n):
    answer = 0
    
    array.append(n)
    array.sort()
    
    print(array)
    print(array.index(n))
    
    n_index = array.index(n)

    if n_index == 0:
        answer = array[1]
    elif n_index == len(array) - 1:
        answer = array[-2]
    elif array[n_index] -  array[n_index - 1] < array[n_index + 1] - array[n_index]:
        answer =  array[n_index - 1]
    elif array[n_index] -  array[n_index - 1] > array[n_index + 1] - array[n_index]:
        answer = array[n_index + 1]
    else:
        answer = array[n_index - 1]
    
    
    return answer