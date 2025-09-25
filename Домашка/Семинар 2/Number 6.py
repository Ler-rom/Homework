q = input().split()
ans = [] #Список с ответом. В задаче он не используется.
for i in range(len(q)):
    if q.count(q[i]) == 1:
        ans.append(q[i])
print(' '.join(ans))
