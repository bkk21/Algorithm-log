def solution(myString):
    answer = [x for x in myString.split('x') if x != '']
    
    
#     answer = myString.split('x')
    
#     for i in answer:
#         if i == '':
#             answer.remove(i)
    
    answer.sort()
    return answer