# Streamlit dependencies
import streamlit as st
import base64

st.set_page_config(
         page_title="Recommender: Home",
         page_icon=":movie",
         layout="wide"
)

with open('resources/style/home.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
st.markdown("<div class='head'> Movie Recommender System </div>", unsafe_allow_html=True)
        
col1, col2 = st.columns([3, 1])

col1.image('resources/imgs/img.jpg', use_column_width=True)

col1.markdown("<h2 class='day_head'> Godzilla, The King of the Jungle <h2>", unsafe_allow_html=True)

col1.markdown("""<h2 class='desc'> Godzilla is the king of the jungle from whom 
                        he was given many ages to rule his kingdom. He came home 
                        from the wars to bear nights and laughter of the waves but the 
                        tide was gone.
               <h2>""", unsafe_allow_html=True)

col2.markdown("<h2 class='top_head'> Top Rated Movies <h2>", unsafe_allow_html=True)

col2.image('resources/imgs/img.jpg', use_column_width=True)

col2.image('resources/imgs/img.jpg', use_column_width=True)

col2.image('resources/imgs/img.jpg', use_column_width=True)

col2.image('resources/imgs/img.jpg', use_column_width=True)