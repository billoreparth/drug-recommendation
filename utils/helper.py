import pickle
import pandas as pd
import numpy as np 

def load_model(path:str):
    with open(path,'rb') as file: 
        return pickle.load(file)
    
def load_training_data():
    return pd.read_csv("src\Data\cleaned_training_data.csv")

def load_output_data():
    return pd.read_csv("src\Data\data.csv")

def save_model(name:str,content):
    '''
    content: any object type like encoder , model file , etc.
    location: current directory
    '''
    with open(name,'wb') as file: 
        pickle.dump(content,file)

def load_model_data():
    return pd.read_csv('src\Data\model_data.csv')

def words_to_vectors(text:str,model:any):
    '''

    text: str: sentence or words \n
    model: any:any word2vec , tf-idf model \n
    retruns a vector for each sentence or word \n
    use it while making a list of vecors \n
    '''

    for i in text:
        words=i.lower().split()
        vectors = [model[word] for word in words if word in model]
        if vectors : 
            return np.mean(vectors,axis=0)
        else : 
            return np.zeros(model.vector_size)

def recommend_drug(drug:str,sim_model:any):
    df=load_training_data()
    index=df[df['drug_name']==drug].index[0]
    model=sim_model
    distances=model[index]
    drug_list=sorted(list(enumerate(distances)),reverse=True,key=lambda c:c[1])[1:6]
    return drug_list

def load_final_data():
    return pd.read_csv('src/Data/final_set.csv')

def split_symptoms(text, chunk_size=2, max_chunks=15):
    words = text.split()
    chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    # Pad with empty strings if fewer than max_chunks
    chunks = chunks[:max_chunks] + [''] * (max_chunks - len(chunks))
    return pd.Series(chunks, index=[f"symptom{i+1}" for i in range(max_chunks)])
