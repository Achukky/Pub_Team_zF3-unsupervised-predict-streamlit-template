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
        
st.markdown("<div class='head'> The Project </div>", unsafe_allow_html=True)

st.image('https://th.bing.com/th/id/R.f32f6c0a36b1166033122544cf0dd8a1?rik=QmYumf41lwVQgA&pid=ImgRaw&r=0', use_column_width=True)
st.write("""It is almost impossible for a person to attempt to consume all the products and choices available.
 It is even most likely that a person will not have the time, patience or resources to even view the myraids of 
 choices in terms of products and services available at his disposal. Hence, it becomes almost imperative for 
 producers of goods and services to help narrow down the choices of products presented to their users in an 
 attempt to reduce overwhelming them and help them reach thier relevant products and services without waste 
 of time and as a result, helping them have a better user experience, while also exposing them to more products
 and services they might have never discovered otherwise. This help comes in the form of recommendation.

Simple as the above sounds, it is not as easy to implement because the traditional approach would have been to 
deploy product recommender agents (like customer service representatives) who will handle recommendation requests 
from customers. But these agents will be unable to learn about every of thier customers and what products and 
services they might want and find useful. So how does one recommend products and services to people he does not know?

The response is using Recommender Systems. Recommender systems are machine learning systems that help users 
discover products and services based on the relationship between the users and the products.Recommender systems 
are like salesmen who have learnt to recognize customers and the products they might like based on their history
 and preferences. Recommender systems are so common place now that every time you shop online, a  recommendation 
 system is guiding you towards the most likely product you might purchase.

There are several use cases of the recommender system. But this project will focus on movie recommendation.""")

st.markdown("<h2 class='top_head'> How are ratings Distributed? <h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
col1.image('resources/imgs/dist.png')
col2.write("""Most of the movies are rated above average. The Top three most common ratings are 3.0, 4.0 and 5.0. 
Generally, the ratings for movies has been good as the chart skews to the left. A look at the chart, we can observe
 that users prefer to rate movies in integers say 3 than thier float say 3.5. For an instance 1.0 is more frequent 
 than 1.5, 2.0 than 2.5, 3.0 than 3.5 and goes all the way.""")
 
st.markdown("<h2 class='top_head'> What Are the Most Rated Movies of all time ? <h2>", unsafe_allow_html=True)
st.image('resources/imgs/most_rated.png')
st.write("""The most rated movies are movies produced in the 90's. Although, these chart does not determine if 
the movies are positevly or negatively rated. It only shows the total number of ratings they are able to garner. 
The question is, which movies are best rated..""")

st.markdown("<h2 class='top_head'> What Are the Top 10 Movies with Best Average rating ? <h2>", unsafe_allow_html=True)
st.image('resources/imgs/top_10.png')
st.write("""The result of the best rated movies points to the possibility that the best rated movies share genres in common.
 In fact, the best and second best movies where parts I and II of Planet Earth (same movie). From the title of the movies, 
 one can make a blind guess that movies ranked top are between action, adventure and triller genres. We explore the common 
 genres of the top rated movies.  """)