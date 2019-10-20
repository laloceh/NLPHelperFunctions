#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 18:14:42 2019

@author: eduardo
"""
from textblob import TextBlob
import nltk
from nltk.corpus import wordnet
import re

def remove_repeated_characters(sentence):
    tokens = nltk.word_tokenize(sentence)
    
    repeat_pattern = re.compile(r'(w*)(\w)\2(\w*)')
    match_substitution = r'\1\2\3'
    def replace(old_word):
        if wordnet.synsets(old_word):
            return old_word
        new_word = repeat_pattern.sub(match_substitution, old_word)
        return replace(new_word) if new_word != old_word else new_word
    
    correct_tokens = [replace(word) for word in tokens]
                      
    good_sentence = " ".join(correct_tokens)
    return good_sentence

def correct_spelling(sentence):
    s = TextBlob(sentence.lower())
    s = s.correct()
    return s
    

sample_sentence = "My schooooll is realllllyyyy amazzziiiing"

# First, remove repeated tokens
sample_sentence = remove_repeated_characters(sample_sentence)
print sample_sentence

# Second, correct spelling
sample_sentence = correct_spelling(sample_sentence)
print sample_sentence

