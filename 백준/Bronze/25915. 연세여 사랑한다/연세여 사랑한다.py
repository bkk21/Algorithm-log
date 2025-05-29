st = input()

now = ord('I')
count = 0

for i in 'LOVEYONSEI':
    count += abs(now - ord(i))
    now = int(ord(i))

count += abs(ord(st) - ord('I'))
print(count)