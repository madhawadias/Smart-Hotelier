#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 23:52:10 2020

@author: madhawadias
"""

from collections import Counter
import nltk
from nltk import ngrams
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
from nltk.tokenize import word_tokenize

# Reading the tsv 
pd.set_option('display.max_colwidth', 2000)
reviewtxt = pd.read_csv('shangrila-tripadvisor.tsv', encoding='ISO-8859-1')
reviews_column = reviewtxt['review']

# Converting pandas datafram to text
review_str = reviews_column.to_string()
review_str = review_str.lower()

# Tokenization
review_str = word_tokenize(review_str)

# Removing Stop words
stopwords_custom = ['lanka', 'sri',  'nan', '!', '...', '..', '.', ',']
tokens_without_sw = [word for word in review_str if not word in stopwords.words('english')]
tokens_without_sw = [word for word in tokens_without_sw if word not in stopwords_custom]

freq = nltk.FreqDist(tokens_without_sw)
for key,val in freq.items():
    if val>10 :
        print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)
# Aspect Score
def calculate_score():
    review_count = reviewtxt['review'].count()
    print(review_count)
    
    staff_score = 0
    print('caring = ', review_str.count('caring')) 
    staff_score += review_str.count('caring')
    print('good staff = ', review_str.count('good staff'))
    staff_score += review_str.count('good staff')
    print('good service = ', review_str.count('good service'))
    staff_score += review_str.count('good service')
    print('great service = ', review_str.count('great service'))
    staff_score += review_str.count('great service')
    print('friendly staff = ', review_str.count('friendly staff'))
    staff_score += review_str.count('friendly staff')
    print('not friendly = ', review_str.count('not friendly'))
    staff_score -= review_str.count('not friendly')
    print('rude = ', review_str.count('rude'))
    staff_score -= review_str.count('rude')
    print('bad service = ', review_str.count('bad service'))
    staff_score -= review_str.count('bad service')
    print('=============================')
    print('STAFF SCORE = ', staff_score, '  ', staff_score/review_count*100)
    print('=============================')
    
    location_score = 0
    print('good location = ', review_str.count('good location')) 
    location_score += review_str.count('good location')
    print('great location = ', review_str.count('great location')) 
    location_score += review_str.count('great location')
    print('shopping = ', review_str.count('shopping')) 
    location_score += review_str.count('shopping')
    print('=============================')
    print('LOCATION SCORE = ', location_score, '  ', location_score/review_count*100)
    print('=============================')
    
    food_score = 0
    print('good food = ', review_str.count('good food')) 
    food_score += review_str.count('good food')
    print('great food = ', review_str.count('great food')) 
    food_score += review_str.count('great food')
    print('good restaurant = ', review_str.count('good restaurant')) 
    food_score += review_str.count('good restaurant')
    print('bad food = ', review_str.count('bad food')) 
    food_score -= review_str.count('bad food')
    print('terrible food = ', review_str.count('terrible food')) 
    food_score -= review_str.count('terrible food')
    print('=============================')
    print('FOOD SCORE = ', food_score, '  ', food_score/review_count*100)
    print('=============================')
    
    room_score = 0
    print('good room = ', review_str.count('good room')) 
    room_score += review_str.count('good room')
    print('great room = ', review_str.count('great room')) 
    room_score += review_str.count('great room')
    print('clean = ', review_str.count('clean')) 
    room_score += review_str.count('clean')
    print('good sound proofing = ', review_str.count('good sound proofing')) 
    room_score += review_str.count('good sound proofing')
    print('good wifi = ', review_str.count('good wifi')) 
    room_score += review_str.count('good wifi')
    print('bad wifi = ', review_str.count('bad wifi')) 
    room_score -= review_str.count('bad wifi')
    print('noise = ', review_str.count('noise')) 
# =============================================================================
#     room_score -= review_str.count('noise')
# =============================================================================
    print('poor sound proofing = ', review_str.count('poor sound proofing')) 
    room_score -= review_str.count('poor sound proofing')
    print('=============================')
    print('ROOM SCORE = ', room_score, '  ', room_score/review_count*100)
    print('=============================')
    
    value_score = 0
    print('good value = ', review_str.count('good value')) 
    value_score += review_str.count('good value')
    print('great value = ', review_str.count('great value')) 
    value_score += review_str.count('great value')
    print('value for money = ', review_str.count('value for money')) 
    value_score += review_str.count('value for money')
    print('expensive = ', review_str.count('expensive')) 
    value_score -= review_str.count('expensive')
    print('not worth = ', review_str.count('not worth')) 
    value_score -= review_str.count('not worth')
    print('=============================')
    print('VALUE SCORE = ', value_score, '  ', value_score/review_count*100)
    print('=============================')

calculate_score()

# Converting list to String
listToStr = ' '.join([str(elem) for elem in tokens_without_sw])

# ngrams
ngram_counts = Counter(ngrams(listToStr.split(), 3))
ngram_counts.most_common(50)

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def show_wordcloud(data, title = None):
    wordcloud = WordCloud(
        background_color = 'white',
        max_words = 200,
        max_font_size = 40, 
        scale = 3,
        random_state = 42
    ).generate(str(data))

    fig = plt.figure(1, figsize = (10, 10))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize = 20)
        fig.subplots_adjust(top = 2.3)

    plt.imshow(wordcloud)
    plt.show()
    
# print wordcloud
show_wordcloud(tokens_without_sw)
