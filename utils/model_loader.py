import pickle
import streamlit as st


MODEL_PATH = "models/xgboost_model.pkl"



@st.cache_resource
def load_model():

    with open(
        MODEL_PATH,
        "rb"
    ) as file:

        model = pickle.load(file)


    return model