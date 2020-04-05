import random

words = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .".split()
transformed = []

for w in words:
    if len(w) > 4:
        str = ''.join(random.sample(list(w[1:-1]), len(w) - 2))
        transformed.append('{}{}{}'.format(w[0], str, w[-1]))
    else:
        transformed.append(w)

print(transformed)
