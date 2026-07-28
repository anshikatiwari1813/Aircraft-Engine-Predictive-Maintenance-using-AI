import streamlit as st
import plotly.express as px


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Aircraft Engine Predictive Maintenance",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# Custom CSS
# ==========================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
    }


    .subtitle {
        font-size: 20px;
        text-align: center;
        color: gray;
    }


    .card {
        padding: 20px;
        border-radius: 10px;
        background-color: #f5f7fa;
        text-align: center;
    }


    </style>

    """,
    unsafe_allow_html=True
)



# ==========================================
# Sidebar
# ==========================================


st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3064/3064197.png",
    width=80
)


st.sidebar.title(
    "✈️ Engine AI"
)


st.sidebar.markdown(
    """
    ---
    
    **Aircraft Engine Predictive Maintenance**

    AI-based system for:

    - RUL Prediction
    - Engine Health Monitoring
    - Failure Risk Detection
    - Explainable AI

    ---
    """
)



st.sidebar.info(
    """
    Navigation:

    Use the pages from the sidebar
    to explore the complete system.
    """
)



# ==========================================
# Home Dashboard
# ==========================================


st.markdown(
    """
    <div class="main-title">
    ✈️ Aircraft Engine Predictive Maintenance System
    </div>

    <div class="subtitle">
    AI-powered Remaining Useful Life (RUL) Prediction Platform
    </div>

    """,

    unsafe_allow_html=True
)



st.write("")



# ==========================================
# Introduction
# ==========================================


st.markdown(
    """
    ## 🚀 Welcome

    This platform uses Machine Learning and Deep Learning
    techniques to monitor aircraft engine health and predict
    remaining useful life before failure occurs.

    The system helps maintenance teams:

    - Predict engine degradation
    - Identify risky engines
    - Analyze sensor behaviour
    - Understand AI decisions
    - Generate maintenance reports

    """
)



st.divider()



# ==========================================
# Project Statistics
# ==========================================


st.subheader(
    "📊 System Overview"
)


col1, col2, col3, col4 = st.columns(4)



col1.metric(
    "AI Models",
    "2"
)


col2.metric(
    "Prediction Target",
    "RUL"
)


col3.metric(
    "ML Algorithm",
    "XGBoost"
)


col4.metric(
    "Explainability",
    "SHAP"
)



st.divider()



# ==========================================
# Sample Fleet Dashboard
# ==========================================


st.subheader(
    "✈️ Fleet Health Overview"
)



fleet_data = {

    "Status": [

        "Healthy",
        "Warning",
        "Critical"

    ],

    "Engines": [

        82,
        13,
        5

    ]

}



fig = px.pie(

    fleet_data,

    names="Status",

    values="Engines",

    title="Engine Condition Distribution"

)



st.plotly_chart(

    fig,

    use_container_width=True

)



st.divider()



# ==========================================
# Technology Stack
# ==========================================


st.subheader(
    "🛠 Technology Stack"
)


col1, col2, col3 = st.columns(3)



with col1:

    st.success(
        """
        ### Machine Learning

        ✓ XGBoost

        ✓ Scikit-learn

        ✓ Feature Engineering

        """
    )


with col2:

    st.info(
        """
        ### Deep Learning

        ✓ LSTM

        ✓ TensorFlow/Keras

        ✓ Time Series Analysis

        """
    )


with col3:

    st.warning(
        """
        ### Deployment

        ✓ Streamlit

        ✓ Plotly

        ✓ SHAP

        """
    )



st.divider()



# ==========================================
# Workflow
# ==========================================


st.subheader(
    "⚙️ System Workflow"
)


workflow = [

    "📂 Dataset Collection",

    "🔧 Data Preprocessing",

    "📊 Exploratory Analysis",

    "🤖 Model Prediction",

    "🧠 Explainable AI",

    "🛠 Maintenance Recommendation",

    "📄 Report Generation"

]


for step in workflow:

    st.write(step)



st.divider()



# ==========================================
# Footer
# ==========================================


st.markdown(
    """
    <center>

    Developed for AI-based Aircraft Engine
    Predictive Maintenance

    <br>

    🚀 Machine Learning | Deep Learning | Explainable AI

    </center>
    """,

    unsafe_allow_html=True
)