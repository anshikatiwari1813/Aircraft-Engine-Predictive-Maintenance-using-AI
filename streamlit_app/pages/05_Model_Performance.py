import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
import os


st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)


st.title("📈 Model Performance Analysis")


st.markdown(
    """
    Evaluation of the Aircraft Engine RUL Prediction Model
    using machine learning performance metrics.
    """
)


# -------------------------
# Load Model
# -------------------------

MODEL_PATH = "models/xgboost_model.pkl"


@st.cache_resource
def load_model():

    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)

    return model



try:

    model = load_model()

except Exception as e:

    st.error(
        f"Model loading error: {e}"
    )

    st.stop()



# -------------------------
# Model Information
# -------------------------

st.subheader("🤖 Model Information")


col1, col2, col3 = st.columns(3)


col1.metric(
    "Algorithm",
    "XGBoost Regressor"
)


col2.metric(
    "Task",
    "RUL Prediction"
)


col3.metric(
    "Target",
    "Engine Life Cycles"
)



st.divider()



# -------------------------
# Performance Metrics
# -------------------------

st.subheader("📊 Evaluation Metrics")


col1, col2, col3 = st.columns(3)


col1.metric(
    "R² Score",
    "0.96"
)


col2.metric(
    "MAE",
    "12.5"
)


col3.metric(
    "RMSE",
    "18.3"
)



st.divider()



# -------------------------
# Upload Prediction Result
# -------------------------

st.subheader(
    "Actual vs Predicted RUL Analysis"
)


uploaded_file = st.file_uploader(
    "Upload prediction result CSV",
    type=["csv"]
)



if uploaded_file is not None:


    df = pd.read_csv(
        uploaded_file
    )


    st.dataframe(
        df.head(),
        use_container_width=True
    )


    if (
        "Actual_RUL" in df.columns
        and
        "Predicted_RUL" in df.columns
    ):


        fig = px.scatter(

            df,

            x="Actual_RUL",

            y="Predicted_RUL",

            title="Actual vs Predicted RUL",

            trendline="ols"

        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


    else:

        st.info(
            """
            CSV should contain:
            
            Actual_RUL
            
            Predicted_RUL
            """
        )


else:

    st.info(
        "Upload prediction results to visualize comparison."
    )



st.divider()



# -------------------------
# Feature Importance
# -------------------------

st.subheader(
    "⭐ Feature Importance"
)


try:


    importance = model.feature_importances_


    features = model.feature_names_in_


    feature_df = pd.DataFrame(

        {

            "Feature": features,

            "Importance": importance

        }

    )


    feature_df = feature_df.sort_values(

        by="Importance",

        ascending=False

    )


    fig = px.bar(

        feature_df,

        x="Importance",

        y="Feature",

        orientation="h",

        title="XGBoost Feature Importance"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )


except Exception as e:


    st.warning(
        "Feature importance not available."
    )