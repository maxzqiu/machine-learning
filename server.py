from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas
import numpy as np

app=FastAPI()
origins = [
    "http://localhost:3000",      # React default port
    "http://localhost:5173",      # Vite / Vue default port
    
]

# 2. Add the middleware to your FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Allow requests from these domains
    allow_credentials=True,          # Allow cookies and auth headers
    allow_methods=["*"],             # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],             # Allow all request headers
)
df=pandas.read_pickle("tf_idf_pickle.pkl")
df_json=[]
for index, row in df.iterrows():
    df_json.append({
        "title":row["title"],
        "genre":row["genres"],
        "tf_idf":row["tf_idf"].tolist()
    })

def topKMovies(movie,top_k=5):
    try:
        
        mask=df["title"]==movie
        print("here")
        vector=df[mask]["tf_idf"].item()
        angle_list=[]
        for i,row in df.iterrows():
            
            angle_list.append([angleBetweenVectors(vector,row["tf_idf"]),row["title"],row["genres"]])
        angle_list.sort()
        print("made it to the end")
        return angle_list[0:top_k]
    except:
        print("exception")
        return [400]

    
    
    

def angleBetweenVectors(a,b):
    dotproduct=np.dot(a,b)
    
    a_length=np.linalg.norm(a)
    b_length=np.linalg.norm(b)
    
    return np.arccos(dotproduct/(a_length*b_length))
# { movies: [
# Toy Story: {
#    genre,tf_idf
# }
# ]
# }
#
#

@app.get("/")
def root():

    return {
        "brain":"stupid",
        "body":"fat",
        "name":"Max"
    }

@app.get("/api")
def api(title:str,top_k:int):
    print(topKMovies(title,top_k))
    return topKMovies(title,top_k)

