"""
Anthony Silva 
CS 457
Final Project
11/18/24
File: menus.py
Description: This file contains the menu functions for the frontend of the project.
"""

from front.helpers import clean_menu_input
from back.FutureAnalyzer import FutureAnalyzer, metals

# from back.main import run_estimations

def statistics_menu(fa: FutureAnalyzer):
    print("\nStatistics Menu")
    print("1. Gold")
    print("2. Silver")
    print("3. Platinum")
    print("4. Palladium")
    print("5. Copper")
    print("6. Back")

    choice = input("Enter your choice: ")
    choice = clean_menu_input(choice, 6)
    if choice == 6:
        return 0
    
    choices = ['gold', 'silver', 'platinum', 'palladium', 'copper']

    # get date to predict
    date_0 = input("Enter the start date (YYYY-MM-DD): ")
    if len(date_0) != 10:
        print("Invalid date format")
        return 0
    
    date_1 = input("Enter the end date (YYYY-MM-DD): ")
    if len(date_1) != 10:
        print("Invalid date format")
        return 0
    
    column = input("Enter the column to calculate statistics for (open, high, low, close, volume): ")
    if column.lower() not in ['open', 'high', 'low', 'close', 'volume']:
        print("Invalid column")
        return 0
    
    options = {
        'metal': metals[choices[choice - 1]],
        'column': column.lower(),
        'range': [date_0, date_1],
        'window': 20, # window for rolling statistics, good value is 20
    }

    results = fa.produceStatistics(options)

    print(f"Statistics for {column} for {choices[choice - 1]} from {date_0} to {date_1}:")
    for key, value in results.items():
        print(f"{key}: {value}")
    
    return 0

def predict_menu(fa: FutureAnalyzer):
    print("\nPredict Menu")
    print("1. Gold")
    print("2. Silver")
    print("3. Platinum")
    print("4. Palladium")
    print("5. Copper")
    print("6. Back")

    choice = input("Enter your choice: ")
    choice = clean_menu_input(choice, 6)
    if choice == 6:
        return 0

    choices = ['gold', 'silver', 'platinum', 'palladium', 'copper']

    # get date to predict
    date = input("Enter the date to predict (YYYY-MM-DD): ")
    if len(date) != 10:
        print("Invalid date format")
        return 0

    column = input("Enter the column to predict (open, high, low, close, volume): ")
    if column.lower() not in ['open', 'high', 'low', 'close', 'volume']:
        print("Invalid column")
        return 0
    

    # run the models and print the results
    options = {
        # 'metal': choices[choice - 1], #need to use the metals enum and match the str value
        'metal': metals[choices[choice - 1]],
        'date': date,
        'algorithm': None,
        'column': column.lower()
    }

    results = fa.predictFuturedata(options)

    print(f"Predicted {column} for {choices[choice - 1]} on {date}:")

    for key, value in results.items():
        print(f"{key}: {value[0].round(2)}")

    return 0

    # results = run_estimations(choices[choice - 1], date)


def visualize_menu(fa: FutureAnalyzer):
    print("\nVisualize Menu")
    print("1. Gold")
    print("2. Silver")
    print("3. Platinum")
    print("4. Palladium")
    print("5. Copper")
    print("6. Back")

    choice = input("Enter your choice: ")
    choice = clean_menu_input(choice, 6)
    if choice == 6:
        return 0
    
    choices = ['gold', 'silver', 'platinum', 'palladium', 'copper']
    
    column = input("Enter the column to visualize (open, high, low, close, volume): ")
    if column.lower() not in ['open', 'high', 'low', 'close', 'volume']:
        print("Invalid column")
        return 0
    
    graph_type = input("Enter the graph type (line, scatter, bar, hist, box): ")
    if graph_type.lower() not in ['line', 'scatter', 'bar', 'hist', 'box']:
        print("Invalid graph type")
        return 0
    
    y = column
    x = 'date'

    xlabel = 'Date'
    ylabel = column.capitalize()

    color = 'blue'
    
    options = {
        'metal': metals[choices[choice - 1]],
        'graphType': graph_type.lower(),
        'x': x,
        'y': y,
        'xlabel': xlabel,
        'ylabel': ylabel,
        'color': color,
        'title': f"{choices[choice - 1].capitalize()} {column.capitalize()} {graph_type.capitalize()} Graph",
    }

    ax = fa.visualizeData(options)

    return 0

def quit_menu(fa: FutureAnalyzer):
    print("\nAre you sure you want to quit?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")
    choice = clean_menu_input(choice, 2)
    if choice == 1:
        return 8989
    else:
        return 0

def main_menu(fa: FutureAnalyzer):
    print("\nMain Menu")
    print("1. Statistics")
    print("2. Predict")
    print("3. Visualize")
    print("4. Exit")
    choice = input("Enter your choice: ")
    choice = clean_menu_input(choice, 4)
    return choice
