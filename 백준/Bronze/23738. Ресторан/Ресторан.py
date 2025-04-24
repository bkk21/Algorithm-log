n = input()

answer = ''
for i in n:
    if i == 'B':
        answer += 'v'
    elif i == 'E':
        answer += 'ye'
    elif i == 'H':
        answer += 'n'
    elif i == 'P':
        answer += 'r'
    elif i == 'C':
        answer += 's'
    elif i == 'Y':
        answer += 'u'
    elif i == 'X':
        answer += 'h'
    else:
        answer += i

print(answer.lower())