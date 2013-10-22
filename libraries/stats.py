from nltk.tokenize import RegexpTokenizer

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