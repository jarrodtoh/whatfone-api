import sys
from libraries import files, tags

if len(sys.argv) >= 4:
    TRAIN_FILE = sys.argv[1]
    TEST_FILE = sys.argv[2]
    OUTPUT_FILE = sys.argv[3]

    train_reviews = files.read_from_xml(TRAIN_FILE)
    test_reviews = files.read_from_xml(TEST_FILE)
    output_reviews = tags.tag_by_training(train_reviews, test_reviews)
    files.export_to_xml(output_reviews, OUTPUT_FILE)

else:
    print 'Invalid command.Please use the format:\n python trained-tag-trainer.py <train_file> <test_file> <output_file>'
    sys.exit()