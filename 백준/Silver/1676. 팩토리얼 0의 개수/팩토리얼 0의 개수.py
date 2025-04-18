import math
n = int(input())

answer = str(math.factorial(n))

answer = answer[::-1]

noindex = [x for x in range(len(answer)) if answer[x] != '0' ][0]

answer = answer[:noindex].count('0')

print(answer)