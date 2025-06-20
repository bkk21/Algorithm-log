from collections import Counter

s = input()

nlist = [str(s.count(i)) for i in 'abcdefghijklmnopqrstuvwxyz']

k = ' '.join(nlist)

print(k)