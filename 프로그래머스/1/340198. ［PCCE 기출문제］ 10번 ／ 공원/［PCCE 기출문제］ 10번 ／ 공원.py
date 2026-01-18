def solution(mats, park):
    answer = -1

    n = len(park)
    m = len(park[0])

    mats.sort(reverse=True)

    for size in mats:
        for i in range(n - size + 1):
            for j in range(m - size + 1):

                can_place = True

                for x in range(i, i + size):
                    for y in range(j, j + size):
                        if park[x][y] != "-1":
                            can_place = False
                            break
                    if not can_place:
                        break

                if can_place:
                    return size

    return answer
