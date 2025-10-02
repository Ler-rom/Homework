s = input().split()
n = int(s[0])
symb = s[1]
if n % 2 == 0:
    for i in range(n//2):
        print((i+1)*symb)
    for i in range(n//2, 0, -1):
        print(i*symb)
else:
    for i in range((n+1)//2):
        print((i+1)*symb)
    for i in range((n-1)//2, 0, -1):
        print((i)*symb)
