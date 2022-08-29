import pandas as pd
import datetime
import time
import pickle
import numpy as np
from sklearn.neighbors import NearestNeighbors

class ModelHelper():
    def __init__(self):
        self.model_load = pickle.load(open("model_knn.h5", 'rb'))
        self.KNN_top_tracks_proc = pd.read_csv("KNN_top_tracks_proc.csv")
        self.KNN_top_tracks_alpha = pd.read_csv("KNN_top_tracks_alpha.csv")
        # pass

    def recommender(self, song):
       
        distances, indices = self.model_load.kneighbors(self.KNN_top_tracks_proc.loc[song].to_numpy().reshape(1,-1), 11)
        rtn = self.KNN_top_tracks_alpha.loc[indices[0]]
        rtn["distance"]=distances[0]

        return (rtn)