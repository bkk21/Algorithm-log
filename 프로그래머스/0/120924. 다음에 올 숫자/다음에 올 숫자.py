def solution(common):
    answer = 0
    
    try:
        if common[1] / common[0] == common[2] / common[1]:
            answer = common[-1] * (common[1] / common[0])
        else:
            answer = common[-1] + (common[1] - common[0])
    except:
        answer = common[-1] + (common[1] - common[0])
    
#     #등비
#     if common[1] % common[0] == 0 and common[2] % common[1] == 0:
#         answer = fini * (common[1] // common[0])
#     else:
#         answer = fini + (common[1] - common[0])
        
#         #print(answer)
        
    return answer