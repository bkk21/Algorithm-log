from collections import Counter
from math import *

def solution(a, b, c, d):
    answer = 0
    count = Counter([a, b, c, d])
    
    #1, 1, 1, 1 케이스
    if max(count.values()) == 1:
        answer = min(a, b, c, d)
        
    #1, 1, 2, 2 케이스
    elif 2 in count.values() and len(count.values()) == 2:
        list2 = [x for x, y in count.items() if y == 2]
        answer = (list2[0] + list2[1]) * abs((list2[0] - list2[1]))
        
    #1, 1, 1, 2 케이스
    elif 3 in count.values():
        p = [x for x, y in count.items() if y == 3]
        q = [x for x, y in count.items() if y == 1]
        answer = (10 * p[0] + q[0])**2
        
    #1, 1, 2, 3 케이스
    elif max(count.values()) == 2 and len(count.values()) == 3:
        list1 = [x for x, y in count.items() if y == 1]  
        answer = list1[0] * list1[1]
        
    #1, 2, 3, 4
    elif max(count.values()) == 4:
        answer = 1111 * a
    

    return answer