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
    api_key=AZURE_OPENAI_KEY,
    azure_endpoint=AZURE_ENDPOINT,
    api_version=API_VERSION
)


st.markdown("<h1 style='text-align:center;'>Sentiment Analysis</h1>", unsafe_allow_html=True)
st.write("Analyze text sentiment using **Azure OpenAI + Streamlit**")

text = st.text_area("Enter Your Text")

if st.button("Analyze Sentiment"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            response = client.chat.completions.create(
                model=DEPLOYMENT_NAME,
                messages= [
                    {
                    "role": "user",
                    "content": "you are a sentiment analysis assistant. Classify sentiment as Positive, Negative, or Neutral."
                    },{
                        "role": "user",
                        "content":f"Text: {text}"
                    }
                ]
            )
            sentiment = response.choices[0].message.content.strip()
        if "Positive" in sentiment:
            st.success(f"😊 sentiment: {sentiment}")
        elif "Negative" in sentiment:
            st.error(f"😔 sentiment: {sentiment}")
        else:
            st.info(f"😑 sentiment: {sentiment}")