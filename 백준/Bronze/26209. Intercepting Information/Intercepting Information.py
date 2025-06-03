nlist = [ x for x in map(int, input().split()) if x != 0 and x != 1]

if len(nlist) != 0:
    print("F")
else:
    print("S")