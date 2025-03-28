# from itertools import combinations
# def solution(numbers):
#     answer = 0
#     num_list = combinations(numbers, 2)
    
#     for i in num_list:
#         print(answer, i[0] * i[1])
#         if answer < i[0] * i[1]:
#             answer = i[0] * i[1]
    
#     return answer

def solution(numbers):
    numbers.sort(reverse=True)
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])