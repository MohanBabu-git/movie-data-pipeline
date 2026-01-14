CREATE TABLE IF NOT EXISTS movies (
    movieId INTEGER PRIMARY KEY,
    title TEXT,
    genres TEXT,
    year INTEGER,
    director TEXT,
    plot TEXT
);

CREATE TABLE IF NOT EXISTS ratings (
    ratingId INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INTEGER,
    movieId INTEGER,
    rating REAL,
    timestamp INTEGER,
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);
