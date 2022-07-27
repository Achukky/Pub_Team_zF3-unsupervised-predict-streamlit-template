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
        
st.markdown("<div class='head'> Who We Are </div>", unsafe_allow_html=True)
        
col1, col2 = st.columns([2, 1])

col1.markdown("""<p class='about'> Strataz is an analytics consulting firm that is focused on providing
               organizations with advanced analytic tools that allows them scale. We boost of a competent 
               team which is able to deliver cost effective and efficient tools in handling different business problems
               ranging from marketing to decision making, human mangement etc.</p> """, unsafe_allow_html=True)
               
col2.markdown("<h2 class='top_head'> Our Mission <h2>", unsafe_allow_html=True)
col2.markdown("""<p class='mission'> Our mission is to help organisations optimize the user experience
                of their products and services, within a cost effective budget. </p> """, unsafe_allow_html=True)
                

team1, team2, team3, team4 = st.columns(4)

team1.image('resources/imgs/Abdul.jpg', use_column_width=True)
team1.markdown("<p class='name'> Abubakar Abdulkadir </p>", unsafe_allow_html=True)
team1.markdown("<p class='role'> Team Lead </p>", unsafe_allow_html=True)

team1.image('resources/imgs/joseph.jpg', use_column_width=True)
team1.markdown("<p class='name'> Joseph Okonkwo </p>", unsafe_allow_html=True)
team1.markdown("<p class='role'> Data Scientist </p>", unsafe_allow_html=True)

team2.image('resources/imgs/Ubasinachi.jpg', use_column_width=True)
team2.markdown("<p class='name'> Ubasinachi Eleonu</p>", unsafe_allow_html=True)
team2.markdown("<p class='role'>Data Analyst </p>", unsafe_allow_html=True)

team2.image('resources/imgs/Bongani.jpg', use_column_width=True)
team2.markdown("<p class='name'> Bongani Mkhizee </p>", unsafe_allow_html=True)
team2.markdown("<p class='role'> Product Designer </p>", unsafe_allow_html=True)

team3.image('resources/imgs/Mamah.jpg', use_column_width=True)
team3.markdown("<p class='name'> Micheal Mamah </p>", unsafe_allow_html=True)
team3.markdown("<p class='role'> Data Scientist </p>", unsafe_allow_html=True)

team4.image('resources/imgs/marvic.jpg', use_column_width=True)
team4.markdown("<p class='name'> Micheal Cocourvi </p>", unsafe_allow_html=True)
team4.markdown("<p class='role'> Business Strategist </p>", unsafe_allow_html=True)