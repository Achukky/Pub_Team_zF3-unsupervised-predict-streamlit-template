"""

    Content-based filtering for item recommendation.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: You are required to extend this baseline algorithm to enable more
    efficient and accurate computation of recommendations.

    !! You must not change the name and signature (arguments) of the
    prediction function, `content_model` !!

    You must however change its contents (i.e. add your own content-based
    filtering algorithm), as well as altering/adding any other functions
    as part of your improvement.

    ---------------------------------------------------------------------

    Description: Provided within this file is a baseline content-based
    filtering algorithm for rating predictions on Movie data.

"""

# Script dependencies
import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pickle as pkl
import math

# read the ratings dataset
df_rating = pd.read_csv('resources/data/train.csv')

# read the ratings dataset
df_movies = pd.read_csv('resources/data/movies.csv')

# read the movie additional information
df_meta = pd.read_csv('resources/data/imdb_data.csv')

with open('resources/models/features.pkl', 'rb') as file:
    features = pkl.load(file)


def data_preprocessing(subset_size):
    """Prepare data for use within Content filtering algorithm.

    Parameters
    ----------
    subset_size : int
        Number of movies to use within the algorithm.

    Returns
    -------
    Pandas Dataframe
        Subset of movies selected for content-based filtering.

    """
    # handle missing data
    df_train.fillna(' ', inplace=True)

    # replacing "|" and "(no genres listed)" with ' ' in genre
    df_train['genres'] = df_train['genres'].apply(lambda x: x.replace("|" , ' ')
                                           .replace("(no genres listed)", ' '))

    # replacing " " with ' ' in director
    df_train['director'] = df_train['director'].apply(lambda x: ((x+'|'))
                                                .replace(" ", '')
                                                .replace("|", " "))

    # replace "|" with ' ' in plot_keywords
    df_train['plot_keywords'] = df_train['plot_keywords'].apply(lambda x: x.replace("|", " "))

    # Merge the genres, plot_keywords and director names as our major predictors
    df_train_string = df_train['genres'] + " " + df_train['director'] + " " + df_train['plot_keywords']

    # change to lower case
    df_train_string.apply(str.lower)
    
    return df_train_string
    
    

# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.  
def content_model(movie_list,top_n=10):
    """Performs Content filtering based upon a list of movies supplied
       by the app user.

    Parameters
    ----------
    movie_list : list (str)
        Favorite movies chosen by the app user.
    top_n : type
        Number of top recommendations to return to the user.

    Returns
    -------
    list (str)
        Titles of the top-n movie recommendations to the user.

    """
    each_number =  math.ceil(top_n / 3)
    top_rated_movies_id = list(df_movies[df_movies['title'].isin(movie_list)]['movieId'])
    unseen_movies = list(df_movies[~ df_movies['movieId'].isin(top_rated_movies_id)].index)
    
    similarity_list = []
    
    for movieId in list(top_rated_movies_id):
        movie_index = df_movies[df_movies['movieId'] == movieId].index[0]
        sim_matrix = cosine_similarity(features[movie_index], features[unseen_movies])[0]
        
        for i in range(each_number):
            similarity_list.append(np.argmax(sim_matrix))
            sim_matrix[np.argmax(sim_matrix)] = 0
        
    return list(df_movies.iloc[similarity_list].head(top_n)['title'])
