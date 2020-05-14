# Natural Language Processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import nltk
from IPython.display import display
nltk.download('stopwords')
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

# Importing the dataset
dataset = pd.read_csv('data/kingsbury-tripadvisor.csv',  encoding='ISO-8859-1')
dataset = dataset.replace(np.nan, '', regex=True)
rows = len(dataset.index)
rows

# library to clean data 
import re  
  
# Natural Language Tool Kit 
import nltk   
  
# to remove stopword 
from nltk.corpus import stopwords 
  
# for Stemming propose  
from nltk.stem.porter import PorterStemmer 
  
# Initialize empty array 
# to append clean text  
corpus = []  
negative_corpus = []
score_series = pd.Series([]) 

review_series = pd.Series([]) 
dataframe = pd.DataFrame()
score_neg_series = pd.Series([])

## Get sentiment analysis of reviews. 

def compund_sentiment(tweets):
    vadersenti = analyser.polarity_scores(tweets)
    result = pd.Series([vadersenti['pos'], vadersenti['neg'], vadersenti['neu'], vadersenti['compound']])
    compund_value = result[3]
    return compund_value

# 1000 (reviews) rows to clean 
for i in range(0, rows):  
      
    # column : "Review", row ith 
    review = re.sub('[^a-zA-Z]', ' ', str(dataset['review'][i]) ) 
      
    # convert all cases to lower cases 
    review = review.lower()  
      
    # split to array(default delimiter is " ") 
    review = review.split()  
      
    # creating PorterStemmer object to 
    # take main stem of each word 
    ps = PorterStemmer()  
      
    # loop for stemming each word 
    # in string array at ith row     
    review = [ps.stem(word) for word in review 
                if not word in set(stopwords.words('english'))]  
                  
    # rejoin all string array elements 
    # to create back into a string 
    review = ' '.join(review)   
    sentiment_score = compund_sentiment(review) 
    score_series[i] = sentiment_score
     
    
    if sentiment_score < 0 :
        negative_corpus.append(review)
        review_series[i] = review
        score_neg_series[i] = sentiment_score
    
    # append each string to create 
    # array of clean text  
    corpus.append(review)

    
dataset.insert(4, "score", score_series)
dataset.head()

dataframe.insert(0, "review", review_series)
dataframe.insert(1, "score", score_neg_series)
dataframe.head()




def plot_distribution(df, col):
    print('Unique value of {}:'.format(col))
    display(df[col].unique())
    print('Number of unique value of {}: {}\n'.format(col, len(df[col].unique())))
    
    fig, ax = plt.subplots(figsize=(10,5))
    sns.set_style(style='whitegrid')
    feature = df[col]
    _ = feature.plot.hist(ax=ax, bins=15, colors=['#cec3c6'])
    mean_line = ax.axvline(x=feature.mean(), linewidth=2, color='black', label='mean {:.2f}'.format(
        feature.mean()))
    median_line = ax.axvline(x=feature.median(), linewidth=2, color='red', label='median {:.2f}'.format(
        feature.median()))
    _ = ax.legend(handles=[mean_line, median_line])
    _ = ax.set_title('Histogram of polarity', fontsize='x-large')
    
    plt.show()
    
plot_distribution(dataset, 'score')


dataset[dataset["score"] <= 5].sort_values("score", ascending = True)[["review", "score"]].head(30)



str_reviews = dataframe['review'].astype(str).values.tolist()

stopwords_custom = ['shangri','la','shangri la','event','colombo','visit','night','floor','hotel']

from wordcloud import WordCloud

def show_wordcloud(data, title = None):
    wordcloud = WordCloud(
        stopwords = stopwords_custom,
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
show_wordcloud(dataframe)











