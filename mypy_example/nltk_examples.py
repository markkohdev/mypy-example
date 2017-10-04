from nltk import word_tokenize, pos_tag

sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""

tokens = word_tokenize(sentence)
print(tokens)

# This will fail!
# will_fail = nltk.word_tokenize(['this is wrong'])

tagged = pos_tag(tokens)
print(tagged[0:6])
