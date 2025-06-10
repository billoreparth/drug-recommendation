import streamlit as st 
import pandas as pd 
import numpy as np
from utils.helper import load_output_data
from Data_validation.data_validation import prediction_input
from Data_transformation.data_transformation import input_cleaning,data_transform,convert_into_numberic
from prediction_pipeline.pred_pipline import predict_drug,inverse_label
import sys
from exception.custom_exception import custom_exception

Providing_Data = st.Page("src/Resources/Help_Data.py", title="Help", icon="🎉")
st.title('Drug Recommendation System')
st.write('Predicts medical conditions and recommend drug accordingly')
st.write('Give all the symptoms you are feeling: like the example in the box')
input_text=st.text_area(label="Please Don't Use the phrase like disease , in the {body part} , for your , symptoms , likely , may , severe , easy , critical , etc ",value='difficult breathing swelling face throat severe skin reaction fever sore throat burning eyes skin pain red purple skin rash spreads causes blistering peeling',max_chars=500)

df=load_output_data()
if st.button('Predict'):

    in_dict={'symptoms':input_text}
    in_val=prediction_input(**in_dict)

    # transforming the data
    clean_in=input_cleaning(in_val)
    transform_in=data_transform(clean_in)
    numeric_in=convert_into_numberic(transform_in)

    # predicting drug
    num_pred=predict_drug(numeric_in)
    

    try:
        final_pred=inverse_label(num_pred)
        st.write(final_pred[0])
       
        drug_info = {
            "Possible Medical Condition":df[df['drug_name']==final_pred[0]]['medical_condition'].values[0],
            "Generic Name": df[df['drug_name']==final_pred[0]]['generic_name'].values[0],
            "Medical Companies": df[df['drug_name']==final_pred[0]]['brand_names'].values[0],
            "Alcohol Interaction": df[df['drug_name']==final_pred[0]]['alcohol'].values[0],
            "CSA Schedule": df[df['drug_name']==final_pred[0]]['csa'].values[0],
            "Pregnancy Category": df[df['drug_name']==final_pred[0]]['pregnancy_category'].values[0],
            "Rx/OTC": df[df['drug_name']==final_pred[0]]['rx_otc'].values[0],
            "More Info": df[df['drug_name']==final_pred[0]]['drug_link'].values[0]
        }

    
        with st.expander(f"Drug Information: {final_pred[0]} ", expanded=True):
            st.markdown(f"""
            **Generic Name**: {drug_info['Generic Name']}    
            **Medical Companies**: {drug_info['Medical Companies']}  
            **Alcohol Interaction**: {drug_info['Alcohol Interaction']}  
            **CSA Schedule**: {drug_info['CSA Schedule']}  
            **Pregnancy Category**: {drug_info['Pregnancy Category']}  
            **Rx / OTC**: {drug_info['Rx/OTC']}  
            🔗 [More Information]({drug_info['More Info']})
            """)


    except: 
        
        st.write('model failed to recognized the drug')

st.write('Need Help in Writing symptoms click')
if st.button('Help'):
    pg=st.navigation([Providing_Data])
    pg.run()

st.markdown("---")
st.info("This guide provides general classifications and definitions. Always consult healthcare professionals for individual drug risks.")