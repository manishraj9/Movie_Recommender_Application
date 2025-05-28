import pickle
import streamlit as st
import requests
import time

# Replace with your actual TMDB API key
TMDB_API_KEY = "502ca94f1328f828ef991f2b66362535"

@st.cache_data(show_spinner=False)
def load_data():
    movies = pickle.load(open('movies.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

@st.cache_data(show_spinner=False)
def fetch_movie_details_with_trailer(movie_id, retries=3, backoff=1):
    base_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": TMDB_API_KEY, "language": "en-US"}

    for attempt in range(retries):
        try:
            url = base_url + "?append_to_response=videos"
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()

            poster_path = data.get("poster_path")
            overview = data.get("overview")
            vote_average = data.get("vote_average")
            release_date = data.get("release_date")
            release_year = release_date.split("-")[0] if release_date else "N/A"
            genres = [genre['name'] for genre in data.get("genres", [])]
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None

            videos = data.get("videos", {}).get("results", [])
            trailer_url = None
            for video in videos:
                if video["type"] == "Trailer" and video["site"] == "YouTube":
                    trailer_url = f"https://www.youtube.com/watch?v={video['key']}"
                    break

            return poster_url, overview, vote_average, release_year, genres, trailer_url

        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                time.sleep(backoff * (2 ** attempt))
                continue
            else:
                st.warning(f"Could not fetch details for movie ID {movie_id}. Error: {e}")
                return None, None, None, None, [], None

def recommend(movie, movies, similarity, selected_genres):
    if movie not in movies['title'].values:
        st.error("Movie not found in database.")
        return []

    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []

    for i in distances[1:60]:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        poster_url, overview, rating, year, genres, trailer_url = fetch_movie_details_with_trailer(movie_id)

        if selected_genres:
            if not set(selected_genres).intersection(set(genres)):
                continue

        recommended_movies.append((title, poster_url, overview, rating, year, genres, trailer_url))
        if len(recommended_movies) >= 36:
            break

    return recommended_movies

def main():
    st.header('🎬 Movie Recommender System')

    movies, similarity = load_data()
    movie_list = movies['title'].values

    search_term = st.text_input("Search for a movie")
    if search_term:
        filtered_movies = [movie for movie in movie_list if search_term.lower() in movie.lower()]
        if filtered_movies:
            selected_movie = st.selectbox("Select a movie from search results", filtered_movies)
        else:
            st.write("No movies found with that name.")
            selected_movie = None
    else:
        selected_movie = st.selectbox("Or select a movie from the dropdown", movie_list)

    all_genres = [
        'Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary',
        'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music',
        'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'Western'
    ]
    selected_genres = st.multiselect("Filter recommendations by genre(s)", all_genres)

    if selected_movie and st.button('Show Recommendations'):
        with st.spinner('Fetching recommendations...'):
            recommendations = recommend(selected_movie, movies, similarity, selected_genres)

        if recommendations:
            cols = st.columns(3)
            for idx, (title, poster, overview, rating, year, genres, trailer_url) in enumerate(recommendations):
                with cols[idx % 3]:
                    with st.container():
                        if poster:
                            st.image(poster, width=220)
                        else:
                            st.write("_Poster not available_")

                        st.markdown(f"### {title} ({year})")
                        st.write(overview[:200] + "..." if overview else "No overview available.")
                        if rating is not None:
                            st.write(f"⭐ Rating: {rating}/10")
                        if genres:
                            st.write("🎞️ Genres: " + ", ".join(genres))

                        with st.expander("Show Trailer"):
                            if trailer_url:
                                st.video(trailer_url, autoplay=True, muted=True, loop=True)
                            else:
                                st.write("_Trailer not available_")

                        st.markdown("<br>", unsafe_allow_html=True)

            st.markdown("---")
        else:
            st.write("No recommendations found matching your criteria.")

if __name__ == '__main__':
    main()
