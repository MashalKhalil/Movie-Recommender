import streamlit as st
import pickle
import pandas as pd
import requests

# --- Set Page Config ---
st.set_page_config(page_title="Movie Recommender", page_icon="🎥", layout="wide")

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 20px;
    }
    .movie-title {
        text-align: center;
        font-size: 16px;
        font-weight: 600;
        margin-top: 10px;
    }
    img {
        border-radius: 10px;
    }
    .stButton>button {
        width: 100%;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 16px;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Helper Function to Fetch Poster ---
def fetch_poster(movie_id):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=ae70e094bc73887d6aa2bcc6c4626360&language=en-US'
        )
        data = response.json()
        return "https://image.tmdb.org/t/p/w500" + data.get('poster_path', '')
    except:
        return "https://via.placeholder.com/500x750?text=No+Image"

# --- Recommendation Logic ---
def recommend(movie):
    if movie not in movies['title'].values:
        return [], []

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        index = i[0]
        movie_id = movies.iloc[index].movie_id
        recommended_movies.append(movies.iloc[index].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# --- Load Data ---
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# --- App Title ---
st.markdown('<div class="title">🎬 Movie Recommender System</div>', unsafe_allow_html=True)

# --- Movie Selection ---
option = st.selectbox('🎞️ Select a movie you like:', movies['title'].values)

# --- Recommend Button ---
if st.button('✨ Recommend Similar Movies'):
    with st.spinner('🔍 Finding best matches...'):
        names, posters = recommend(option)

        if names:
            st.markdown("### 🍿 Top 5 Recommendations for You")
            cols = st.columns(5)

            for i in range(len(names)):
                with cols[i]:
                    st.image(posters[i], use_container_width=True)
                    st.markdown(f'<div class="movie-title">{names[i]}</div>', unsafe_allow_html=True)

        else:
            st.error("⚠️ No recommendations found. Please try a different movie.")
