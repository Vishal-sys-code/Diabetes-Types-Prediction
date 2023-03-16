import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the diabetes dataset
df = pd.read_csv('NCSU_Dataset.csv')

# Select the features for clustering
X = df[['Age', 'Pregnancies', 'Glucose']].values

# Load the KMeans model from a pickle file
with open('kmeans_model.pkl', 'rb') as f:
    kmeans = pickle.load(f)

# Define a function to predict cluster membership for new data
def predict_cluster(age, pregnancies, glucose):
    return kmeans.predict([[age, pregnancies, glucose]])[0]

# Create the Streamlit web app
st.title('Diabetes Cluster Prediction')

# Add user input fields for age, pregnancies, and glucose
age = st.slider('Age', min_value=0, max_value=100, step=1)
pregnancies = st.slider('Number of Pregnancies', min_value=0, max_value=20, step=1)
glucose = st.slider('Glucose Level', min_value=0, max_value=200, step=1)

# Make a prediction and display the predicted cluster number
cluster_number = predict_cluster(age, pregnancies, glucose)
st.write('The predicted cluster number is', cluster_number)
