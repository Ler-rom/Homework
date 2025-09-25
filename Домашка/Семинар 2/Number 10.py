with open("семинар 2/input_10.txt", "r+", encoding="utf-8") as f:
    text = f.read()

text = text.split()
code = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']
fintext = []

for i in range(len(text)):
    word = list(text[i])

    for j in range(1,len(word)):
        get = 0
        got = 0

        for n in range(9):
            if word[j] == code[n]:
                get = 1
                got = 1
                break

        if get == 1:
            for m in range(9):
                if word[j-1] == code[m]:
                    got = 0

        if got == 1:
            word[j] = word[j] + 'с' + word[j]

    finword = ''.join(word)
    fintext.append(finword)
fintext = ' '.join(fintext)

with open('семинар 2/output_10.txt', 'w', encoding="utf-8") as write:
    write.writelines(fintext)
        
    
    
     
