import sys
from libraries import files, tags

if len(sys.argv) >= 3:
    TRAIN_FILE = sys.argv[1]
    OUTPUT_FILE = sys.argv[2]

    reviews = files.read_from_xml(TRAIN_FILE)
    trained_reviews = tags.default_tag(reviews)
    files.export_to_xml(trained_reviews, OUTPUT_FILE)

else:
    print 'Invalid command.Please use the format:\n python default-tag-trainer.py <input_file> <output_file>'
    sys.exit()