import sys
from libraries import stats, files

if len(sys.argv) >= 3:
    FILE_1 = sys.argv[1]
    FILE_2 = sys.argv[2]
    train_reviews = files.read_from_xml(FILE_1)
    corrected_reviews = files.read_from_xml(FILE_2)
    precision, recall, f1 = stats.tag_analysis(train_reviews, corrected_reviews)

    print 'Precision: ' + str(precision) + '\nRecall: ' + str(recall) + '\nF1: ' + str(f1)
else:
    print 'Invalid command.Please use the format:\n python analyze-tags.py <trained_file> <corrected_file>'
    sys.exit()