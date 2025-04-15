n = int(input())

numlist = list(map(int, input().split()))

answer = 0

if 1 in numlist:
    numlist.remove(1)

for i in numlist:
    for j in range(2, i):
        if i % j == 0:
            answer -= 1
            break

    answer += 1

print(answer)

    