import streamlit as st
import pandas as pd
import pickle
import shap
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="AI Explainability",
    page_icon="🧠",
    layout="wide"
)


st.title("🧠 AI Explainability (SHAP Analysis)")


st.markdown(
    """
    Understand why the AI model predicted a specific
    Remaining Useful Life (RUL) value.
    
    SHAP explains the contribution of each sensor feature
    in the model decision.
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
# Upload Data
# -----------------------------

st.subheader(
    "📂 Upload Engine Data"
)


uploaded_file = st.file_uploader(
    "Upload CSV",
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


    # Remove target column

    if "RUL" in df.columns:

        df = df.drop(
            columns=["RUL"]
        )



    st.divider()



    # Prediction

    prediction = model.predict(df)


    rul = round(
        prediction.mean(),
        2
    )


    st.subheader(
        "Prediction Result"
    )


    st.metric(
        "Predicted RUL",
        f"{rul} cycles"
    )



    st.divider()



    # -----------------------------
    # SHAP Explanation
    # -----------------------------


    st.subheader(
        "🔍 Feature Contribution Analysis"
    )


    try:


        explainer = shap.TreeExplainer(
            model
        )


        shap_values = explainer.shap_values(
            df
        )


        st.write(
            "Features influencing prediction:"
        )


        fig, ax = plt.subplots(
            figsize=(10,6)
        )


        shap.summary_plot(

            shap_values,

            df,

            plot_type="bar",

            show=False

        )


        st.pyplot(
            fig
        )



        st.divider()



        st.subheader(
            "📌 Detailed Feature Impact"
        )


        shap_df = pd.DataFrame(

            {

                "Feature": df.columns,

                "Impact": abs(
                    shap_values.mean(axis=0)
                )

            }

        )


        shap_df = shap_df.sort_values(
            by="Impact",
            ascending=False
        )


        st.dataframe(
            shap_df,
            use_container_width=True
        )


    except Exception as e:


        st.warning(
            f"SHAP analysis error: {e}"
        )



else:

    st.info(
        "Upload engine sensor data to view AI explanation."
    )