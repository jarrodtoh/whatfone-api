import nltk

s = 'this is a sentence.. please tokenize it. thanks!'

ss = nltk.word_tokenize(s)
print nltk.pos_tag(ss)