"""
Anthony Silva
CS 457
Final Project
11/18/24
File: FutureAnalyzer.py
Description: This file contains the FutureAnalyzer class 
"""

from back.Predictor import Predictor
from back.Visualizer import Visualizer
from back.StatisticsCalculator import StatisticsCalculator
from back.models import Gold, Silver, Copper, Platinum, Palladium, Predictions, Visualizations, Statistics
from back.models import session

from enum import Enum
import pandas as pd
from datetime import datetime

metals = Enum('metals', 'gold silver copper platinum palladium')

class FutureAnalyzer:
    
    def __init__(self):
        self.predictor = Predictor()
        self.visualizer = Visualizer()
        self.calculator = StatisticsCalculator()
        self.data = None
    
    def visualizeData(self, options : dict):
        """
        This function takes in a dataframe and visualizes the data.
        """
        self.dataLoader(options['metal'])
        self.visualizer.visualizeData(self.data, options)
        # self.saveVisualization(options)

    def produceStatistics(self, options : dict):
        """
        This function takes in a dataframe and produces statistics.
        """
        self.dataLoader(options['metal'])
        calculations = self.calculator.getAllCalculations(self.data, options)
        self.saveStatistic(calculations, options)
        return calculations

    def predictFuturedata(self, options : dict):
        """
        This function takes in a dataframe and predicts future data.
        """
        self.dataLoader(options['metal'])
        predictions = self.predictor.runPredictions(self.data, options)
        self.savePredictions(predictions, options)
        return predictions

    def dataLoader(self, data : metals):
        """
        This function loads data from sqlalchemy into a df
        """

        if data == metals.gold: # Gold
            result = session.query(Gold).all()
        elif data == metals.silver:
            result = session.query(Silver).all()
        elif data == metals.copper:
            result = session.query(Copper).all()
        elif data == metals.platinum:
            result = session.query(Platinum).all()
        elif data == metals.palladium:
            result = session.query(Palladium).all()
        else:
            print("Invalid metal")
            result = None
            return
        
        # convert to df
        df = pd.DataFrame([(r.date, r.open, r.close, r.high, r.low, r.volume) for r in result], columns=['date', 'open', 'close', 'high', 'low', 'volume'])

        df['date'] = pd.to_datetime(df['date'])
        df['date_ordinal'] = df['date'].apply(lambda x: x.toordinal())

        self.data = df
    
    def savePredictions(self, predictions : dict, options : dict):
        """
        This function saves the predictions to the database.
        """

        for algorithm, prediction in predictions.items():
            newPrediction = Predictions(
                metal=options['metal'].name,
                algorithm=algorithm,
                prediction=float(prediction[0]),
                predicted_date=options['date'],
                generated_at = datetime.now()
            )
            session.add(newPrediction)
        
        session.commit()
    
    def saveStatistic(self, statistic : dict, options : dict):
        """
        This function saves the statistics to the database.
        """

        print("statistic: ", statistic)

        for stat_type, value in statistic.items():
            newStatistic = Statistics(
                metal=options['metal'].name,
                stat_type=stat_type,
                value=float(value),
                # start_date=options['start_date'],
                # end_date=options['end_date'],
                generated_at = datetime.now(),
                column=options['column']
            )
            if options['range'] != None:
                # print(options['range'])
                newStatistic.start_date = options['range'][0]
                newStatistic.end_date = options['range'][1]
            else:
                newStatistic.start_date = 'N/A'
                newStatistic.end_date = 'N/A'
            session.add(newStatistic)

        session.commit()

    def saveVisualization(self, visualization : dict):
        """
        This function saves the visualizations to the database.
        """
        newVisualization = Visualizations(
            metal=visualization['metal'],
            visual_type=visualization['graphType'],
            parameters=visualization['parameters'],
            file_path=visualization['file_path'],
            generated_at=visualization['generated_at']
        )
        session.add(newVisualization)
        session.commit()
