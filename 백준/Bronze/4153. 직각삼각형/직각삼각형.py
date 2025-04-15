while True:
    numlist = list(map(int, input().split()))

    if 0 in numlist:
        break

    numlist.sort()

    c = numlist.pop()
    a = numlist.pop()
    b = numlist.pop()
    
    if a*a + b*b == c*c:
        print("right")
    else:
        print("wrong")