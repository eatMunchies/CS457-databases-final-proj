"""
Anthony Silva
CS 457
Final Project
11/18/24
File: StatisticsCalculator.py
Description: This file contains the StatisticsCalculator class 
"""

import pandas as pd
import numpy as np

class StatisticsCalculator:

    sessionStatistics = 0

    def __init__(self):
        pass

    def calculateMean(self, df: pd.DataFrame, options: dict):
        """
        This function takes in a dataframe and calculates the mean.
        """
        
        column = options['column']
        range = options['numeric_range']
        mean = 0

        if range:
            mean = np.mean(df[column].iloc[range[0]:range[1]])
        else:
            mean = np.mean(df[column])
        
        self.sessionStatistics += 1
        
        return mean

    def calculateMedian(self, df: pd.DataFrame, options: dict):
        """
        This function takes in a dataframe and calculates the median.
        """
        
        column = options['column']
        range = options['numeric_range']
        median = 0

        if range:
            median = np.median(df[column].iloc[range[0]:range[1]])
        else:
            median = np.median(df[column])

        self.sessionStatistics += 1
        
        return median

    def calculateMode(self, df: pd.DataFrame, options: dict):
        """
        This function takes in a dataframe and calculates the mode.
        """
        
        column = options['column']
        mode = 0

        mode = df[column].mode()

        self.sessionStatistics += 1
        
        return mode

    def calculateVariance(self, df: pd.DataFrame, options: dict):
        """
        This function takes in a dataframe and calculates the variance.
        """
        
        column = options['column']
        range = options['numeric_range']
        variance = 0

        if range:
            variance = np.var(df[column].iloc[range[0]:range[1]])
        else:
            variance = np.var(df[column])
        
        self.sessionStatistics += 1
        
        return variance

    def calculateStandardDeviation(self, df: pd.DataFrame, options: dict):
        """
        This function takes in a dataframe and calculates the standard deviation.
        """
        
        column = options['column']
        range = options['numeric_range']
        stdDev = 0

        if range:
            stdDev = np.std(df[column].iloc[range[0]:range[1]])
        else:
            stdDev = np.std(df[column])
        
        self.sessionStatistics += 1
        
        return stdDev

    def calculateVolatility(self, df: pd.DataFrame, options: dict):
        """
        This function takes in a dataframe and calculates the volatility.
        """
        
        column = options['column']
        range = options['numeric_range']
        volatility = 0

        if range:
            volatility = np.std(df[column].pct_change().iloc[range[0]:range[1]])
        else:
            volatility = np.std(df[column].pct_change())
        
        self.sessionStatistics += 1
        
        return volatility

    def calculateRollingAverage(self, df: pd.DataFrame, options: dict):
        """
        This function takes in a dataframe and calculates the rolling average.
        """
        
        column = options['column']
        window = options['window']
        rollingAverage = 0

        rollingAverage = df[column].rolling(window=window).mean()

        self.sessionStatistics += 1
        
        return rollingAverage

    def getAllCalculations(self, df: pd.DataFrame, options: dict):
        """
        This function takes in a dataframe and calculates all statistics.
        """
        
        column = options['column']
        range = options['range']

        # need to convert range to indices
        if range:
            range = [df[df['date'] == range[0]].index[0], df[df['date'] == range[1]].index[0]]
        options['numeric_range'] = range

        window = options['window']

        calculations = {}

        calculations['mean'] = self.calculateMean(df, options)
        calculations['median'] = self.calculateMedian(df, options)
        calculations['mode'] = self.calculateMode(df, options)
        calculations['variance'] = self.calculateVariance(df, options)
        calculations['standard deviation'] = self.calculateStandardDeviation(df, options)
        calculations['volatility'] = self.calculateVolatility(df, options)
        # calculations['rolling average'] = self.calculateRollingAverage(df, options)
        # calculations['options'] = options

        return calculations