import streamlit as st 
from utils.helper import load_output_data
from prediction_pipeline.similarity_prediction import give_drug_name
from logging_.logger import setup_logging
from utils.helper import load_model
from Data_validation.data_validation import recomendation_input


st.title("Drug Recommendation System")
st.write('Recommend similar drug by drug name')


df=load_output_data()
drug_input=st.selectbox('select the drug you want similar drug of',df['drug_name'].values)

dic={'drug_name':drug_input}
drug_in=recomendation_input(**dic)

recommendation=give_drug_name(drug_in)
button=st.button('Recommend')
if button:
    count=1
    for i in recommendation:
        st.write(f'{count}. {i}')
        j=df[df['drug_name']==i].index[0]
        st.write("for more information click :")
        st.markdown(df['drug_link'][j])
        count+=1

st.markdown("---")
st.info("This guide provides general classifications and definitions. Always consult healthcare professionals for individual drug risks.")