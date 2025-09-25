q, b, a = input(), int(input()), int(input())
w = list(q)
e = len(w)
r = 1
t = 0
y = 1
while r <= e :
   t = t + ((b**(r-1))*int(w[(-1)*r]))
   r = r + 1
while y <= t :
    y = y * a
y = y // a
u = []
while y > 1 :
    i = t // y
    u.append(str(i))
    t = t - (i * y)
    y = y // a
u.append(str(t))
o = int(''.join(u))
print(o)
    

