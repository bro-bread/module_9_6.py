from itertools import *

def all_variants(text):
    list_tr = []
    variants = list(text)
    for i in range(len(text)):
        list_tr.append(variants[i])


    for r in range(len(text)):
        for t in range(len(text)):
            if r < t == 1:
                rrr = str(variants[r] + variants[t])
                list_tr.append(rrr)
            if t > r == 1:
                ttt = str(variants[t] + variants[r])
                list_tr.append(ttt)

    list_tr.append(text)

    for t in list_tr:
        if print(*t) != None:
            yield print(*t)


text = "abc"
fff = all_variants(text)

for nnn in fff:
    print(nnn)






