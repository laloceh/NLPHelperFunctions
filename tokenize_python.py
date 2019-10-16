#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 09:59:01 2018

@author: eduardo

https://likegeeks.com/nlp-tutorial-using-python-nltk/
"""


# Tokenize Text using Pure Python
from bs4 import BeautifulSoup
from urllib2 import urlopen
import nltk

response = urlopen('http://php.net/')
html = response.read()
#print html

soup = BeautifulSoup(html)
text = soup.get_text(strip=True)

tokens = [t for t in text.split()] 

# Count word frequency
freq = nltk.FreqDist(tokens)
 
for key,val in freq.items():
    print (str(key) + ':' + str(val))

freq.plot(20, cumulative=False)

# Remove Stop words
from nltk.corpus import stopwords 
stopwords.words('english')

clean_tokens = tokens[:]
sr = stopwords.words('english')
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
        
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    try:
        print (str(key) + ':' + str(val))
    except:
        pass
    
freq.plot(20,cumulative=False)



