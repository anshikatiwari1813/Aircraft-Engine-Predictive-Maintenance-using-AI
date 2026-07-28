import streamlit as st
import pandas as pd
import pickle
import plotly.express as px


st.set_page_config(
    page_title="Batch Prediction",
    page_icon="📂",
    layout="wide"
)


st.title("📂 Batch Engine RUL Prediction")


st.markdown(
    """
    Upload multiple engine records and predict
    Remaining Useful Life (RUL) for the entire fleet.
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

    st.success(
        "XGBoost model loaded successfully!"
    )

except Exception as e:

    st.error(
        f"Model loading failed: {e}"
    )

    st.stop()



# -----------------------------
# Upload File
# -----------------------------

st.subheader(
    "📁 Upload Fleet Data"
)


uploaded_file = st.file_uploader(
    "Upload CSV file",
    type=["csv"]
)



if uploaded_file is not None:


    df = pd.read_csv(
        uploaded_file
    )


    st.success(
        "Dataset uploaded successfully!"
    )


    st.subheader(
        "Dataset Preview"
    )


    st.dataframe(
        df.head(),
        use_container_width=True
    )



    # Remove target column

    prediction_data = df.copy()


    if "RUL" in prediction_data.columns:

        prediction_data = prediction_data.drop(
            columns=["RUL"]
        )



    st.divider()



    if st.button(
        "🚀 Predict All Engines"
    ):


        try:


            predictions = model.predict(
                prediction_data
            )


            result = df.copy()


            result["Predicted_RUL"] = predictions



            # Status Classification

            def get_status(rul):

                if rul > 150:

                    return "🟢 Healthy"

                elif rul > 50:

                    return "🟡 Warning"

                else:

                    return "🔴 Critical"



            result["Status"] = (
                result["Predicted_RUL"]
                .apply(get_status)
            )



            st.subheader(
                "Prediction Results"
            )


            st.dataframe(
                result,
                use_container_width=True
            )



            st.divider()



            # Summary Cards

            st.subheader(
                "Fleet Health Summary"
            )


            healthy = len(
                result[
                    result["Status"]
                    ==
                    "🟢 Healthy"
                ]
            )


            warning = len(
                result[
                    result["Status"]
                    ==
                    "🟡 Warning"
                ]
            )


            critical = len(
                result[
                    result["Status"]
                    ==
                    "🔴 Critical"
                ]
            )


            col1, col2, col3 = st.columns(3)


            col1.metric(
                "Healthy Engines",
                healthy
            )


            col2.metric(
                "Warning Engines",
                warning
            )


            col3.metric(
                "Critical Engines",
                critical
            )



            st.divider()



            # Pie Chart


            status_count = result["Status"].value_counts()


            fig = px.pie(

                values=status_count.values,

                names=status_count.index,

                title="Fleet Condition Distribution"

            )


            st.plotly_chart(
                fig,
                use_container_width=True
            )



            st.divider()



            # Download Button


            csv = result.to_csv(
                index=False
            )


            st.download_button(

                label="⬇️ Download Prediction Report",

                data=csv,

                file_name=
                "engine_rul_predictions.csv",

                mime=
                "text/csv"

            )



        except Exception as e:


            st.error(
                f"Prediction error: {e}"
            )



else:

    st.info(
        "Upload fleet engine data to start batch prediction."
    )