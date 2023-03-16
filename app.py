import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the KMeans model from file
with open('kmeans_model.pkl', 'r+b') as f:
    kmeans = pickle.load(f)

# Define a function to predict cluster membership for new data
def predict_cluster(age, pregnancies, glucose):
    return kmeans.predict([[age, pregnancies, glucose]])[0]

# Define a function to assign cluster conditions
def get_cluster_conditions(cluster_num, age, pregnancies, glucose):
    if cluster_num == 0:
        if age >= 13 and age <= 18 and (glucose <= 120 or glucose >= 170):
            return "Type 1 Diabetes"
        else:
            return "Type 1 Diabetes"
    elif cluster_num == 1:
        if age >= 18 and age <= 30 and (glucose <= 90 or glucose >= 130):
            return "Type 2 Diabetes"
        elif age >= 30 and (glucose <= 90 or glucose >= 130):
            return "Type 2 Diabetes"
        else:
            return "Type 1 Diabetes"
    else:
        if age >= 18 and age <= 30 and pregnancies == 1 and (glucose <= 90 or glucose >= 130):
            return "Type 3 Diabetes"
        elif age >= 30 and pregnancies == 1 and (glucose <= 90 or glucose >= 130):
            return "Type 3 Diabetes"
        else:
            return "Type 2 Diabetes"

# Create the Streamlit web app
st.title('Diabetes Cluster Prediction')

# Add user input fields for age, pregnancies, and glucose
age = st.slider('Age', min_value=0, max_value=100, step=1)
pregnancies = st.slider('Number of Pregnancies', min_value=0, max_value=20, step=1)
glucose = st.slider('Glucose Level', min_value=0, max_value=200, step=1)

# Make a prediction and display the predicted cluster condition
cluster_number = predict_cluster(age, pregnancies, glucose)
cluster_condition = get_cluster_conditions(cluster_number, age, pregnancies, glucose)
st.write('The predicted cluster condition is:', cluster_condition)
