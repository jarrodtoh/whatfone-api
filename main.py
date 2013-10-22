from libraries import stats, files

reviews = files.read_from_xml('data/2/test2.xml')
doc_count, token_count = stats.corpora_stats(reviews)

print 'Total Documents: ' + str(doc_count) + ', Total Tokens: ' + str(token_count)