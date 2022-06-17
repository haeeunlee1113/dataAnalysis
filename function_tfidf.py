import os
import pickle
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from config import model_dir, rsc_dir

class tfidf_predictor():
    def __init__(self):
        # variables
        self.vector_loads = []
        self.model_loads = []
        self.model_num = 5

        for i in range(0, self.model_num):
            # file names
            vector_file_dir = os.path.join(model_dir, 'tfidf_vector_201128_aug_%d.pkl' %i)
            model_file_dir = os.path.join(model_dir, 'tfidf_logreg_201128_aug_%d.pkl' %i)

            # load files
            self.vector_loads.append(joblib.load(vector_file_dir))
            self.model_loads.append(joblib.load(model_file_dir))

    def predict(self, body:str) -> tuple:
        weights = [] # a list to save weights of a number of models

        for i in range(0, self.model_num):
            # calculate weight
            test_matrix = self.vector_loads[i].transform([body])
            confidence = self.model_loads[i].predict_proba(test_matrix)[0, 1]

            # save confidence as ith weight
            weights.append(confidence)

        return sum(weights) / len(weights)