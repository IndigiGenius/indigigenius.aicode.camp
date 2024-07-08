
import pandas as pd

path_prefix = "./week_one/notebooks/4 - Day Four/"

links_small = pd.read_csv(path_prefix + "links_small.csv")
ratings_small = pd.read_csv(path_prefix + "ratings_small.csv")

# Clean Credits dataset
credits = pd.read_csv(path_prefix + "credits.csv")
credits["id"] = pd.to_numeric(credits["id"], errors="coerce")
credits.dropna(inplace=True)

# Clean Metadata dataset
movies_metadata = pd.read_csv(path_prefix + "movies_metadata.csv")
movies_metadata.rename({"imdb_id": "imdbId"}, axis=1, inplace=True)
movies_metadata["imdbId"] = pd.to_numeric(movies_metadata["imdbId"].str[2:], errors="coerce")
movies_metadata["id"] = pd.to_numeric(movies_metadata["id"], errors="coerce")
movies_metadata.dropna(subset=["imdbId", "id"], inplace=True)
movies_metadata.to_csv("new_movies.csv")

# Get Rating Statistics
compiled_ratings = pd.merge(ratings_small, links_small, on="movieId", how="inner")
compiled_ratings = compiled_ratings.groupby("movieId").agg(["mean", "count", "std"])["rating"].reset_index()
compiled_ratings.dropna(inplace=True)
compiled_ratings.columns = ["movieId"] + ["ratings_" + col for col in compiled_ratings.columns if col != "movieId"]

# Merge datasets into one
compiled_ratings = pd.merge(compiled_ratings, links_small, on="movieId")
compiled_dataset = pd.merge(compiled_ratings, movies_metadata, on="imdbId")
compiled_dataset = pd.merge(compiled_dataset, credits, on="id")

# Export Dataset
compiled_dataset.to_csv("movie_dataset_final.csv", index=False)
