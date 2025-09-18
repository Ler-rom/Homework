q = open('input.txt')
w = q.readlines()
q.close()
# Разбили все числа на строки в массиве.
e = w[0].split()
# t - это основание системы.
r = w[2].split()
t = int(r[0])

u = len(e) # u - кол-во чисел.
i = [] # i - пустой массив для переведенных в десятичное основание чисел.

o = 0
while u > 0: # Перевод чисел в десятичную систему.
    p = list(e[o])
    z = len(p)
    a = 1
    summ = 0
    while a <= z:
        summ = summ + ((t**(a-1))*int(p[(-1)*a]))
        a = a + 1
    i.append(str(summ))
    o = o + 1
    u = u - 1
    
# Проводимая операция.
d = len(i) - 1
f = 1
g = int(i[0])
if w[1] == '+':
    while f <= d:
       g = g + int(i[f])
       f = f + 1
elif w[1] == '-':
    while f <= d:
       g = g - int(i[f])
       f = f + 1
else:
    while f <= d:
       g = g * int(i[f])
       f = f + 1

# Перевод в основание R. Подсчёт кол-ва разрядов.
h = 1
while h <= g:
    h = h * t
h = h // t

y = []
# Сам перевод.
while h > 1:
    j = g // h
    y.append(str(j))
    g = g - (j * h)
    h = h // t
y.append(str(g))
k = int(''.join(y))
l = open('output.txt', 'w')
l.write(str(k))
l.close()
