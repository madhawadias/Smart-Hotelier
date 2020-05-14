# Natural Language Processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
nltk.download('stopwords')

# Importing the dataset
dataset = pd.read_csv('shangrila-tripadvisor.tsv',  encoding='ISO-8859-1')
dataset = dataset.replace(np.nan, '', regex=True)

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
score = []

## Get sentiment analysis of reviews. 

def compund_sentiment(tweets):
    vadersenti = analyser.polarity_scores(tweets)
    result = pd.Series([vadersenti['pos'], vadersenti['neg'], vadersenti['neu'], vadersenti['compound']])
    compund_value = result[3]
    return compund_value

# 1000 (reviews) rows to clean 
for i in range(0, 1549):  
      
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
    score.append(sentiment_score)
    if sentiment_score < 0 :
        negative_corpus.append(review)
    dataset['score'] = sentiment_score
    # append each string to create 
    # array of clean text  
    corpus.append(review)



# Creating the Bag of Words model 
from sklearn.feature_extraction.text import CountVectorizer 
  
# To extract max 1500 feature. 
# "max_features" is attribute to 
# experiment with to get better results 
cv = CountVectorizer(max_features = 1549)  
  
# X contains corpus (dependent variable) 
X = cv.fit_transform(corpus).toarray() 
  
# y contains answers if review 
# is positive or negative 
y = dataset.iloc[:, 1].values  

# Splitting the dataset into 
# the Training set and Test set 
from sklearn.model_selection import train_test_split 
  
# experiment with "test_size" 
# to get better results 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25) 


# Fitting Random Forest Classification 
# to the Training set 
from sklearn.ensemble import RandomForestClassifier 

# n_estimators can be said as number of 
# trees, experiment with n_estimators 
# to get better results 
model = RandomForestClassifier(n_estimators = 501, criterion = 'entropy') 


model.fit(X_train, y_train) 

# Predicting the Test set results 
y_pred = model.predict(X_test) 
  
y_pred 

# Making the Confusion Matrix 
from sklearn.metrics import confusion_matrix 
  
cm = confusion_matrix(y_test, y_pred) 
  
cm 
###### T E S T I N G ######

def precision(label, confusion_matrix):
    col = confusion_matrix[:, label]
    return confusion_matrix[label, label] / col.sum()
    
def recall(label, confusion_matrix):
    row = confusion_matrix[label, :]
    return confusion_matrix[label, label] / row.sum()

def precision_macro_average(confusion_matrix):
    rows, columns = confusion_matrix.shape
    sum_of_precisions = 0
    for label in range(rows):
        sum_of_precisions += precision(label, confusion_matrix)
    return sum_of_precisions / rows

def recall_macro_average(confusion_matrix):
    rows, columns = confusion_matrix.shape
    sum_of_recalls = 0
    for label in range(columns):
        sum_of_recalls += recall(label, confusion_matrix)
    return sum_of_recalls / columns

print("label precision recall")
for label in range(10):
    print(f"{label:5d} {precision(label, cm):9.3f} {recall(label, cm):6.3f}")

print("precision total:", precision_macro_average(cm))

print("recall total:", recall_macro_average(cm))



from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

def print_sentiment_scores(tweets):
    vadersenti = analyser.polarity_scores(tweets)
    result = pd.Series([vadersenti['pos'], vadersenti['neg'], vadersenti['neu'], vadersenti['compound']])
    return result

text = 'Bad room, smelly interior, unpleasent staff'

print_sentiment_scores(text)






















# Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)