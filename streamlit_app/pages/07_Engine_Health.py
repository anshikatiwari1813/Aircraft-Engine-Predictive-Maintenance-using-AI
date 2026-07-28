import streamlit as st
import pandas as pd
import pickle
import plotly.express as px


st.set_page_config(
    page_title="Engine Health Monitoring",
    page_icon="❤️",
    layout="wide"
)


st.title("❤️ Engine Health Monitoring Dashboard")


st.markdown(
    """
    Monitor individual aircraft engine health,
    remaining useful life, and sensor behaviour.
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

except Exception as e:

    st.error(
        f"Model loading error: {e}"
    )

    st.stop()



# -----------------------------
# Upload Dataset
# -----------------------------

st.subheader("📂 Upload Engine Dataset")


uploaded_file = st.file_uploader(
    "Upload CSV file",
    type=["csv"]
)



if uploaded_file is not None:


    df = pd.read_csv(
        uploaded_file
    )


    st.success(
        "Dataset loaded successfully"
    )



    # Engine Selection

    if "engine_id" in df.columns:


        engine_list = sorted(
            df["engine_id"].unique()
        )


        selected_engine = st.selectbox(
            "Select Engine ID",
            engine_list
        )


        engine_data = df[
            df["engine_id"] == selected_engine
        ].copy()



    else:

        st.warning(
            "engine_id column not found"
        )

        engine_data = df.copy()



    # Remove target column

    if "RUL" in engine_data.columns:

        engine_data = engine_data.drop(
            columns=["RUL"]
        )



    st.divider()



    # -----------------------------
    # Prediction
    # -----------------------------


    prediction = model.predict(
        engine_data
    )


    rul = round(
        prediction[-1],
        2
    )



    # Health score

    health_score = min(
        max(
            (rul / 300) * 100,
            0
        ),
        100
    )


    # Status

    if rul > 150:

        status = "🟢 Healthy"

    elif rul > 50:

        status = "🟡 Warning"

    else:

        status = "🔴 Critical"



    # -----------------------------
    # Metrics
    # -----------------------------


    st.subheader(
        "Engine Condition"
    )


    col1, col2, col3 = st.columns(3)


    col1.metric(
        "Engine ID",
        selected_engine
    )


    col2.metric(
        "Remaining Useful Life",
        f"{rul} cycles"
    )


    col3.metric(
        "Condition",
        status
    )



    st.divider()



    # Health Gauge


    st.subheader(
        "Engine Health Score"
    )


    st.progress(
        int(health_score)
    )


    st.metric(
        "Health Score",
        f"{round(health_score,2)}%"
    )



    st.divider()



    # -----------------------------
    # Sensor Analysis
    # -----------------------------


    st.subheader(
        "📈 Sensor Behaviour"
    )


    sensors = [

        col for col in engine_data.columns

        if "sensor" in col.lower()

    ]


    if len(sensors) > 0:


        selected_sensor = st.selectbox(

            "Select Sensor",

            sensors

        )


        if "cycle" in engine_data.columns:


            fig = px.line(

                engine_data,

                x="cycle",

                y=selected_sensor,

                title=f"{selected_sensor} Trend"

            )


            st.plotly_chart(

                fig,

                use_container_width=True

            )


        else:


            st.warning(
                "Cycle column not available"
            )



    st.divider()



    # Maintenance Recommendation


    st.subheader(
        "🛠 Maintenance Recommendation"
    )


    if rul > 150:

        st.success(
            "Engine is operating normally. Continue monitoring."
        )


    elif rul > 50:

        st.warning(
            "Schedule preventive inspection soon."
        )


    else:

        st.error(
            "Immediate maintenance required."
        )



else:

    st.info(
        "Upload engine data to monitor health."
    )