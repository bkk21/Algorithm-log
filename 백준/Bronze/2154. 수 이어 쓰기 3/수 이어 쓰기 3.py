n = int(input())

st = ''.join([str(i) for i in range(1, n+1)])
print(st.index(str(n)) + 1)