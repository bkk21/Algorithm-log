import pandas as pd
def solution(score):
#     answer = []
#     avg_dic = {}
    
#     for i in score:
#         avg_dic[str(score.index(i) + 1)] = sum(i) / 2
    
#     print(avg_dic)
#     sort_avg = sorted(avg_dic.values(), reverse=True)
#     print(sort_avg)
    
#     for i in range(len(sort_avg)):
#         if sort_avg.count(avg_dic[str(i + 1)]) >= 2:
#             answer.append(sort_avg.index(avg_dic[str(i + 1)]) + sort_avg.count(avg_dic[str(i + 1)]) - 1)
#         else:
#             answer.append(sort_avg.index(avg_dic[str(i + 1)]) + 1)
    
    answer = []
    avg_list = []
    for i in score:
        avg_list.append(sum(i) / 2)
    
    avg_pd = pd.DataFrame({'avg':avg_list})
    answer = list(avg_pd['avg'].rank(method='min', ascending=False))
    
    
    return answer