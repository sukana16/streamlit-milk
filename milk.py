import pickle 
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('milk.sav', 'rb'))

# judul web
st.title('Grade MILK')

ph = st.number_input('pH')

temperature = st.number_input('Temperature')

taste = st.number_input('Taste')

odor = st.number_input('Odor')

fat = st.number_input('Fat')

turbidity= st.number_input('Turbidity')

colour = st.number_input('Colour')



# code for prediction
Grade_Milk= ''

if st.button ('Grade Milk') :
    Grade_Milk = model.predict([[ph,temperature,taste,odor,fat ,turbidity,colour]])
    
    if ([0]==1):
        Grade_Milk = 'Grade Milk High'
    else:
        Grade_Milk = 'Grade Milk Low'
st.success(Grade_Milk)
