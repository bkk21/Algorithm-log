dic = {')' : '(', ']':'['}
while True:
    n = input()

    if n == '.':
        break

    stack = []

    for i in n:
        if i == '(' or i == '[':
            stack.append(i)

        elif i == ')' or i == ']':
            if stack != [] and stack[-1] == dic[i]:
                stack.pop()
            else:
                stack.append(1)
                break
                
        else:
            continue

    if stack == []:
        print("yes")
        
    else:
        print("no")


        