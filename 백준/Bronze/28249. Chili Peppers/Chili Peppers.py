dic = {'Poblano' : 1500, 'Mirasol':6000, 'Serrano':15500, 'Cayenne':40000, 'Thai':75000, 'Habanero': 125000}

sum = 0

n = int(input())

for _ in range(n):
    sum += dic[input()]

print(sum)