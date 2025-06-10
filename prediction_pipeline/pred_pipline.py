from logging_.logger import setup_logging
from exception.custom_exception import custom_exception
import pandas as pd 
import numpy as np 
from tensorflow.keras.models import load_model
import pickle
import logging
import sys

model=load_model('final_models/pred_model.h5')
with open('final_models/pred_enc.pkl','rb') as file:
    encoder=pickle.load(file)

def predict_drug(arr:np.ndarray)->list:
    try:
        setup_logging('giving input to model',logging.INFO)
        prediction=model.predict(arr)
        lst=prediction.tolist()[0]
        return lst
    except Exception as e : 
        raise custom_exception(e,sys)
    
def inverse_label(lst:list):
    try:
        f_pred=encoder.inverse_transform([int(np.expm1(int(i))) for i in lst])
        return f_pred
    except Exception as e : 
        raise custom_exception(e,sys)