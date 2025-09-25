q = input().split()
n = int(q[0])
q.pop(0)
q = (''.join(q))
HEHEHE = []
for i in range((len(q)//n)):
    slise = (''.join(reversed(q[(i*n):(i*n)+n])))
    HEHEHE.append(slise)
HAHAHA = (''.join(HEHEHE))
print(HAHAHA)
