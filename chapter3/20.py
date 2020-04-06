# coding:utf-8
import json
import gzip

def wiki_reader(title, json_data):
    with gzip.open(json_data, 'r') as f:
        for line in f:
            obj = json.loads(line)
            if obj['title'].encode('utf-8') == title:
                print(obj['text'])
wiki_reader('イギリス', 'data/jawiki-country.json.gz')