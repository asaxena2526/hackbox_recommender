import numpy as np
import pandas 
import pickle
import scipy.sparse as sp
from scipy.sparse.linalg import svds

movie_score = pandas.read_csv('Movie_score_overall.csv')

def best_movies_by_genre(genre,top_n):
    ans =  pandas.DataFrame(movie_score.loc[(movie_score[genre]==1)].sort_values(['weighted_score'],ascending=False)[['title','count','mean','weighted_score']][:top_n])
    out = ans.reset_index()
    return out['title'].tolist()
