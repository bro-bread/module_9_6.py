from itertools import *

def all_variants(text):
    variants = []
    for i in range(len(text)):
        variants.extend(product(text, repeat=i+1))
    for t in variants:
        if print(*t) != None:
            yield print(*t)


text = "abc"
fff = all_variants(text)
for variant in fff:
    print(variant)