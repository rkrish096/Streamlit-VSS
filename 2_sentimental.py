# from turtle import color, position
import streamlit as st
#from textblob import TextBlob
from transformers import pipeline
# from streamlit_lottie import st_lottie, st_lottie_spinner
# import requests
# from datetime import time
# import json
from PIL import Image

image = Image.open("D:\pn (2).png")

st.image(image)


with open("demo.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)



st.title("Sentimental Analysis")
st.markdown(
    """
    " Sentiment Analysis, as the name suggests, it means to identify the view or human behaviour behind a sentences. 
    It basically means to analyze and find the postive and Negative behind a piece of text communication ". 
"""
) 

from_sent = st.text_area("Enter a Message ", placeholder="Type here...")
if st.button("Click Me 👈"):
    #model_path = 'cardiffnlp/twitter-xlm-roberta-base-sentiment'
    #sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
    #prediction = sentiment_task(from_sent)
    sentiment_analysis = pipeline("sentiment-analysis",model="siebert/sentiment-roberta-large-english")
    prediction = sentiment_analysis(from_sent)
    if prediction[0]["label"] == "POSITIVE":
        st.success(prediction)                

    if prediction[0]["label"] == "NEGATIVE":
        st.error(prediction)
