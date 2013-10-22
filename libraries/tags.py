import nltk
from libraries import files

def default_tag(reviews):
    """
    Return the reviews with default tag
    """

    for review in reviews:
        text = nltk.word_tokenize(review.content)
        tagged_tokens = nltk.pos_tag(text)
        tagged_content = ''
        for token in tagged_tokens:
            str_token = nltk.tuple2str(token, '/')
            tagged_content += str_token + ' '
        review.content = tagged_content.strip()

    return reviews

def tag_by_training(trained_reviews, test_reviews):
    """
    Train the trained reviews into Tagger Model, and tag test_reviews to be returned
    """

    train_sent = []
    for review in trained_reviews:  # iterate each review
        for part in nltk.sent_tokenize(review.content):  # split review content into sentences
            sent = []
            for token in part.split():  # split sentence into tokens
                sent.append(nltk.tag.str2tuple(token))  # change tagged-token format to tuple
            train_sent.append(sent)  # append sentence into trained sentences array
            #print sent

    unigram_tagger = nltk.UnigramTagger(train_sent)

    for test_review in test_reviews:
        tagged_tokens = unigram_tagger.tag(test_review.content.split())
        tagged_content = ''
        for token in tagged_tokens:
            str_token = nltk.tuple2str(token, '/')
            tagged_content += str_token + ' '
        test_review.content = tagged_content.strip()

    return test_reviews