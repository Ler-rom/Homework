q = open('tyu.txt')
w = q.readlines()
e = w[0].split()
r = len(e) - 1
t = 1
y = int(e[0])
if w[1] == '+' :
   while t <= r :
       y = y + int(e[t])
       t = t + 1
elif w[1] == '-' :
    while t <= r :
       y = y - int(e[t])
       t = t + 1
else:
    while t <= r :
       y = y * int(e[t])
       t = t + 1
q.close()
u = open('tyuAnswer.txt', 'w')
u.write(str(y))
u.close()
