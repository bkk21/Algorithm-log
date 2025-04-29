n = int(input())

dic = []

for _ in range(n):
    x, y = map(int, input().split())
    dic.append((x, y))

for x, y in sorted(dic, key = lambda x:(x[0], x[1])):
    print(x, y)