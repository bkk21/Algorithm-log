#이게 좀 더 간결한 방법
def solution(num_list):
    answer = []

    num_list.sort()
    answer = num_list[5:]
    return answer

# def quick(array):

#     if len(array) <= 1:
#         return array

#     pivot = array[0]
#     not_pivot = array[1:]

#     left = [x for x in not_pivot if x <= pivot]
#     right = [x for x in not_pivot if x > pivot]

#     return quick(left) + [pivot] + quick(right)
        
# def solution(num_list):
#     answer = []

#     answer = quick(num_list)[5:]
#     return answer