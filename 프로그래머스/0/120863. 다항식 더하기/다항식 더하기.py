def solution(polynomial):
    answer = ''
    
    polynomial = polynomial.split()

    
    #x 수 만들기
    x_list = [x.replace('x', '') for x in polynomial if 'x' in x]
    
    num1 = 0
    for x in x_list:
        if x == '':
            num1 += 1
        else:
            num1 += int(x)
    
    #상수항 만들기
    y_list = [int(x) for x in polynomial if 'x' not in x and x != '+']
    
    num2 = sum(y_list)
    
    if num1 > 1:
        answer = str(num1) + 'x' 
    elif num1 == 1:
        answer = 'x'
    
    if num2 != 0 and num1 != 0:
        answer += ' + ' + str(num2)
    elif num2 != 0:
        answer += str(num2)
    
    
    print(answer)
    
    return answer