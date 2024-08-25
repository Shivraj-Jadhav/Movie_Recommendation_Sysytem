import streamlit as st
import pickle
import pandas

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for movie in movie_list:
        recommended_movies.append(movies.iloc[movie[0]].title)
    return recommended_movies


movies_list = movies['title'].values
st.title("Movie Recommender System")

selected_movie = st.selectbox(
'Select Your Favourite Movie',
movies_list
)

if st.button('Recommend'):
    st.write(selected_movie)
    recommendations= recommend(selected_movie)
    for i in recommendations:
        st.write(i)

