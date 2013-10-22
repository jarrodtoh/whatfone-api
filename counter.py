import sys
from libraries import stats, files

if len(sys.argv) >= 2:
    FILE = sys.argv[1]
    reviews = files.read_from_xml(FILE)
    doc_count, token_count = stats.corpora_stats(reviews)

    print 'Total Documents: ' + str(doc_count) + ', Total Tokens: ' + str(token_count)
else:
    print 'Invalid command.Please use the format:\n python counter.py <filename>'
    sys.exit()