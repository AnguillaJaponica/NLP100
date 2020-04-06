# coding:utf-8
import json
import gzip
import re

def wiki_reader(title, json_data):
    with gzip.open(json_data, 'r') as f:
        for line in f:
            obj = json.loads(line)
            if obj['title'].encode('utf-8') == title:
                return obj['text']

def is_section(string):
    return re.match(r'^=.*=$', string)

def main():
    text = wiki_reader('イギリス', 'data/jawiki-country.json.gz').split('\n')
    for line in text:
        count = 0
        if is_section(line):
            for s in line:
                if s == '=':
                    count += 1
                else:
                    break
            print('セクション名:{} レベル:{}'.format(line[count:-count].encode('utf-8'), count - 1))

main()