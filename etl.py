import pandas as pd
import sqlite3
import requests
import time

API_KEY = "YOUR_API_KEY"   # 👈 paste your OMDb key here

print("ETL started")

# -------- EXTRACT --------
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")
print("CSV files loaded")

# -------- TRANSFORM --------
movies["year"] = movies["title"].str.extract(r"\((\d{4})\)")
movies["year"] = movies["year"].astype("float")

# -------- OMDb API FUNCTION --------
def fetch_omdb_details(title):
    clean_title = title.split("(")[0].strip()
    url = f"http://www.omdbapi.com/?t={clean_title}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        return data.get("Director"), data.get("Plot")
    else:
        return None, None

# -------- API CALL (LIMITED) --------
directors = []
plots = []

print("Calling OMDb API (first 50 movies)...")

for title in movies["title"].head(50):
    director, plot = fetch_omdb_details(title)
    directors.append(director)
    plots.append(plot)
    time.sleep(0.2)   # avoid API limit

# Fill remaining rows with NULL
while len(directors) < len(movies):
    directors.append(None)
    plots.append(None)

movies["director"] = directors
movies["plot"] = plots

print("OMDb enrichment completed")

# -------- LOAD --------
conn = sqlite3.connect("movies.db")
movies.to_sql("movies", conn, if_exists="replace", index=False)
ratings.to_sql("ratings", conn, if_exists="replace", index=False)
conn.close()

print("Data loaded into database successfully")
