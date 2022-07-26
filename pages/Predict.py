# Streamlit dependencies
import streamlit as st
import base64
import pandas as pd
import pickle as pkl
from collections import Counter
import os

st.set_page_config(
         page_title="Recommender: Home",
         page_icon=":movie",
         layout="wide"
)

#df_movies = pd.read_csv('../unsupervised_data/movies.csv')
#df_train = pd.read_csv('../unsupervised_data/train.csv')

with open('resources/style/home.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
st.write(os.path.abspathgetcwd('../'))