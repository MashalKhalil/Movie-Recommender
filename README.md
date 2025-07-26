# 🎬 Movie Recommender System

A Content-Based Movie Recommendation System built using Python and machine learning techniques. This project uses the TMDB 5000 Movie Dataset and recommends similar movies based on content like genres, cast, crew, keywords, and overview.

## 🔍 Features

- Merges two datasets: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`
- Extracts and cleans relevant columns like genres, keywords, cast, crew, and overview
- Creates a new feature (`tags`) by combining all important content
- Applies **Natural Language Processing (NLP)** techniques including:
  - Text normalization (lowercasing, stemming)
  - Vectorization using `CountVectorizer`
  - Cosine similarity to find and rank similar movies
- Provides top 5 movie recommendations based on the selected movie
- Pickle files for easy deployment and integration into web apps

---

## 📁 Dataset

The project uses two datasets:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

These are publicly available on [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

---

## 🧠 Model Workflow

1. **Data Preprocessing**
   - Merge datasets on the movie title
   - Drop unnecessary and null values
   - Clean and parse `genres`, `keywords`, `cast`, and `crew` columns

2. **Feature Engineering**
   - Create a new `tags` column combining overview, genres, keywords, cast, and director
   - Normalize text and apply stemming using NLTK's `PorterStemmer`

3. **Vectorization**
   - Convert `tags` column into numerical vectors using `CountVectorizer`
   - Limit vocabulary size to 5000 and remove English stop words

4. **Similarity Calculation**
   - Use cosine similarity to compute similarity scores between movies

5. **Recommendation Function**
   - Recommend top 5 similar movies based on cosine similarity scores

---
## 🖥️ Web App with Streamlit

A sleek and interactive **web interface** is built using [Streamlit](https://streamlit.io/) to allow users to easily get movie recommendations with a single click!

### ✅ Features:
- Clean, centered UI with responsive layout and custom styling using HTML & CSS
- Dropdown menu to select a movie from the list
- "✨ Recommend Similar Movies" button to fetch top 5 similar movies
- Dynamic fetching of **movie posters** using the [TMDB API](https://developer.themoviedb.org/)
- Movie titles displayed beautifully under each poster
- User-friendly loading indicator and graceful error handling

### 🧪 Technologies Used:
- **Streamlit** – for building the interactive web UI
- **Pickle** – to load the trained model and preprocessed data
- **Requests** – for calling the TMDB API to fetch movie poster images
- **Pandas** – to handle and manipulate movie data

---

### 🚀 How to Run the Web App Locally

1. Clone the repository:

```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
