# 🎬 Movie Recommender System
<p align="center"> <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit&logoColor=white" /> <img src="https://img.shields.io/badge/Machine%20Learning-Content%20Based-orange?style=for-the-badge" /> <img src="https://img.shields.io/badge/TMDB-API-01B4E4?style=for-the-badge&logo=themoviedatabase&logoColor=white" /> </p>

<p align="center"> <img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white" /> <img src="https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" /> <img src="https://img.shields.io/badge/GitHub-Version%20Control-181717?style=for-the-badge&logo=github&logoColor=white" /> <img src="https://img.shields.io/badge/Deployment-Streamlit%20Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" /> </p>

A web-based **Movie Recommendation System** built with Python, Streamlit, and machine learning. The application recommends movies based on content similarity and enriches the recommendations with real-time movie information from **The Movie Database (TMDB) API**, including posters, ratings, genres, descriptions, and trailers.

## 🚀 Live Demo

🎬 **Live Application:**
https://movierecommenderapplicationm.streamlit.app/

## 📌 Features

* 🎬 **Content-Based Movie Recommendation**

  * Recommends movies similar to the selected movie using a pre-trained similarity matrix.

* 🔎 **Movie Search**

  * Search for movies by title and select from matching results.

* 🎭 **Genre Filtering**

  * Filter recommendations by genres such as Action, Adventure, Comedy, Drama, Horror, Romance, Thriller, and more.

* 🖼️ **Movie Posters**

  * Fetches movie posters dynamically using TMDB.

* ⭐ **Movie Ratings**

  * Displays TMDB ratings for recommended movies.

* 📝 **Movie Overview**

  * Shows a short description of each recommended movie.

* 🎞️ **Genre Information**

  * Displays the genres associated with each movie.

* ▶️ **Movie Trailers**

  * Provides YouTube trailers when available.

* 🎥 **Animated Background**

  * Uses a custom background video to enhance the user interface.

* ☁️ **Cloud Deployment**

  * Deployed using Streamlit Community Cloud.

## 🧠 How It Works

The system uses a **content-based recommendation approach**.

The movie dataset contains information about thousands of movies. A similarity matrix is used to calculate how closely related movies are to one another.

The recommendation flow is:

```text
User selects a movie
        ↓
Movie title is searched in the dataset
        ↓
Similarity scores are calculated
        ↓
Most similar movies are selected
        ↓
Genre filters are applied
        ↓
TMDB API fetches movie metadata
        ↓
Posters + Overview + Rating + Genres + Trailer
        ↓
Recommendations displayed in Streamlit
```

## 🛠️ Tech Stack

### Programming Language

* Python

### Machine Learning / Data Processing

* Pandas
* NumPy
* Scikit-learn
* Pickle

### Web Application

* Streamlit

### API

* TMDB API
* YouTube trailer links

### Deployment

* Streamlit Community Cloud

### Development Tools

* VS Code
* Git
* GitHub

## 📂 Project Structure

```text
Movie_Recommender_Application/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── video.mp4
├── movierecommdersystem.ipynb
├── requirements.txt
├── README.md
├── .gitignore
│
├── .streamlit/
│   └── config.toml
│
├── assests/
│
└── static/
```

### Important Files

| File                         | Description                             |
| ---------------------------- | --------------------------------------- |
| `app.py`                     | Main Streamlit application              |
| `movies.pkl`                 | Processed movie dataset                 |
| `similarity.pkl`             | Precomputed movie similarity matrix     |
| `video.mp4`                  | Background video                        |
| `movierecommdersystem.ipynb` | Notebook used for model/data processing |
| `requirements.txt`           | Python dependencies                     |
| `.streamlit/config.toml`     | Streamlit configuration                 |

## ⚙️ Installation & Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/manishraj9/Movie_Recommender_Application.git
```

### 2. Move into the project directory

```bash
cd Movie_Recommender_Application
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the TMDB API key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
TMDB_API_KEY = "YOUR_TMDB_API_KEY"
```

**Never commit `secrets.toml` to GitHub.**

### 6. Run the application

```bash
python -m streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

## 🔐 API Security

The TMDB API key is stored using Streamlit Secrets rather than being hardcoded into the public repository.

The following file should remain private:

```text
.streamlit/secrets.toml
```

It is excluded using `.gitignore`.

## 📊 Recommendation Method

This project uses **content-based filtering**.

Instead of relying on user ratings or collaborative behavior, the system recommends movies based on the similarity between movie features.

The precomputed similarity matrix is stored in:

```text
similarity.pkl
```

When a user selects a movie, the application retrieves its similarity scores and returns the most similar movies.

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

Every update pushed to the `main` branch can trigger a new deployment.

**Live Demo:**

https://movierecommenderapplicationm.streamlit.app/

## 🔮 Future Improvements

* 👤 User-based personalized recommendations
* ❤️ Favorite/watchlist functionality
* 🔐 User authentication
* 🌟 Personalized recommendations based on ratings
* 🧠 Hybrid recommendation system
* 🔍 Advanced movie search
* 🎭 More detailed genre filtering
* 📈 Recommendation analytics
* 💬 AI-powered movie chatbot
* 🎞️ Improved trailer and streaming information
* 📱 Improved mobile responsive UI

## 👨‍💻 Author

**Manish Raj Aryan**

B.Tech Computer Science & Engineering

GitHub:
https://github.com/manishraj9

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

### 📜 License

This project is intended for educational and portfolio purposes.

