import numpy as np
import pickle
import streamlit as st
import pandas as pd

pickle_in = open("specs_prediction.pkl","rb")
model=pickle.load(pickle_in)


st.title('Specs Prediction')

list_of_columns=['phone', 'Laptop', 'TV', 'Headaches', 'Blurry vision', 'Specs']

input_data=pd.DataFrame(columns=list_of_columns)
input_data.drop(['Specs'], axis='columns',inplace=True)


input_data.at[0, 'phone'] = st.slider('phone:',
                            min_value = 0,
                            max_value = 24,
                            )
input_data.at[0, 'Laptop'] = st.slider('Laptop:',
                            min_value = 0,
                            max_value = 24,
                            )
input_data.at[0, 'TV'] = st.slider('TV:',
                            min_value = 0,
                            max_value = 24,
                            )

input_data.at[0, 'Headaches'] = st.radio("Do you have headaches",
                                ('yes', 'no'))

input_data.at[0, 'Blurry vision'] = st.radio("Do you have blurry vision",
                                    ('yes', 'no'))

varlist =  ['Headaches', 'Blurry vision']

def binary_map(x):
    return x.map({'yes': 1, "no": 0})

input_data[varlist] = input_data[varlist].apply(binary_map)


if st.button("Predict"):

    y_pred =  model.predict(input_data)

    if(y_pred[0]==1):
        st.text('You need specs')
    if(y_pred[0]==0):
        st.text('You do not need specs')