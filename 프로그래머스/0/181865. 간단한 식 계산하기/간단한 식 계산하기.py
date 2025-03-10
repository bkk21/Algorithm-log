def solution(binomial):
    answer = 0
    
    if binomial.split()[1] == '+':
        answer = int(binomial.split()[0]) + int(binomial.split()[2])

    elif binomial.split()[1] == '-':
        answer = int(binomial.split()[0]) - int(binomial.split()[2])
        
    elif binomial.split()[1] == '*':
        answer = int(binomial.split()[0]) * int(binomial.split()[2])
    return answer