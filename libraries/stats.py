from nltk.tokenize import RegexpTokenizer
from libraries import tags
import nltk
import itertools
from libraries import files


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


def tag_analysis(original, corrected):
    # process original reviews into tuples
    o_review_tags = []
    for o_review in original:
        for token in o_review.content.split():
            o_review_tags.append(nltk.tag.str2tuple(token))

    # remove tokens which are not tagged in original reviews
    for o in o_review_tags:
        if o[1] is None or o[1] == '':
            o_review_tags.remove(o)

    # sort and group tags in original reviews
    o_review_tags = sorted(o_review_tags)
    original_grp = [(g[0], len(list(g[1]))) for g in itertools.groupby(o_review_tags)]

    # process corrected reviews into tuples
    c_review_tags = []
    for c_review in corrected:
        for token in c_review.content.split():
            c_review_tags.append(nltk.tag.str2tuple(token))

    # sort and group tags into corrected reviews
    c_review_tags = sorted(c_review_tags)
    corrected_grp = [(g[0], len(list(g[1]))) for g in itertools.groupby(c_review_tags)]

    # ---- Start of reviews comparison ---- #
    error = 0
    new = len(c_review_tags) - len(o_review_tags)

    for c_grp in corrected_grp:
        for o_grp in original_grp:
            if o_grp[0] == c_grp[0]:  # if tags are the same
                if o_grp[1] != c_grp[1]:  # if counts are different
                    error += abs(o_grp[1] - c_grp[1])  # get the difference in absolute
                corrected_grp.remove(c_grp)
                original_grp.remove(o_grp)
                break

    # precision
    total_original_tagged = float(len(o_review_tags))
    total_correct = total_original_tagged - error
    precision = total_correct/total_original_tagged

    # recall
    total_tokens = float(len(c_review_tags))
    print total_tokens, total_original_tagged
    recall = total_correct/total_tokens

    # F1 Measure
    f1 = F1(precision, recall)

    return precision, recall, f1


def F1(precision, recall):

    f1 = 2 * ((precision * recall)/(precision + recall))

    return f1