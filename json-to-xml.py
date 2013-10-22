import json
import sys

from models.models import *
from libraries.files import *


# read json
if len(sys.argv) == 2:
    json_data = open('data/' + sys.argv[1])
    data = json.load(json_data)

    id_count = 1 # initial id count
    reviews = []

    # store records into objects
    for record in data:
        source = ''
        date = record['date']
        title = ''
        content = ''
        for row in record['review']:
            row = re.sub('\r\n', '', row)
            row = row.strip()
            content += row.encode('ascii', 'ignore') + ' '
        content = content.lower().strip()

        new_review = Review(id_count, source, date, title, content)

        id_count += 1
        reviews.append(new_review)

    export_to_xml(reviews, 'data/reviews.xml')
else:
    print "Error! Please input in the following format:\n python json-to-xml.py json_file"