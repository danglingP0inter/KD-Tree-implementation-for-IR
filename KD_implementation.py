In [1]:

#Importing libraries

import pandas as pd

import numpy as np

import nltk



In [2]:

#Reading first 2000 rows of the dataset

people = pd.read_csv('people_data.csv',nrows =2000)



In [4]:

#Using countvectoriser to count the freq of occurence of each word

from sklearn.feature_extraction.text import CountVectorizer

count_vect = CountVectorizer()

X_train_counts = count_vect.fit_transform(people.text)



In [5]:

#Using tf-idf to reduce the effect of common words

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer()

X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)



In [6]:

#Using tfidf as a feature

people['tfidf']=list(X_train_tfidf.toarray())



In [8]:

#Importing KDTree

from sklearn.neighbors import KDTree

kdt = KDTree(people['tfidf'].tolist(), leaf_size=3)



In [9]:

#Using KDTree to find 3 articles similar to that of Barack Obama

dist, idx = kdt.query(people['tfidf'][people['name']=='Barack Obama'].tolist(), k=3)



In [10]:

#Indices of 3 nearest articles

idx[0]



Out[10]:

array([  32,    0, 1177])



In [11]:

#Nearest neighbour 1

people['name'][32]



Out[11]:

'Barack Obama'



In [12]:

#Nearest neighbour 2

people['name'][0]



Out[12]:

'Bill Clinton'



In [13]:

#Nearest neighbour 3

people['name'][1177]



Out[13]:

'Donald Fowler'
