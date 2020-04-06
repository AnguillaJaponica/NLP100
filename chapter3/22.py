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

def is_category(string):
    return re.match(r'^\[\[Category:+\]\]', string)

def main():
    text = wiki_reader('イギリス', 'data/jawiki-country.json.gz').split('\n')
    for line in text:
        if is_category(line):
            print(line)

main()