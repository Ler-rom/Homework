Reverse = {
    'A':'A', 'H':'H', 'I':'I', 'M':'M', 'O':'O', 'T':'T', 'U':'U',
    'V':'V', 'W':'W', 'X':'X', 'Y':'Y', '1':'1', '8':'8', 'E':'3',
    '3':'E', 'J':'L', 'L':'J', 'S':'2', '2':'S', 'Z':'5', '5':'Z',
}

def mirroring(x):
    for y in x:
        if y not in Reverse:
            return 
    Rev = x.maketrans(Reverse)
    x = x.translate(Rev)
    x = x[::-1]
    return x

q = input()
palin = (q == q[::-1])
mirror = (q == mirroring(q))

if palin and mirror:
    print(f'{q} is a mirrored palindrome.')
elif palin:
    print(f'{q} is a regular palindrome.')
elif mirror:
    print(f'{q} is a mirrored string.')
else:
    print(f'{q} is not a palindrome.')
