import nltk
from libraries import files

reviews = files.read_from_xml('data/3/corrected3.xml')
count = 0
for review in reviews:
    text = review.content.split()
    for token in text:
        str_token = nltk.str2tuple(token, '/')
        if str_token[1] is None or str_token[1] == '':
            print str_token
            count += 1

print count