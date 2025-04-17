n = int(input())

stlist = [[x] for x in range(51) ]

for _ in range(n):
    st = input()
    stlist[len(st)].append(st)


for i in range(51):
    stlist[i].remove(i)
    tp = list(set(stlist[i]))
    tp.sort()
    
    for j in tp:
        print(j)
