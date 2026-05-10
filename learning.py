import numpy as np 
import pandas as pd

# Numpy
vector = np.array([10,20,30,40])
print(vector)
print(vector[0])
print(vector[0:2])
print(vector.shape)
print(vector*2) # multiply vector by 2
print(vector-1) # subtract 1
print(vector+vector) # adds each corresponding part of vector
print(np.version)

idx=np.array([0,2,1,1])
print(vector[idx])

mask=np.array([False,True,True,False])
print(vector[mask])

# mask=[None, None, None, None]
# for i in range(4):
#    mask[i]=vector[i]>25
#mask=np.array(mask)

# filter
# mask=vector >25
print(vector[vector>25])

# Pandas :) 
data = {
    "title":["Toy Story", "Project Hail Mary", "Jumanji"],
    "genre":["Animation","Scifi","Comedy"],
    "rating":[3,5,4]
}

# CSV format
# title, genre, rating
# Toy Story, Animation, 3
# Project Hail Mary,SciFi,5
#Jumanji,Comedy,4

df=pd.DataFrame(data)
print(df)

print(df["title"])
print(df["title","rating"])

print(df["rating"].sum()) # Pandas data act as a numpy array
print(df["rating"].mean()) #returns 4.0


print(list(df["rating"]*2))  # [6,10,8]

df["double"]=df["rating"]*2
print(df)

mask = df["rating"]>3 # gets entire dataframe for movies where rating > 3

mask=df["genre"]=="Scifi"
print(df[mask]) # filters movies with only sci fi genre

print(list(df["title"].str.lower()))
print(df)

