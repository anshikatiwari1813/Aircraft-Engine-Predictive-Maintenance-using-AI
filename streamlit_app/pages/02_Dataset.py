import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Dataset Analysis",
    page_icon="📂",
    layout="wide"
)


st.title("📂 Aircraft Engine Dataset")


st.markdown(
    """
    Explore the engine sensor dataset used for
    Remaining Useful Life (RUL) prediction.
    """
)


# Upload Dataset

st.subheader("Upload Dataset")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)


if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)


    st.success("Dataset loaded successfully!")


    # Dataset Information

    st.subheader("📊 Dataset Overview")


    col1, col2, col3 = st.columns(3)


    col1.metric(
        "Total Rows",
        df.shape[0]
    )

    col2.metric(
        "Total Columns",
        df.shape[1]
    )

    col3.metric(
        "Missing Values",
        df.isnull().sum().sum()
    )


    st.divider()


    # Dataset Preview

    st.subheader("👀 Dataset Preview")


    st.dataframe(
        df.head(20),
        use_container_width=True
    )


    st.divider()


    # Columns

    st.subheader("📌 Feature Information")


    feature_data = pd.DataFrame(
        {
            "Feature Name": df.columns,
            "Data Type": df.dtypes.astype(str)
        }
    )


    st.dataframe(
        feature_data,
        use_container_width=True
    )


    st.divider()


    # Statistics

    st.subheader("📈 Statistical Summary")


    st.dataframe(
        df.describe(),
        use_container_width=True
    )


    st.divider()


    # Missing Values

    st.subheader("🔍 Missing Value Analysis")


    missing = pd.DataFrame(
        {
            "Column": df.columns,
            "Missing Values": df.isnull().sum()
        }
    )


    st.dataframe(
        missing,
        use_container_width=True
    )


else:

    st.info(
        "Please upload an engine dataset CSV file."
    )