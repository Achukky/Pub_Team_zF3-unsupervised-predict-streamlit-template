# Streamlit dependencies
import streamlit as st
import base64
import pandas as pd
import pickle as pkl
from collections import Counter

st.set_page_config(
         page_title="Recommender: Home",
         page_icon=":movie",
         layout="wide"
)

df_movies = pd.read_csv('../unsupervised_data/movies.csv')
df_train = pd.read_csv('../unsupervised_data/train.csv')

with open('resources/style/home.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
st.markdown("<div class='head'> Predict Your Rating </div>", unsafe_allow_html=True)
st.write("Select a movie lets help your predict if you will like them or not")

# function to filter low rating users
def filter_low_rating_users(df, min_no_rating):
    users_per_rating = dict(Counter(df.userId))
    required_users = []
    
    for key, value in users_per_rating.items():
        if value > min_no_rating:
            required_users.append(key)
        
    return df[df['userId'].isin(required_users)]

# function to filter low rated movies    
def filter_low_rated_movies(df, min_no_rating):
    movies_per_rating = dict(Counter(df.movieId))
    required_movies = []
    
    for key, value in movies_per_rating.items():
        if value > min_no_rating:
            required_movies.append(key)
        
    return df[df['movieId'].isin(required_movies)]
    
# Configurable minimum number of movie and users ratings
min_no_movie_rating = 2200
min_no_user_rating = 180

# Filter the training set with the configuration
training_set = filter_low_rated_movies(df_train, min_no_movie_rating)
training_set = filter_low_rating_users(training_set, min_no_user_rating)

movies = df_movies[df_movies['movieId'].isin(training_set['movieId'].unique())]

col1, col2 = st.columns(2)
userId = col1.selectbox('Select your User ID', training_set['userId'].unique())
movie_title = col2.selectbox('Choose a Movie', movies['title'].unique())

movieId = list(df_movies.loc[df_movies['title'] == movie_title, 'movieId'])[0]

predict = st.button("Predict Rating")

if predict:
    with open('resources/models/model.pkl', 'rb') as file:
        model = pkl.load(file)
       
    st.success("Predicted Rating : {}".format(round(model.predict(userId, movieId, verbose=False).est, 2)))