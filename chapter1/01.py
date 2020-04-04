str = 'パタトクカシーー'
extracted = []
for i in range(0, len(str) - 1):
    if i % 2 == 0:
            extracted.append(str[i])

print(''.join(extracted))