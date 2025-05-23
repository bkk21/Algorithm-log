while 1:
    m = input().lower()

    if m == '#':
        break

    print(len([ x for x in m if x in ['a', 'e', 'i', 'o', 'u'] ]))