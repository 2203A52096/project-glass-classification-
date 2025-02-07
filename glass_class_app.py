# -*- coding: utf-8 -*-
"""glass_class_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bwKJ_hGt3CpbtwqjaeDmPMcZudA5YmmX
"""

import pickle
import streamlit as st
import joblib
from PIL import Image

# loading the saved models

model = joblib.load('glass_classification.joblib')
image = Image.open('glass.jpg')
st.title("Glass Type Prediction")
st.image(image,use_container_width=True)

# Create input fields for the features
col1, col2 ,col3,col4,col5 = st.columns(5)

with col1:
    feature_1 = st.number_input("RI", min_value=0, value=1)
    feature_2 = st.number_input("Na", min_value=0, value=1)

with col2:
    feature_3 = st.number_input("Mg", min_value=0, value=1)
    feature_4 = st.number_input("Al", min_value=0, value=1)
with col3:
    feature_5 = st.number_input("Si", min_value=0, value=1)
    feature_6 = st.number_input("K", min_value=0, value=1)

with col4:
    feature_7 = st.number_input("Ca", min_value=0, value=1)
    feature_8 = st.number_input("Ba", min_value=0, value=1)
with col5:
    feature_9 = st.number_input("Fe", min_value=0, value=1)

features = [[feature_1,feature_2,feature_3,feature_4,feature_5,feature_6,feature_7,feature_8,feature_9]]

# Predict the glass type when the button is clicked
if st.sidebar.button('Predict Glass Type'):
    # Make prediction
    prediction = model.predict(features)

    # Display the prediction result
    glass_types = {
        1: 'Building Windows Float Glass',
        2: 'Building Windows Non-Float Glass',
        3: 'Vehicle Windows Float Glass',
        4: 'Vehicle Windows Non-Float Glass',
        5: 'Containers',
        6: 'Tableware',
        7: 'Headlamps'
    }

    # Display the result in the app
    st.write(f"Predicted Glass Type: {glass_types.get(prediction[0], 'Unknown')}")
