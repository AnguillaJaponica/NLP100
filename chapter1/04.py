import re

blank_blocks = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()
words = []
word_list = {}

for word in blank_blocks:
    if blank_blocks.index(word) in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
        words.append(word.strip('[,.]')[0])
    else:
        words.append(word.strip('[,.]')[:2])

for word in words:
    word_list[word] = words.index(word) + 1

word_list