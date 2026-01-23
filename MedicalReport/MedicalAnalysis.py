import streamlit as st
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")
API_VERSION = os.getenv("AZURE_API_VERSION")

client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY, azure_endpoint=AZURE_ENDPOINT, api_version=API_VERSION
)

st.title("Medical Report Analysis")
st.caption("This project is used to analysis the report and give a short and understandable form of report..")

medical_report = st.text_area(
    "Enter your report.",
    height=250,
    placeholder="Paste clinical notes, lab report, discharge summary...",
)

if st.button("Analyze Report"):
    if medical_report.strip() == "":
        st.warning("Enter your Report")
    else:
        with st.spinner("Analyzing report..."):
            response = client.chat.completions.create(
                model=DEPLOYMENT_NAME,
                messages=[

                    {

                        "role": "system",
                        "content": """You are a medical document assistant that extracts and organizes information from clinical reports.
                        Your responsibilities:
                            - Extract information exactly as stated in the report
                            - Organize content into clear, structured sections
                            - Use simple, patient-friendly language
                            - Never add diagnoses, interpretations, or medical advice not present in the original report
                            - If a section has no information in the report, state "Not mentioned in report"
                            - Maintain patient confidentiality and handle all information professionally""",

                    },


                    {
                        "role": "user",
                        "content": f"""
                        Summarize the following medical report using:
                        - Patient Information 
                        - Chief Complaint
                        - Key Findings
                        - Symptoms
                        - Medications
                        - Follow-up Advice
                        - Guidelines
                        

                        Medical Report:
                        {medical_report}
                        """,
                    },
                ],
                temperature=0.2 #this will tell ai how to work.this is very important,
            )
        st.subheader("Report Summary")
        st.warning(response.choices[0].message.content)

        st.error(
            "This is AI-generated summary for reference only. Consult a medical professional soon."
        )
