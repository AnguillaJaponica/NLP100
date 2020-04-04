import re

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
word_list = []

for str in sentence.split():
    word_list.append(str.strip('[,.]'))
