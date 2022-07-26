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

# define demographic recommender function
def recommend(df_ratings, metric, popularity):
    df = df_ratings.groupby('movieId') \
       .agg({'movieId':'count', 'rating':'mean'}) \
       .rename(columns={'movieId':'count','rating':'average_rating'})
    
    # filter the dataset to contain only ratings greather than or equal to metric
    df = df[(df['average_rating'] >= metric) & (df['count'] >= popularity)]
    
    # select movie of the day and other top 10 random movies
    currentDate = datetime.date.today()
    day_of_year = currentDate.timetuple().tm_yday

    return (df.iloc[day_of_year].name, [random.choice(df.index) for x in range(10)])
    
    
# function to get movie details from IMDB using movie id
def get_movie(id):
    link = df_links[df_links['movieId'] == id]['imdbId'].values[0]
    for x in range(0, 4):
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
daily, others = recommend(df_ratings, 4.0, 100)
# get movie of the day
movie_of_day = get_movie(daily)

# get image of other movies
other_movies = list(set([ get_movie(x)['image'] for x in others]))

    

with open('resources/style/home.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
st.markdown("<div class='head'> Spacy </div>", unsafe_allow_html=True)
        
col1, col2, col3 = st.columns([3, 1, 1])

col1.image(movie_of_day['image'], use_column_width=True)

col1.markdown("<h2 class='main_sub_head'> Movie of the Day <h2>", unsafe_allow_html=True)
col1.markdown("<h2 class='day_head'>{}<h2>".format(movie_of_day['title']), unsafe_allow_html=True)

col1.markdown("""<h2 class='desc'>{}<h2>""".format(movie_of_day['desc']), unsafe_allow_html=True)
               
col1.markdown("<a href='https://www.google.com' class='link'> View Movie Overview </a>", unsafe_allow_html=True)

col2.markdown("<h2 class='top_head'> Top Rated Movies <h2>", unsafe_allow_html=True)

col2.image(other_movies[0], use_column_width=True)

col2.image(other_movies[1], use_column_width=True)

col2.image(other_movies[2], use_column_width=True)


col3.image(other_movies[3], use_column_width=True)
col3.image(other_movies[4], use_column_width=True)
col3.image(other_movies[5], use_column_width=True)
