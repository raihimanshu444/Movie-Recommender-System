# Movie-Recommender-System
A movie recommendation system built with Python, Streamlit, and TMDb API. 
It provides movie recommendations based on user selection.

#Features

Movie recommendations based on similarity.
Displays movie posters and titles.
Interactive UI built with Streamlit.

#Prerequisites
Python 3.6+

#Install dependencies:
pip install -r requirements.txt

#Setup
Clone the repo:

git clone https://github.com/raihimanshu444/movie-recommender-system.git
cd movie-recommender-system

Get a TMDb API Key from TMDb API and replace it in the code.
Running Locally
Run the app:
streamlit run app.py

Open http://localhost:8501 in your browser.

##Deployment on Heroku
Install Heroku CLI.
Create a Procfile:
web: streamlit run app.py

#Deploy:

git init
git add .
git commit -m "Initial commit"
heroku create
git push heroku master
heroku open

#Troubleshooting
Make sure movies.pkl and similarity.pkl are in your project directory.
Ensure your TMDb API key is valid.

