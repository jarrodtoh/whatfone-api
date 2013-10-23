import sys
from libraries import stats, files

if len(sys.argv) >= 3:
    FILE_1 = sys.argv[1]
    FILE_2 = sys.argv[2]
    train_reviews = files.read_from_xml(FILE_1)
    corrected_reviews = files.read_from_xml(FILE_2)
    count, error = stats.tag_corrected(train_reviews, corrected_reviews)

    print 'Total Corrected Tags: ' + str(count) + '\nError Review ID(s): ' + str(error)
else:
    print 'Invalid command.Please use the format:\n python counter.py <filename>'
    sys.exit()