from utils.helper import load_model,split_symptoms
from logging_.logger import setup_logging
from exception.custom_exception import custom_exception
from Data_validation.data_validation import prediction_input
from utils.helper import load_model_data
from nltk.corpus import stopwords
import pandas as pd 
import re
import sys
import logging
import pickle



model_data=load_model_data()
drugs_name=[]
for i in model_data['drug_name']:
    drugs_name.append(str(i).lower())

stopword=stopwords.words('english')
stopword=stopword + drugs_name # made stopwords and name to be remove

stopword=stopword + ['(','hive',';',',',')','.','hives','+','/']

def input_cleaning(text:prediction_input):
    try:
        setup_logging('intiating input data cleaning',logging.INFO)
        filtered_words = [word for word in re.split(r'[,\./;()\s]+', text.symptoms) if word not in stopword]
        result=' '.join(filtered_words)
        return result
    except Exception as e : 
        raise custom_exception(e,sys)
    


def data_transform(result:str):
    try:
        setup_logging('trying to split data',logging.INFO)
        inp=split_symptoms(text=result)
        return inp
    except Exception as e : 
        raise custom_exception(e,sys)

def convert_into_numberic(inp):
    try:
        setup_logging('converting the data into numbers',logging.INFO)
        ob=load_model('final_models/original_enc.pkl')
        arr=ob.transform([inp])
        return arr
    except Exception as e : 
        raise custom_exception(e,sys)