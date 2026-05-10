import numpy as np
import pandas as pd

## NUMPY

vector = np.array([10, 20, 30, 40])
print(vector)
print(vector[0])
print(vector[0:2])
print(vector.shape)

matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

print(vector.dot(vector))
print(vector.sum())
print(vector.min())

idx = np.array([0, 2, 1, 1])
print(vector[idx])

mask = np.array([False, True, True, False])
print(vector[mask])

# mask = [None, None, None, None]
# for i in range(4):
#     mask[i] = vector[i] > 25
# mask = np.array(mask)

# "filter"
print(vector[vector > 25])



## PANDAS

data = {
    "title": ["Toy Story", "Project Hail Mary", "Jumanji"],
    "genre": ["Animation", "Scifi", "Comedy"],
    "rating": [3, 5, 4],
}

# movies.csv
# title,genre,rating
# Toy Story,Animation,3
# Project Hail Mary,Sci,5
# Jumanji,Comedy,4

df = pd.DataFrame(data)
print(df)

# print(df[["title", "rating"]])
print(df["rating"].sum())

df["double"] = df["rating"] * 2
print(df)

mask = df["rating"] > 3
print(df[mask])

mask = df["genre"] == "Scifi"
print(df[mask])

df["title"] = df["title"].str.lower()

# print(pd.read_csv("./ml-32m/movies.csv"))

print(df)


## Practice Problems

# TODO: Download ml-32m dataset and load all 4 csvs
# Use df = pd.read_csv("./ml-32m/movies.csv")

# TODO: Check shapes of dataframs and print them
# TODO: Use .head() to display first n rows of movies
# TODO: Find number of unique users in ratings
# TODO: Find number of unique movies
# TODO: Find movies with rating of 1
# TODO: Find ratings associated with a movie (by ID)
# TODO: Find ratings associated with a movie (by Title)

# TODO: Genres column is split by | right now, split that column
# so it is a list of strings and put it back in the df

