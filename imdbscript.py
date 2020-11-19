#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd

#data processing 
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer


# In[3]:


movies = pd.read_csv("IMDB_Movies.csv")
print(movies['text'].iloc[10])


# In[4]:


print(movies['label'].value_counts())


# In[14]:


#data cleaning

stop_words = set(stopwords.words('english'))
filtered_sent = []

for index, row in movies.iterrows():
    #remove punctuation first
    movies.at[index, 'text'] = re.sub(r"\W", " ", movies.at[index, 'text'])
    
    #remove the numbers
    movies.at[index, 'text'] = re.sub(r"\d+", "", movies.at[index, 'text'])
    
    #remove the extra spaces
    movies.at[index, 'text'] = re.sub(r"\s+", " ", movies.at[index, 'text'])
    
    #make all words lower case
    movies.at[index, 'text'] = str(movies.at[index, 'text']).lower()
    
    #tokenize that sentence
    movies.at[index, 'text'] = nltk.word_tokenize(movies.at[index, 'text'])
    
    for w in movies.at[index, 'text']:
        if w not in stop_words:
            filtered_sent.append(w)
            
    movies.at[index, 'text'] = filtered_sent
    filtered_sent = []
            


# In[16]:


print(movies['text'].iloc[10])


# In[22]:


#lemmitization
lemmatizer = WordNetLemmatizer() 

for index, row in movies.iterrows():
    newWords = []
    
    for word in movies.at[index, 'text']:
        newWords.append(lemmatizer.lemmatize(word, pos = "v"))
        
    
    movies.at[index, 'text'] = " ".join(newWords)
    


# In[23]:


print(movies['text'].iloc[10])


# In[24]:


cv = CountVectorizer(max_features = 200, lowercase = False)

x = cv.fit_transform(movies['text']).toarray()
y = movies['label'].values

header = cv.get_feature_names()


# In[25]:


output = pd.DataFrame(x, columns = header)
output['label'] = movies['label']

print(output.head())


# In[26]:


output.to_csv("IMDBspmatrix.csv", index = False)

