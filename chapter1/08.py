import re

def cipher(str):
    transformed = []
    for s in str:
        if re.compile(r'[a-z]').search(s):
            transformed.append(chr(219 - ord(s)))
        else:
            transformed.append(s)
    return transformed

print(''.join(cipher('ho5efuTapiyo')))
