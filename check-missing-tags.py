import sys
import nltk
from libraries import files

if len(sys.argv) >= 2:
    FILE = sys.argv[1]
    reviews = files.read_from_xml(FILE)
    count = 0
    for review in reviews:
        text = review.content.split()
        for token in text:
            str_token = nltk.str2tuple(token, '/')
            if str_token[1] is None or str_token[1] == '':
                print str_token
                count += 1

    print count
else:
    print 'Invalid command.Please use the format:\n python check-missing-tags.py <filename>'
    sys.exit()