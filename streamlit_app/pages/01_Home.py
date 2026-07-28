import streamlit as st
import plotly.express as px


st.set_page_config(
    page_title="Home Dashboard",
    page_icon="✈️",
    layout="wide"
)


st.title("✈️ Engine Fleet Dashboard")


# Metrics

col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Total Engines",
    "100"
)

col2.metric(
    "Healthy Engines",
    "82"
)

col3.metric(
    "Warning Engines",
    "13"
)

col4.metric(
    "Critical Engines",
    "5"
)



st.divider()


# Health Distribution

st.subheader("Engine Health Distribution")


health_data = {
    "Status": [
        "Healthy",
        "Warning",
        "Critical"
    ],
    "Count": [
        82,
        13,
        5
    ]
}


fig = px.pie(
    health_data,
    names="Status",
    values="Count",
    title="Fleet Health Status"
)


st.plotly_chart(
    fig,
    use_container_width=True
)



st.divider()


# Engine Table

st.subheader("Latest Engine Status")


data = {
    "Engine ID": [
        "Engine_001",
        "Engine_002",
        "Engine_003"
    ],
    "RUL (Cycles)": [
        250,
        80,
        20
    ],
    "Status": [
        "Healthy",
        "Warning",
        "Critical"
    ]
}


st.dataframe(
    data,
    use_container_width=True
)