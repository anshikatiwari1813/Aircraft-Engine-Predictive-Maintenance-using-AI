import streamlit as st


st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)


st.title("ℹ️ About Aircraft Engine Predictive Maintenance")


st.markdown(
    """
    ## ✈️ Project Overview

    Aircraft Engine Predictive Maintenance is an
    AI-based system designed to predict engine
    degradation and estimate Remaining Useful Life (RUL)
    using machine learning.

    The system helps maintenance teams perform
    preventive maintenance before unexpected failures.
    """
)


st.divider()


# Problem Statement

st.subheader("🎯 Problem Statement")


st.write(
    """
    Traditional aircraft maintenance follows fixed schedules,
    which may lead to unnecessary maintenance or unexpected
    failures.

    This project uses sensor data and machine learning models
    to predict engine health and remaining operational cycles.
    """
)



st.divider()



# Workflow

st.subheader("⚙️ System Workflow")


workflow = [

    "1. Collect aircraft engine sensor data",

    "2. Perform data preprocessing and feature engineering",

    "3. Train machine learning models",

    "4. Predict Remaining Useful Life (RUL)",

    "5. Explain predictions using SHAP",

    "6. Generate maintenance recommendations"

]


for item in workflow:

    st.write(
        item
    )



st.divider()



# ML Models

st.subheader("🤖 Machine Learning Approach")


col1, col2 = st.columns(2)


with col1:

    st.info(
        """
        ### XGBoost Regressor

        Used for:

        ✓ RUL Prediction

        ✓ Feature importance analysis

        ✓ High accuracy regression
        """
    )


with col2:

    st.info(
        """
        ### LSTM Deep Learning

        Used for:

        ✓ Time-series sensor analysis

        ✓ Sequential degradation patterns

        ✓ Future health forecasting
        """
    )



st.divider()



# Dataset

st.subheader("📊 Dataset Information")


st.write(
    """
    Dataset:

    NASA C-MAPSS Aircraft Engine Dataset


    Data Contains:

    - Engine ID
    - Operating cycles
    - Sensor measurements
    - Engine operating conditions
    - Remaining Useful Life (RUL)
    """
)



st.divider()



# Technology Stack

st.subheader("🛠 Technology Stack")


tech = {

    "Programming": "Python",

    "Machine Learning": "XGBoost, Scikit-learn",

    "Deep Learning": "TensorFlow / Keras",

    "Visualization": "Streamlit, Plotly",

    "Explainable AI": "SHAP",

    "Database": "SQLite"

}



st.table(
    tech
)



st.divider()



# Features

st.subheader("🚀 Dashboard Features")


features = [

    "📊 Interactive Data Exploration",

    "🔮 RUL Prediction",

    "❤️ Engine Health Monitoring",

    "🧠 SHAP Explainability",

    "📂 Batch Fleet Prediction",

    "📜 Prediction History",

    "📄 Automated Maintenance Reports"

]


for feature in features:

    st.write(
        feature
    )



st.divider()



st.success(
    """
    Developed as an AI/ML based predictive maintenance
    solution for aircraft engine health monitoring.
    """
)