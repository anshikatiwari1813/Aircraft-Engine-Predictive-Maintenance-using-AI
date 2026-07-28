import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os


st.set_page_config(
    page_title="Download Report",
    page_icon="📄",
    layout="wide"
)


st.title("📄 Aircraft Engine Maintenance Report")


st.markdown(
    """
    Generate a downloadable PDF report
    containing engine health prediction details.
    """
)



# -----------------------------
# User Input
# -----------------------------

st.subheader("Enter Engine Details")


engine_id = st.text_input(
    "Engine ID",
    "Engine_001"
)


rul = st.number_input(
    "Predicted RUL (Cycles)",
    min_value=0,
    value=150
)



# Status calculation

if rul > 150:

    status = "Healthy"

    recommendation = (
        "Engine is operating normally. "
        "Continue regular monitoring."
    )


elif rul > 50:

    status = "Warning"

    recommendation = (
        "Schedule preventive inspection "
        "within upcoming maintenance cycle."
    )


else:

    status = "Critical"

    recommendation = (
        "Immediate maintenance required. "
        "Inspect engine components."
    )



st.subheader("Prediction Summary")


col1, col2, col3 = st.columns(3)


col1.metric(
    "Engine ID",
    engine_id
)


col2.metric(
    "RUL",
    f"{rul} cycles"
)


col3.metric(
    "Status",
    status
)



st.divider()



# -----------------------------
# Generate PDF
# -----------------------------


def create_pdf():

    file_path = "Aircraft_Engine_Report.pdf"


    document = SimpleDocTemplate(
        file_path
    )


    styles = getSampleStyleSheet()


    content = []


    content.append(
        Paragraph(
            "Aircraft Engine Predictive Maintenance Report",
            styles["Title"]
        )
    )


    content.append(
        Spacer(1, 20)
    )


    report_data = f"""
    Engine ID: {engine_id}<br/>

    Prediction Date:
    {datetime.now().strftime('%Y-%m-%d %H:%M')}<br/>

    Remaining Useful Life:
    {rul} cycles<br/>

    Engine Condition:
    {status}<br/>

    Maintenance Recommendation:
    {recommendation}
    """


    content.append(
        Paragraph(
            report_data,
            styles["Normal"]
        )
    )


    document.build(
        content
    )


    return file_path



if st.button(
    "📄 Generate PDF Report"
):


    pdf_file = create_pdf()


    with open(
        pdf_file,
        "rb"
    ) as file:


        st.download_button(

            label="⬇️ Download Report",

            data=file,

            file_name=
            "Aircraft_Engine_Report.pdf",

            mime=
            "application/pdf"

        )


    st.success(
        "Report generated successfully!"
    )