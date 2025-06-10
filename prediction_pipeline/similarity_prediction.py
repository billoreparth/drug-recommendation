from utils.helper import recommend_drug
from utils.helper import load_training_data
from utils.helper import load_model
from Data_validation.data_validation import recomendation_input
import logging
from logging_.logger import setup_logging
from exception.custom_exception import custom_exception
import sys

def give_drug_name(drug_name:recomendation_input):
    try:
        lst=[]
        df=load_training_data()

        sim_model=load_model('final_models/similarity.pkl')
        setup_logging('similarity model has been setup',logging.INFO)

        recommendation_list=recommend_drug(drug_name.drug_name,sim_model=sim_model)
        setup_logging('list of indexes is ready converting it into name ...',logging.INFO)
        for i in recommendation_list: 
            lst.append(df.iloc[i[0]].drug_name)

        return lst
    except Exception as e : 
        raise custom_exception(e,sys)

