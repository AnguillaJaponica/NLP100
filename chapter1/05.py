def n_gram(n, sequence, word_gram_flag):
    elements = []
    if word_gram_flag:
        sequence = sequence.split()
    for i in range(0, len(sequence) - n + 1):
        elements.append(sequence[i: i + n])
    return elements