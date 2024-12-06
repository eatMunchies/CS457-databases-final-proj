"""
Anthony Silva
CS 457
Final Project
11/18/24
File: Predictor.py
Description: This file contains the Predictor class 
"""

import sklearn as sk
import pandas as pd
import numpy as np
from datetime import datetime

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor

class Predictor:
    sessionPredictions = 0

    def __init__(self):
        pass

    def predictUsingAlgorithm(self, df: pd.DataFrame, options: dict):
        """
        This function takes in a dataframe and predicts future data using a specific algorithm.
        """
        
        algorithm = options['algorithm'] # actual function to call

        column = options['column']

        date = options['date']
        prediction = 0

        # use sklearn to predict future data

        # X = np.array(df.index).reshape(-1, 1) # this only works if the index is a date
        X = df[['date_ordinal']]
        Y = np.array(df[column])

        model = algorithm()
        model.fit(X, Y)
        
        ordinal_date = datetime.strptime(date, '%Y-%m-%d').toordinal()
        prediction = model.predict([[ordinal_date]])

        self.sessionPredictions += 1

        return prediction

    def runPredictions(self, df: pd.DataFrame, options: dict):
        """
        This function takes in a dataframe and runs all the predictions.
        """

        # acceptable algorithms
        algorithms = [
            'linear regression', 
            'random forest', 
            'SVM', 
            'KNN', 
            # 'moving average', 
            # 'exponential smoothing'
        ]
        algorithm_mapping = {
            'linear regression': LinearRegression,
            'random forest': RandomForestRegressor,
            'SVM': SVR,
            'KNN': KNeighborsRegressor
        }

        # run all predictions
        predictions = {}

        for algorithm in algorithms:
            if algorithm in algorithm_mapping:
                options['algorithm'] = algorithm_mapping[algorithm]
                predictions[algorithm] = self.predictUsingAlgorithm(df, options)

            else:
                print('Invalid algorithm:', algorithm)
        
        return predictions
    
    def runPrediction(self, df: pd.DataFrame, options: dict):
        """
        This function takes in a dataframe and runs a single prediction.
        """

        # acceptable algorithms
        algorithms = [
            'linear regression', 
            'random forest', 
            'SVM', 
            'KNN', 
            # 'moving average', 
            # 'exponential smoothing'
        ]
        algorithm_mapping = {
            'linear regression': sk.linear_model.LinearRegression,
            'random forest': sk.ensemble.RandomForestRegressor,
            'SVM': sk.svm.SVR,
            'KNN': sk.neighbors.KNeighborsRegressor
        }

        # run single prediction
        prediction = {}

        algorithm = options['algorithm']

        if algorithm in algorithm_mapping:
            options['algorithm'] = algorithm_mapping[algorithm]
            prediction[algorithm] = self.predictUsingAlgorithm(df, options)
        else:
            print('Invalid algorithm')
        
        return prediction