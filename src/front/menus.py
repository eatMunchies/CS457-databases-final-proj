"""
Anthony Silva 
CS 457
Final Project
11/18/24
File: menus.py
Description: This file contains the menu functions for the frontend of the project.
"""

from front.helpers import clean_menu_input
# from back.main import run_estimations

def statistics_menu():
    pass

def predict_menu():
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

    # run the models and print the results
    # results = run_estimations(choices[choice - 1], date)


def visualize_menu():
    pass

def quit_menu():
    print("\nAre you sure you want to quit?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")
    choice = clean_menu_input(choice, 2)
    if choice == 1:
        return 8989
    else:
        return 0

def main_menu():
    print("\nMain Menu")
    print("1. Statistics")
    print("2. Predict")
    print("3. Visualize")
    print("4. Exit")
    choice = input("Enter your choice: ")
    choice = clean_menu_input(choice, 4)
    return choice
