import sys
from libraries import files, tags


def check_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if len(sys.argv) >= 5:
    NUM_OF_TRAIN = sys.argv[1]
    if check_int(NUM_OF_TRAIN):
        NUM_OF_TRAIN = int(NUM_OF_TRAIN)
        next_index = 0

        TRAIN_FILES = []
        while next_index < NUM_OF_TRAIN:
            TRAIN_FILES.append(sys.argv[(next_index+2)])
            next_index += 1

        TEST_FILE = sys.argv[(NUM_OF_TRAIN + 2)]
        OUTPUT_FILE = sys.argv[(NUM_OF_TRAIN + 3)]

        train_reviews = []
        for TRAIN_FILE in TRAIN_FILES:
            train_reviews.extend(files.read_from_xml(TRAIN_FILE))

        test_reviews = files.read_from_xml(TEST_FILE)
        output_reviews = tags.tag_by_training(train_reviews, test_reviews)
        files.export_to_xml(output_reviews, OUTPUT_FILE)
    else:
        print 'Argument[1] must be an integer.'
else:
    print 'Invalid command.Please use the format:\n python trained-tag-trainer.py <train_file> <test_file> <output_file>'
    sys.exit()