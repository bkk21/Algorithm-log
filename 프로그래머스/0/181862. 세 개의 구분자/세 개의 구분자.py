def solution(myStr):
    answer = []
    
    answer = [x for x in myStr.replace('b', 'a').replace('c', 'a').split('a') if x != '']
    
    if answer == []:
        answer = ["EMPTY"]

    return answer