import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Get the directory where app.py is located
current_dir = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(current_dir, 'model.pkl')
data_path = os.path.join(current_dir, 'sonar data.csv')

# Load model and dataset using absolute relative paths
@st.cache_resource
def load_data_and_model():
    model = joblib.load(model_path)
    sonar_data = pd.read_csv(data_path, header=None)
    return model, sonar_data

model, sonar_data = load_data_and_model()

st.title("Sonar Navigation: Rock vs. Mine Dashboard")
st.write("An interactive web application built with Streamlit to analyze sonar return frequencies and evaluate machine learning predictions.")

# Sidebar navigation
page = st.sidebar.selectbox("Choose a View", ["Dataset Overview", "Make a Prediction"])

if page == "Dataset Overview":
    st.subheader("Dataset Summary")
    st.write(f"Total Rows (Samples): {sonar_data.shape[0]}")
    st.write(f"Total Columns (Sonar Frequencies + Label): {sonar_data.shape[1]}")
    
    st.markdown("### Class Distribution")
    class_counts = sonar_data[60].value_counts().reindex(['M', 'R'])
    st.bar_chart(class_counts)

elif page == "Make a Prediction":
    st.subheader("Test Sonar Instance Prediction")
    st.write("Click the button below to test a sample instance from the dataset through your Logistic Regression model.")
    
    if st.button("Run Prediction on Sample", type="primary"):
        # Grab a sample row from dataset features (Row 0)
        sample_input = sonar_data.drop(columns=60).iloc[0].values.reshape(1, -1)
        pred = model.predict(sample_input)[0]
        
        if pred == 'M':
            st.error("Prediction Result: Mine (M)")
        else:
            st.success("Prediction Result: Rock (R)")
