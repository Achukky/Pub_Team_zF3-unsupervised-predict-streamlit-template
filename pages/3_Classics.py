# Streamlit dependencies
import streamlit as st
import base64
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import random

st.set_page_config(
         page_title="Recommender: Home",
         page_icon=":movie",
         layout="wide"
)

# Get datasets
df_ratings = pd.read_csv('resources/data/train.csv')
df_links = pd.read_csv('resources/data/links.csv')
df_movies = pd.read_csv('resources/data/movies.csv')

with open('resources/style/home.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
st.markdown("<div class='head'> Classic Movies </div>", unsafe_allow_html=True)

# recommender function
def recommend_classic(df_movies, df_ratings, metric, popularity, year):
    df_movies['year'] = df_movies['title'].apply(extract_year)
    df_movies = df_movies[df_movies['year'] <= year]
    df_movies_ratings = df_movies[['movieId', 'title', 'year']].merge(df_ratings[['movieId', 'rating']], on='movieId')
    df = df_movies_ratings.groupby('movieId') \
       .agg({'movieId':'count', 'rating':'mean'}) \
       .rename(columns={'movieId':'count','rating':'average_rating'})
    
    # filter the dataset to contain only ratings greather than or equal to metric
    df = df[(df['average_rating'] >= metric) & (df['count'] >= popularity)]
    
    # select movie of the day and other top 5 random movies
    currentDate = datetime.date.today()
    day_of_year = currentDate.timetuple().tm_yday % len(df)

    return (df.iloc[day_of_year].name, [random.choice(df.index) for x in range(6)])

# Extract production year from movie title
def extract_year(title):
    year = title.split('(')
    if len(year) > 1:
        try:
            year = int(year[1][0:4])
            if year > 1500:
                return year
        except:
            pass
            
            
# function to get movie details from IMDB using movie id
def get_movie(id):
    link = df_links[df_links['movieId'] == id]['imdbId'].values[0]
    for x in [2, 1, 0]:
        URL = "https://www.imdb.com/title/tt{}{}/".format("0" * x, link)
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        title = soup.find('h1', attrs= {'data-testid':"hero-title-block__title", "class":"sc-b73cd867-0"})
        if title:
            title = title.text
            break

    cover_image = soup.find('img', attrs = {'class':'ipc-image'})['src']
    desc = soup.find('span', attrs= {'data-testid':"plot-xs_to_m"}).text

    return {'title':title, 'image':cover_image, 'desc':desc}
    

# Recommend movie Daily and other popular movies 
daily, others = recommend_classic(df_movies, df_ratings, 3.5, 50, 1999)

# get movie of the day
movie_of_day = get_movie(daily)

# get image of other movies
other_movies = list(set([ get_movie(x)['image'] for x in others]))

        
col1, col2, col3 = st.columns([1, 1, 2])

col1.image(other_movies[0], use_column_width=True)
col1.image(other_movies[1], use_column_width=True)
col1.image(other_movies[2], use_column_width=True)

col2.image(other_movies[3], use_column_width=True)
col2.image(other_movies[4], use_column_width=True)
col2.image(other_movies[5], use_column_width=True)

col3.markdown("<h2 class='main_sub_head'> Classic Movie Of the Day <h2>", unsafe_allow_html=True)
col3.image(movie_of_day['image'], use_column_width=True)
col3.markdown("<h2 class='day_head'>{}<h2>".format(movie_of_day['title']), unsafe_allow_html=True)

col3.markdown("<h2 class='desc'>{}<h2>".format(movie_of_day['desc']), unsafe_allow_html=True)


