import string

def solution(l, r):
    answer = []
    
    five_zero = ["0", "5"]
    
    for i in range(l, r+1):
        target = str(i)
        
        status = []
        
        for x in target:
            if x in five_zero:
                status.append(1)
            else:
                status.append(0)
        
        if 0 not in status:
            answer.append(i)
            
    if answer == []:
        answer.append(-1)
    return answer