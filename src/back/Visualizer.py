"""
Anthony Silva
CS 457
Final Project
11/18/24
File: Visualizer.py
Description: This file contains the Visualizer class 
"""

import matplotlib.pyplot as plt
import pandas as pd

class Visualizer:

    sessionVisualizations = 0

    def __init__(self):
        pass

    def visualizeData(self, df: pd.DataFrame, options: dict):
        """
        This function takes in a dataframe and visualizes the data.
        """
        
        graphType = options['graphType']
        x = options['x']
        y = options['y']
        title = options['title']
        xlabel = options['xlabel']
        ylabel = options['ylabel']
        color = options['color']

        if graphType == 'line':
            ax = df.plot(x=x, y=y, title=title, xlabel=xlabel, ylabel=ylabel, color=color)
            # plt.show()
        elif graphType == 'scatter':
            ax = df.plot.scatter(x=x, y=y, title=title, xlabel=xlabel, ylabel=ylabel, color=color)
            # plt.show()
        elif graphType == 'bar':
            ax = df.plot.bar(x=x, y=y, title=title, xlabel=xlabel, ylabel=ylabel, color=color)
            # plt.show()
        elif graphType == 'hist':
            ax = df.plot.hist(x=x, y=y, title=title, xlabel=xlabel, ylabel=ylabel, color=color)
            # plt.show()
        elif graphType == 'box':
            ax = df.plot.box(x=x, y=y, title=title, xlabel=xlabel, ylabel=ylabel, color=color)
            # plt.show()
        else:
            print('Invalid graph type')
            return
        
        self.sessionVisualizations += 1

        if 'outputPath' in options:
            plt.savefig(options['outputPath'] + options['title'] + '.png', bbox_inches='tight')
            print(f"Plot saved to {options['outputPath']}")

        plt.show()

        return ax