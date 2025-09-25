n = int(input())
q = input().split()
for i in range(n):
    x = n
    for j in range(n):
        if int(q[i]) > int(q[j]):
            x = x - 1
        elif int(q[i]) < int(q[j]):
            x = x + 1
        else:
            x = x
    if x == n:
        print(int(q[i]))
