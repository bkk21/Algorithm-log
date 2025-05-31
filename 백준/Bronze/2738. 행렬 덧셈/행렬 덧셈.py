n, m = map(int, input().split())

nlist = [] 


for _ in range(n):
    nlist.append(list(map(int, input().split())))

for i in range(n):
    tmp = list(map(int, input().split()))
    
    for j in range(len(tmp)):
        tmp[j] = tmp[j] + nlist[i][j]
        print(tmp[j], end = ' ')

    print()

