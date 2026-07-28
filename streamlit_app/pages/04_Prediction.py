import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go
import os


st.set_page_config(
    page_title="RUL Prediction",
    page_icon="🔮",
    layout="wide"
)


st.title("🔮 Remaining Useful Life (RUL) Prediction")


st.markdown(
    """
    Upload engine sensor data and the AI model will
    estimate the remaining useful life of the engine.
    """
)


# -----------------------------
# Load Model
# -----------------------------

MODEL_PATH = "models/xgboost_model.pkl"


@st.cache_resource
def load_model():

    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)

    return model



try:

    model = load_model()

    st.success("Model loaded successfully!")

except Exception as e:

    st.error(
        f"Model loading failed: {e}"
    )

    st.stop()



# -----------------------------
# Upload Dataset
# -----------------------------

st.subheader("📂 Upload Engine Data")


uploaded_file = st.file_uploader(
    "Upload CSV file",
    type=["csv"]
)



if uploaded_file is not None:


    df = pd.read_csv(uploaded_file)


    st.success(
        "Dataset uploaded successfully!"
    )


    st.subheader("Dataset Preview")


    st.dataframe(
        df.head(),
        use_container_width=True
    )


    # Remove target column

    if "RUL" in df.columns:

        df = df.drop(
            columns=["RUL"]
        )



    st.divider()



    # -----------------------------
    # Prediction
    # -----------------------------


    if st.button(
        "🚀 Predict RUL"
    ):


        try:

            prediction = model.predict(df)


            rul = round(
                prediction.mean(),
                2
            )


            st.subheader(
                "Prediction Result"
            )


            col1, col2, col3 = st.columns(3)


            col1.metric(
                "Predicted RUL",
                f"{rul} cycles"
            )



            # Risk calculation

            if rul > 150:

                status = "🟢 Healthy"
                risk = "Low Risk"


            elif rul > 50:

                status = "🟡 Warning"
                risk = "Medium Risk"


            else:

                status = "🔴 Critical"
                risk = "High Risk"



            col2.metric(
                "Engine Status",
                status
            )


            col3.metric(
                "Failure Risk",
                risk
            )


            st.divider()



            # Gauge Chart


            st.subheader(
                "Engine Life Indicator"
            )


            fig = go.Figure(
                go.Indicator(

                    mode="gauge+number",

                    value=rul,

                    title={
                        "text":
                        "Remaining Useful Life"
                    },

                    gauge={

                        "axis":{
                            "range":[0,300]
                        }

                    }

                )
            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



        except Exception as e:


            st.error(
                f"Prediction error: {e}"
            )


else:

    st.info(
        "Please upload engine sensor data."
    )