# Import some librairies
import numpy as np
import pandas as pd
import seaborn as sns
import re
from sklearn.datasets import fetch_20newsgroups
#Convert text do features
def clean_and_split_document(document):   
    words = re.sub("[^\w]", " ", document).split()
    cleaned_text = [w.lower() for w in words]    
    return cleaned_text

def all_document_tokenized(all_documents_train, all_documents_test):    
    tokens = []
    #Train document and tokens
    documents_train = []
    for document in all_documents_train:        
        document_clean = clean_and_split_document(document)
        documents_train.append(document_clean)
        tokens.extend(document_clean)
    tokens = sorted(list(set(tokens)))
    
    #test document
    documents_test = []
    for document in all_documents_test:        
        document_clean = clean_and_split_document(document)
        documents_test.append(document_clean)
    return tokens, documents_train, documents_test


def extract_feature_and_bags(all_documents_train, all_documents_test):
    tokens, documents_train, documents_test = all_document_tokenized(all_documents_train, all_documents_test)    
    data_train = []
    # Extract feature in data_test
    print("begin")
    print(len(tokens))
    for i, document in enumerate(documents_train):        
        bag_vector = np.zeros(len(tokens))
        for j, token in enumerate(tokens):
            bag_vector[j] = document.count(token)
        data_train.append(np.array(bag_vector))
    print("end 1")
    # Extract feature in data_test
    data_test = []
    for i, document in enumerate(documents_test):        
        bag_vector = np.zeros(len(tokens))
        for j, token in enumerate(tokens):
            bag_vector[j] = document.count(token)
        data_test.append(np.array(bag_vector))
    print("end")
    return tokens, np.array(data_train), np.array(data_test)
        
        
def TermFrequencies_InverseDocumentFrequency(data_train_transf, data_test_transf):
    # Term Frequencies
    print("begin1")
    #Data train
    for i, li in enumerate(data_train_transf):
        data_train_transf[i] = li/np.sum(li)
    print("end 12")
    #Data test
    for i, li in enumerate(data_train_transf):
        data_train_transf[i] = li/np.sum(li)
    print("end 13")
    # Inverse Document Frequency
    #Data train
    nb_documents = len(data_train_transf[:,0])
    nb_features = len(data_train_transf[0])
    for i in range(nb_features):
        non_zero = np.count_nonzero(data_train_transf[:,i])
        data_train_transf[:,i] = data_train_transf[:,i] * (np.log(nb_documents / non_zero) / np.log(10))
    print("end 14")
    #Data test
    nb_documents = len(data_test_transf[:,0])
    for i in range(nb_features):
        non_zero = np.count_nonzero(data_test_transf[:,i])
        if non_zero != 0:
            data_test_transf[:,i] = data_test_transf[:,i] * (np.log(nb_documents / non_zero) / np.log(10))
    print("end ...")
    return data_train_transf, data_test_transf

raw_data = fetch_20newsgroups()
# Have a Look on one data
#print(raw_data.data[6])
# Display all possible classes
print("Classes: ",raw_data.target_names)

# I choose four type of texts : talk.politics.misc, soc.religion.christian, comp.os.ms-windows.misc, rec.sport.baseball
classes = ["talk.politics.misc", "soc.religion.christian", "comp.os.ms-windows.misc", "rec.sport.baseball"]
classes = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']
#Get Train and test datas
raw_data_train = fetch_20newsgroups(subset='train', categories=classes)
raw_data_test = fetch_20newsgroups(subset='test', categories=classes)
#Shapes
print("Train data shape ", np.shape(raw_data_train.data))
print("Test data shape ", np.shape(raw_data_test.data))

#raw_data_train = ['This movie is very scary and long','This movie is not scary and is slow',
#'This movie is spooky and good']
#raw_data_test = ['Movie complee very long', 'Slow down This scary']
raw_data_train = raw_data_train.data
raw_data_test = raw_data_test.data[0:200]

#Transform Train and Test data
tokens, data_train, data_test = extract_feature_and_bags(raw_data_train, raw_data_test)
print(data_train)
data_train, data_test = TermFrequencies_InverseDocumentFrequency(data_train, data_test)

#Convert to Pandas DataFrame 
data_train = pd.DataFrame(data_train, columns=tokens)
data_test = pd.DataFrame(data_test, columns=tokens)

#Shapes email, whom I couldn't
print("Train data shape ", np.shape(data_train))
print("Test data shape ", np.shape(data_test))