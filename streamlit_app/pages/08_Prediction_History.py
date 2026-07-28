import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime
import plotly.express as px


st.set_page_config(
    page_title="Prediction History",
    page_icon="📜",
    layout="wide"
)


st.title("📜 Prediction History")


st.markdown(
    """
    View previous aircraft engine RUL predictions
    and maintenance status records.
    """
)


# Database path

DB_PATH = "prediction_history.db"


# -----------------------------
# Database Functions
# -----------------------------

def create_table():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS predictions
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            engine_id TEXT,
            rul REAL,
            status TEXT
        )
        """
    )

    conn.commit()

    conn.close()



def load_history():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql(
        "SELECT * FROM predictions ORDER BY id DESC",
        conn
    )

    conn.close()

    return df



def add_prediction(
        engine_id,
        rul,
        status
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO predictions
        (date, engine_id, rul, status)

        VALUES (?, ?, ?, ?)
        """,

        (
            datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            ),

            engine_id,

            rul,

            status
        )
    )


    conn.commit()

    conn.close()



create_table()



# -----------------------------
# Add Sample Prediction
# -----------------------------

st.subheader(
    "➕ Add Prediction Record"
)


col1, col2, col3 = st.columns(3)


engine_id = col1.text_input(
    "Engine ID",
    "Engine_001"
)


rul = col2.number_input(
    "Predicted RUL",
    min_value=0,
    value=150
)



if rul > 150:

    status = "Healthy"

elif rul > 50:

    status = "Warning"

else:

    status = "Critical"



col3.write(
    "Status"
)

col3.success(
    status
)



if st.button(
    "Save Prediction"
):

    add_prediction(
        engine_id,
        rul,
        status
    )


    st.success(
        "Prediction saved successfully!"
    )



st.divider()



# -----------------------------
# History Table
# -----------------------------


st.subheader(
    "📋 Previous Predictions"
)


history = load_history()



if len(history) > 0:


    st.dataframe(
        history,
        use_container_width=True
    )



    st.divider()



    # Filter

    st.subheader(
        "🔎 Filter History"
    )


    selected_status = st.selectbox(

        "Select Status",

        [
            "All",
            "Healthy",
            "Warning",
            "Critical"
        ]

    )



    filtered = history.copy()



    if selected_status != "All":

        filtered = filtered[
            filtered["status"] == selected_status
        ]



    st.dataframe(
        filtered,
        use_container_width=True
    )



    st.divider()



    # Chart


    st.subheader(
        "📈 RUL Trend"
    )



    fig = px.line(

        history,

        x="date",

        y="rul",

        color="engine_id",

        markers=True,

        title="Remaining Useful Life Trend"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )



else:

    st.info(
        "No prediction history available."
    )