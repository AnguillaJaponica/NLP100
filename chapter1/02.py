str1 = 'パトカー'
str2 = 'タクシー'

extracted = []
for i in range(0, 4):
    extracted.append(str1[i])
    extracted.append(str2[i]) 

print(''.join(extracted))