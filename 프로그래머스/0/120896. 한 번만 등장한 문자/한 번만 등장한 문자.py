from collections import Counter
def solution(s):
    
    count = Counter(s)
    
    answer = ''.join(sorted([x for x, y in count.items() if y == 1]))
    return answer