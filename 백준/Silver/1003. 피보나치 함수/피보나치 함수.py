n = int(input())

nlist = [[0, 0]] * 41

nlist[0] = [1, 0]
nlist[1] = [0, 1]

for _ in range(n):
    t = int(input())

    for i in range(2, t+1):
        nlist[i] = [nlist[i-1][0] + nlist[i-2][0], nlist[i-1][1] + nlist[i-2][1]]

    print(nlist[t][0], nlist[t][1])