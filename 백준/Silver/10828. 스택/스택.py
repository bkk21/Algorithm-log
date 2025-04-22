n = int(input())

nlist = []

for _ in range(n):
    m = input()

    if 'push' in m:
        nlist.append(m.split()[1])
        continue

    if m == 'size':
        print(len(nlist))
        continue

    if m == 'empty':
        if nlist == []:
            print('1')
            continue
        else:
            print('0')
            continue

    if m == 'top':
        try:
            print(nlist[-1])
            continue
        except:
            print('-1')
            continue

    try:
        print(nlist.pop())
    except:
        print('-1')

    