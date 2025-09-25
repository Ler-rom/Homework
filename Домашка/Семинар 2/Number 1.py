s = list(map(int, input().split()))
n = s[0]
s.pop(0)
s = sorted(s)
for i in range(n):
    if i+1 not in s:
        print(i+1)
        break
    
