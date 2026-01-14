

## Overview
This project implements a complete ETL pipeline that ingests movie data from CSV files,
enriches it using the OMDb external API, and loads the processed data into a SQLite database
for analytical querying.

## Data Sources
- MovieLens Small Dataset (movies.csv, ratings.csv)
- OMDb API (Director, Plot)

## Tech Stack
- Python
- Pandas
- SQLite
- OMDb API

## How to Run
1. Install dependencies:
   pip install pandas requests
2. Run the ETL pipeline:
   python etl.py

## ETL Steps
- Extract: Read movie and rating data from CSV files
- Transform: Clean data and extract release year from titles
- Enrich: Fetch director and plot details using OMDb API
- Load: Store processed data into SQLite database

## Database Schema
- movies(movieId, title, genres, year, director, plot)
- ratings(userId, movieId, rating, timestamp)

## Challenges & Handling
- API rate limits handled by limiting calls and adding delays
- Missing API data handled gracefully using NULL values

## Improvements
- Enrich full dataset with API
- Normalize genres into separate table
- Use Airflow for scheduling
