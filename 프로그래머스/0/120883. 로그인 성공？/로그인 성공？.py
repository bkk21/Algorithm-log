def solution(id_pw, db):
    answer = ''
    db_dic = {}
    
    for i in db:
        db_dic[i[0]] = i[1]
        
    print(db_dic)
    
    if id_pw[0] not in db_dic.keys():
        answer = 'fail'
        
    elif db_dic[id_pw[0]] == id_pw[1]:
        answer = 'login'
    
    else:
        answer = 'wrong pw'
                
    return answer