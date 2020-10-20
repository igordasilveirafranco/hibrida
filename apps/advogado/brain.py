import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import itertools
import time
from datetime import timedelta
from sklearn.utils import shuffle

import unidecode
from string import punctuation

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import KFold, cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import auc, roc_curve, roc_auc_score
from scipy import interp
import matplotlib.patches as patches

from string import punctuation
import pickle
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

def corrigirAcentos(texto):
    texto = unidecode.unidecode(texto)
    return texto

def corrigirAcentos(texto):
    texto = unidecode.unidecode(texto)
    return texto

stopwords = set(stopwords.words('portuguese') + list(punctuation))

def remove_stopwords(text):
    
    # remove pontuações e caracteres especiais
    chars = ['0','1','2','3','4','5','6','7','8','9','"',
             '»', '«', '’','“','\r','\n','\t','.','\'','\'',
             '?','!','$','%','^','%','"','&','*','(',')','-',
             '_','+','*','=','#',',','@',':','\\','/',',',';',
             '~','`','<','>','´','ª','¨','|','[', ']','{','}',
             '§','º','°']
    
    for c in chars:
        text = text.replace(c,' ').lower()
    text = text.split()
    stopwords = nltk.corpus.stopwords.words('portuguese')
    content = [w for w in text if w.lower().strip() not in stopwords]
    return (" ".join(content))


#########RSLP Stemmer
def Stemming(texto):
    stemmer = nltk.stem.RSLPStemmer()
    radicais=[]
    for w in texto.split():
        radicais.append(stemmer.stem(w))
    return (" ".join(radicais))


def removeStemsCurtos(text):
    text = text.split()
    content = [w for w in text if len(w) > 1 and not w.isdigit()]
    return (" ".join(content))


def preproc(textos):
    textos = textos.apply(lambda x: remove_stopwords(x)) # remove stopwords
    textos = textos.apply(lambda x: Stemming(x))         # aplica RSLP stemming
    textos = textos.apply(lambda x: corrigirAcentos(x))  # remove acentos e cedilhas
    textos = textos.apply(lambda x: removeStemsCurtos(x)) 
    return textos

def brain_analise(texto):
    
    df = pd.Series(texto)
    cwd = os.getcwd() 
    file= open(cwd+"/apps/advogado/vector",'rb')
    vectorTreino = pickle.load(file,encoding='bytes')
    file.close()
    text_proc = preproc(df)
    vectorizer = vectorTreino
    X_teste = vectorizer.transform(text_proc)
    file= open(cwd+"/apps/advogado/model_lsvm_word",'rb')
    model = pickle.load(file,encoding='bytes')
    file.close()
    y_pred =  model.predict(X_teste)
    return y_pred 

    