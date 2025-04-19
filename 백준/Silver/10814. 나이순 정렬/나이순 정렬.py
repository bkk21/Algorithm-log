n = int(input())

person = {}

for i in range(n):
    age, name = input().split()
    age = int(age)
    if age in person.keys():
        person[age].append(name)
    else:
        person[age] = [ name ]

#print(person)

for i in sorted(person):
    while person[i] != []:
        print(i, person[i].pop(0))



