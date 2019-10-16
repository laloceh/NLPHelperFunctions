#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 10:23:22 2018

@author: eduardo
https://likegeeks.com/nlp-tutorial-using-python-nltk/
"""
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
 
print(sent_tokenize(mytext))

print(word_tokenize(mytext))


#Get Synonyms from WordNet

from nltk.corpus import wordnet
 
syn = wordnet.synsets("hard")
print(syn[0].definition())
print(syn[0].examples())

for w in range(len(syn)):
    print '%s,%s' % (syn[w].definition(), syn[w].examples())


syn = wordnet.synsets("NLP") 
print(syn[0].definition())
 
syn = wordnet.synsets("Python") 
print(syn[0].definition())

syn = wordnet.synsets("Cute") 
print(syn[0].definition())
syn = wordnet.synsets("beautiful") 
print(syn[0].definition())

synonyms = []
for syn in wordnet.synsets('Computer'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
        
print(synonyms)

antonyms = []
for syn in wordnet.synsets("small"):
    for l in syn.lemmas():
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
 
print(antonyms)

# NLTK Word Stemming

from nltk.stem import PorterStemmer
 
stemmer = PorterStemmer()
print(stemmer.stem('working'))

print(stemmer.stem('running'))


# Lemmatizing Words Using WordNet

from nltk.stem import WordNetLemmatizer
 
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('increases'))

print(lemmatizer.lemmatize('playing'))
print(lemmatizer.lemmatize('playing', pos="v")) #<- For verbs 
print(lemmatizer.lemmatize('playing', pos="n")) 
print(lemmatizer.lemmatize('playing', pos="a")) 
print(lemmatizer.lemmatize('playing', pos="r"))

# Differenes between Stem and Lemmatize
print(stemmer.stem('stones'))
print(stemmer.stem('speaking'))
print(stemmer.stem('bedroom'))
print(stemmer.stem('jokes'))
print(stemmer.stem('lisa'))
print(stemmer.stem('purple'))

print('----------------------')
 
print(lemmatizer.lemmatize('stones')) 
print(lemmatizer.lemmatize('speaking')) 
print(lemmatizer.lemmatize('bedroom')) 
print(lemmatizer.lemmatize('jokes')) 
print(lemmatizer.lemmatize('lisa')) 
print(lemmatizer.lemmatize('purple'))























