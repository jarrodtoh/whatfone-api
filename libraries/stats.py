from nltk.tokenize import RegexpTokenizer
from libraries import tags
import nltk


def corpora_stats(reviews):
    """
    Return the document count and token count
    """

    # init stats
    doc_count = 0
    token_count = 0

    for review in reviews:
        tokenizer = RegexpTokenizer(r'\w+')  # detects only word, ignore punctuations
        content_tokens = tokenizer.tokenize(review.content)
        doc_count += 1
        token_count += len(content_tokens)

        if token_count > 10000:
            print review.id
            break

    return doc_count, token_count


def tag_corrected(original, corrected):
    count = 0 # total corrected tags
    error = [] # list of review ids with error

    for (o_review, c_review) in zip(original, corrected):
        o_review_tags = []
        for token in o_review.content.split():
            o_review_tags.append(nltk.tag.str2tuple(token))

        c_review_tags = []
        for token in c_review.content.split():
            c_review_tags.append(nltk.tag.str2tuple(token))

        if len(o_review_tags) != len(c_review_tags):
            error.append(o_review.id)
        else:
            for (o_tag, c_tag) in zip(o_review_tags, c_review_tags):
                if o_tag != c_tag:
                    count += 1

    return count, error