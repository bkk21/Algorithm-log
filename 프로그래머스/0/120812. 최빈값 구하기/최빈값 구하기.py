from collections import Counter
def solution(array):
    answer = 0
    
    count = Counter(array)
    
    tmp = [x for x, y in count.items() if y == max(list(count.values()))]
    
    if len(tmp) >= 2:
        answer = -1
    else:
        answer = tmp[0]
        
        
#     count_list = list(count.values())
    
#     answer = max(count_list)
    
#     if count_list.count(answer) == 2:
#         answer = -1

    return answer