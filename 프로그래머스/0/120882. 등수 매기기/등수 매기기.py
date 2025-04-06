import pandas as pd
def solution(score):
    
    answer = []
    
    #평균 리스트 생성
    avg_list = []
    
    #평균 계산
    for i in score:
        avg_list.append(sum(i) / 2)
    
    #데이터 프레임 활용
    avg_pd = pd.DataFrame({'avg':avg_list})
    answer = list(avg_pd['avg'].rank(method='min', ascending=False))
    
    
    return answer