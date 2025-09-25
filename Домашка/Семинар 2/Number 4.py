'''q = input().split()
ans = []
for i in range(len(q)-(len(q) % 2)):
    if i % 2 == 0:
        ans.append(q[i+1])
    else:
        ans.append(q[i-1])
if len(q) % 2 != 0:
    ans.append(q[-1])
print(''.join(ans))
'''


q = input().split()
ans = [(q[i+1]) if i % 2 == 0 else (q[i-1]) for i in range(len(q)-(len(q) % 2))]
print(' '.join(ans if len(q) % 2 == 0 else ans+[q[-1]]))
