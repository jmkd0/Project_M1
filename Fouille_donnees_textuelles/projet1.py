# Import some librairies
import numpy as np
import pandas as pd
import seaborn as sns
import re
from matplotlib import pyplot as plt
from sklearn.datasets import fetch_20newsgroups

#Convert text do features
def all_document_tokenized(all_documents):    
    tokens = []
    # document and tokens
    documents = []
    for document in all_documents:   
        document = document.lower()
        document = re.sub("[^\w]", " ", document)
        documents.append(document)
        tokens.extend(document.split())
    tokens = sorted(list(set(tokens)))
    return tokens, documents


def CountVectorizerOwn(all_documents):
    tokens, documents = all_document_tokenized(all_documents)  
    data = []
    # Extract feature in data
    for i, document in enumerate(documents):
        bag_vector = np.zeros(len(tokens))
        for j, token in enumerate(tokens):
            bag_vector[j] = document.split().count(token)
        data.append(np.array(bag_vector))
        print(i)
    return np.array(data)
        
        
def TfidfTransformerOwn(data):
    # Term Frequencies
    #Data 
    for i, li in enumerate(data):
        data[i] = li/np.sum(li)
        print(i)
        
    # Inverse Document Frequency
    #Data train
    nb_documents = len(data[:,0])
    nb_features = len(data[0])
    for i in range(nb_features):
        non_zero = np.count_nonzero(data[:,i])
        data[:,i] = data[:,i] * (np.log(nb_documents / non_zero) / np.log(10))
        print(i)
        
    return data

def TextProcessing(raw_data, method):
    if(method == "my_own"):
        #Transform Data
        data = CountVectorizerOwn(raw_data)
        #print(data)
        data = TfidfTransformerOwn(data)
    elif method == "scikit-learn":
        data = CountVectorizer().fit_transform(raw_data)
        tf_transformer = TfidfTransformer(use_idf=False).fit(data)
        data = tf_transformer.transform(data)
    return data

    

# I choose four type of texts : talk.politics.misc, soc.religion.christian, comp.os.ms-windows.misc, rec.sport.baseball
classes = ["talk.politics.misc", "soc.religion.christian", "comp.os.ms-windows.misc"]
raw_data = fetch_20newsgroups(categories=classes)
#Shapes
#print("Train data shape ", np.shape(raw_data.data))

data = TextProcessing(raw_data.data[:500], "my_own")
print(data)