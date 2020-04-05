def n_gram(n, sequence, word_gram_flag):
    elements = []
    if word_gram_flag:
        sequence = sequence.split()
    for i in range(0, len(sequence) - n + 1):
        elements.append(sequence[i: i + n])
    return elements

x = n_gram(2, "paraparaparadise", False)
y = n_gram(2, "paragraph", False)
x_set = set(n_gram(2, "paraparaparadise", False))
y_set = set(n_gram(2, "paragraph", False))

print("和集合は{}、積集合は{}、差集合は{}です".format(x_set | y_set, x_set & y_set, x_set - y_set))

if 'se' in x or 'se' in y:
    print('yes')
else:
    print('no')
