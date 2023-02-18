from turtle import color, position
import streamlit as st
from textblob import TextBlob
from transformers import pipeline
from streamlit_lottie import st_lottie, st_lottie_spinner
import requests
from datetime import time
import json
from PIL import Image

image = Image.open("D:\Group.png")

st.image(image)


with open("demo.css") as source_des:
        st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

st.title("Natural Language Processing.")

def main():
    
    
    st.markdown(
    """
    
"Natural Language Processing (NLP) is a branch of Artificial Intelligence (AI) that enables machines to understand the human language.
Its goal is to build systems that can make sense of text and automatically perform tasks like translation, spell check, or topic classification"

please select the side bar for the operation 👈

- Sentiment Analysis
- Emotion Detection


"""
)     
  
if __name__ == "__main__":
    main()
