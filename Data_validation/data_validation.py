from pydantic import BaseModel ,Field
from typing import Annotated

class recomendation_input(BaseModel):
    drug_name:Annotated[str,Field(max_length=83,title='name of drug that you want to similar to others',description='max number of character allowed is 83 because largest lenght drug is 83')]


class prediction_input(BaseModel):
    symptoms:Annotated[str,Field(max_length=500,title='Give all the symtoms',description='give all the symptoms you are facing in 500 characters')]
    