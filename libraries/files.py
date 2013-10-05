from xml.etree.ElementTree import Element, SubElement
from xml.etree import ElementTree
from xml.dom import minidom
import re

from models.models import *


def export_to_xml(reviews, filename):
    """
    Method takes in list of reviews and export to XML with preferred filename
    """

    # define xml format
    root = Element('reviews') # set root element
    for rev in reviews: # crawl each review
        doc = SubElement(root, 'doc', {'id': str(rev.id)}) # doc as 2nd level
        # third level - attributes of doc
        attr_source = SubElement(doc, 'source')
        attr_source.text = rev.source
        attr_date = SubElement(doc, 'date')
        attr_date.text = rev.date
        attr_title = SubElement(doc, 'title')
        attr_title.text = rev.title
        attr_review = SubElement(doc, 'text')
        attr_review.text = rev.content

    # format the xml
    new_doc = prettify(root)
    text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)
    pretty_xml = text_re.sub('>\g<1></', new_doc)

    # output to xml
    file = open(filename, 'w')
    file.write(pretty_xml)
    file.close()


def prettify(elem):
    """
    Internal method for xml export - helps to indent elements
    """

    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def read_from_xml(source):
    """
    Method reads the XML file and extract data into review objects
    """

    tree = ElementTree.parse(source)
    root = tree.getroot() # locate the root
    doc = root.findall('doc') # get all "doc" tags

    reviews = [] # to collect all the Review objects

    for d in doc:
        # extract data from xml
        id = d.attrib['id']
        source = d.find('source').text if d.find('source').text != None else ''
        date = d.find('date').text
        title = d.find('title').text if d.find('title').text != None else ''
        content = d.find('text').text

        # save to object
        new_review = Review(id, source, date, title, content)

        # add to collection
        reviews.append(new_review)

    return reviews


def general_export(content, filename):
    """
    Method is for general exporting of data into file
    """

    file = open(filename, 'w')
    file.write(content)
    file.close()