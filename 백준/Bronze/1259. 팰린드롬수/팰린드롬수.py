while True:
    n = input()
    if int(n) == 0:
        break
        
    else:
        y = 1
        for i in range(len(n)):
            if n[i] != n[len(n) - 1 - i]:
                y = 0
                break

        if y == 0:
            print("no")
        else:
            print("yes")