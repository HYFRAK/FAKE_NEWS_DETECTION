# -*- coding: utf-8 -*-
"""Fake_News_Detection Final .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q2PknfZY2BWO8_rKJ0PUZu6hdCbpnaJR
"""

import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import nltk
import json
from nltk.corpus import stopwords
import requests
nltk.download('stopwords')
nltk.download('punkt')
stop_words = stopwords.words('english')
import warnings
warnings.filterwarnings("ignore")

f = pd.read_csv("Fake.csv")
f.insert(4, 'label', "FAKE")

r = pd.read_csv("True.csv")
r.insert(4, 'label', "REAL")

totdf = pd.concat([f,r])

labels = totdf.label

x_train, x_test, y_train, y_test = train_test_split(totdf['text'], labels, test_size = 0.2, random_state = 1)

tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)

tfidf_train=tfidf_vectorizer.fit_transform(x_train) 
tfidf_test=tfidf_vectorizer.transform(x_test)

pac=PassiveAggressiveClassifier(max_iter=50 )
pac.fit(tfidf_train,y_train)
y_pred=pac.predict(tfidf_test)
dfcheck = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

score=accuracy_score(y_test,y_pred)
print(f'Accuracy of the PAC model: {round(score*100,5)}%')

def detector1(text = None, title = None, source = None):
  if source is not None:
    with open('result.json','r') as file1:
      f = json.load(file1)
    if str(source) in f.keys():
      p = int(f[source]['fake'])*100/int(f[source]['total']) 
      print(p)

  if text is not None:
    a = r.head(1)
    a['text'] = str(text)
    tfidf_test=tfidf_vectorizer.transform(a['text'])
    y_pred=pac.predict(tfidf_test)
    print(y_pred[0])

  if title is not None:
    b = str(title)
    c = [i.lower() for i in b.split() if i not in stop_words]
    d = ""
    for i in c:
      d += i + " "
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/NewsSearchAPI"

    headers = {
      'x-rapidapi-key': "ebe0483065mshe6d76ab3df7360ap162611jsn4e19fece0593",
      'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
      }

    querystring = {"q":d,"pageNumber":"1","pageSize":"10","autoCorrect":"true","fromPublishedDate":"null","toPublishedDate":"null"}
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    resp_head = [response['value'][i]['title'] for i in range(10)]
    tot = list()
    l1 =[];l2 =[]
    X_set = set(c)
    Y_set = [{w.lower() for w in resp_head[i].split() if w not in stop_words }for i in range(10)]
    for j in Y_set:
      rvector = X_set.union(j)
      for w in rvector:
        if w in X_set: l1.append(1) # create a vector
        else: l1.append(0)
        if w in j: l2.append(1)
        else: l2.append(0)
      c = 0

      # cosine formula
      for i in range(len(rvector)):
        c+= l1[i]*l2[i]
      cosine = c / float((sum(l1)*sum(l2))**0.5)
      tot.append(cosine)
    
    for i in tot:
      if i > 0.29:
        print("REAL")
        break;
    else: print("FAKE")



