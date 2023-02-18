#from turtle import color, position
import streamlit as st
#from textblob import TextBlob
from transformers import pipeline
from streamlit_lottie import st_lottie, st_lottie_spinner
import requests
#from datetime import time
import json
from PIL import Image

image = Image.open("D:\Main_Group.png")

st.image(image)


with open("demo.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.title("Emotion Detection")
st.markdown(
    """
    " We can even break these principal sentiments(positive and negative) into  emotions detection
     such as “Happy”, “Love”, ”Surprise”, “Sad”, “Fear”, “Angry” etc. as per the needs or business requirement" 
"""
) 

from_sent = st.text_area("Enter a Message ", placeholder="Type here...")
if st.button("Click Me 👈"):        
    emotion = pipeline('sentiment-analysis',model= 'bhadresh-savani/distilbert-base-uncased-emotion')
    prediction = emotion(from_sent)
    if prediction[0]["label"] == "fear":
        st.success(prediction)
        lottie_url = "https://assets9.lottiefiles.com/private_files/lf30_qolzpdwh.json"
        lottie_json = load_lottieurl(lottie_url)
        st_lottie(lottie_json,height=100,width=100)
    if prediction[0]["label"] == "anger":
        st.success(prediction)
        lottie_url = "https://assets10.lottiefiles.com/packages/lf20_ffwoyvsy.json"
        lottie_json = load_lottieurl(lottie_url)
        st_lottie(lottie_json,height=100,width=100)
    if prediction[0]["label"] == "sadness":
        lottie_url = "https://assets9.lottiefiles.com/packages/lf20_kyqRXF.json"
        lottie_json = load_lottieurl(lottie_url)
        st_lottie(lottie_json,height=100,width=100)
        st.success(prediction)
    if prediction[0]["label"] == "joy":
        st.success(prediction)
        lottie_url = "https://assets5.lottiefiles.com/packages/lf20_yV8hDU.json"
        lottie_json = load_lottieurl(lottie_url)
        st_lottie(lottie_json,height=100,width=100)
    if prediction[0]["label"] == "love":
        st.success(prediction)
        lottie_url = "https://assets4.lottiefiles.com/packages/lf20_hru9amb4.json"
        lottie_json = load_lottieurl(lottie_url)
        st_lottie(lottie_json,height=100,width=100)
    if prediction[0]["label"] == "surprise":
        st.success(prediction)
        lottie_url = "https://assets5.lottiefiles.com/packages/lf20_cehxtohr.json"
        lottie_json = load_lottieurl(lottie_url)
        st_lottie(lottie_json,height=100,width=100)