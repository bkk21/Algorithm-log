n = int(input())
answer = n
for i in range(n, 0, -1):
    if i + sum([int(j) for j in str(i)]) == int(n):
        if i <= n:
            answer = i

if answer == n:
    answer = 0
print(answer)