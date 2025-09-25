q = input().split()
n = 0
for i in range(len(q)):
    v = q.count(q[i])
    if v > n:
        n = int(q[i])
print(n)
