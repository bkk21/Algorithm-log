numlist = list(map(int, input().split()))


print(sum([ i*i for i in numlist ]) % 10)