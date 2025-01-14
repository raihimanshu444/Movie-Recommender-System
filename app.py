import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    matched_movies = movies_list[movies_list['title'] == movie]

    if matched_movies.empty:
        st.error(f"Movie '{movie}' not found.")
        return []

    movie_index = matched_movies.index[0]
    distances = similarity[movie_index]

    # Get the top 5 recommendations based on similarity
    movies_list1 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster=[]
    for i in movies_list1:
        movie_id=movies_list.iloc[i[0]].movie_id

        recommended_movies.append(movies_list.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_poster


st.title('Movie Recommender System')

# Load the movie dataset and the similarity matrix
movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_titles = movies_list['title'].values

selected_movie_name = st.selectbox(
    "Select a movie for recommendations:",
    movies_titles,
)

if st.button("Recommend"):
    names,posters= recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
