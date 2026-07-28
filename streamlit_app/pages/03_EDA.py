import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
    page_title="Exploratory Data Analysis",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Exploratory Data Analysis (EDA)")


st.markdown(
    """
    Analyze aircraft engine sensor behavior,
    identify patterns, and understand feature relationships.
    """
)


# Upload Dataset

uploaded_file = st.file_uploader(
    "Upload Engine Dataset CSV",
    type=["csv"]
)


if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)


    st.success("Dataset loaded successfully!")


    # Dataset Summary

    st.subheader("Dataset Summary")


    col1, col2, col3 = st.columns(3)


    col1.metric(
        "Rows",
        df.shape[0]
    )

    col2.metric(
        "Columns",
        df.shape[1]
    )

    col3.metric(
        "Sensors",
        len(
            [c for c in df.columns if "sensor" in c.lower()]
        )
    )


    st.divider()


    # Detect Sensors

    sensor_columns = [
        col for col in df.columns
        if "sensor" in col.lower()
    ]


    if len(sensor_columns) == 0:

        st.warning(
            "No sensor columns found in dataset."
        )

        st.stop()



    # Sensor Selection

    st.subheader("🔎 Sensor Analysis")


    selected_sensor = st.selectbox(
        "Select Sensor",
        sensor_columns
    )


    # Histogram

    st.write(
        f"### Distribution of {selected_sensor}"
    )


    fig_hist = px.histogram(
        df,
        x=selected_sensor,
        nbins=50,
        title=f"{selected_sensor} Distribution"
    )


    st.plotly_chart(
        fig_hist,
        use_container_width=True
    )


    st.divider()



    # Sensor Trend

    st.subheader(
        "📈 Sensor Trend Over Engine Cycles"
    )


    if "cycle" in df.columns:

        fig_line = px.line(
            df,
            x="cycle",
            y=selected_sensor,
            title=f"{selected_sensor} vs Cycle"
        )


        st.plotly_chart(
            fig_line,
            use_container_width=True
        )

    else:

        st.warning(
            "Cycle column not available."
        )


    st.divider()



    # Correlation Heatmap

    st.subheader(
        "🔥 Feature Correlation Heatmap"
    )


    numeric_df = df.select_dtypes(
        include="number"
    )


    correlation = numeric_df.corr()


    fig, ax = plt.subplots(
        figsize=(12,8)
    )


    sns.heatmap(
        correlation,
        cmap="coolwarm",
        ax=ax
    )


    st.pyplot(fig)



    st.divider()



    # Sensor Statistics

    st.subheader(
        "📋 Sensor Statistics"
    )


    stats = df[sensor_columns].describe().T


    st.dataframe(
        stats,
        use_container_width=True
    )


else:

    st.info(
        "Upload your aircraft engine dataset to start EDA."
    )