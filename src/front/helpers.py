"""
Anthony Silva
CS 457
Final Project
11/18/24
File: helpers.py
Description: This file contains helper functions for the frontend of the project.
"""

def clean_menu_input(user_input : str, range : int) -> int:
    """
    cleans user menu input to an int in the menu range, returns -1 if invalid
    """

    try:
        user_input = int(user_input)
        if user_input < 1 or user_input > range:
            return -1
        return user_input
    except:
        return -1

def print_welcome_message():
    string = f"""\n\n\n
    ******************************************************************
    *                                                                *
    *                                                                *
    *                                                                *
    *    WELCOME TO THE PRECIOUS METALS DATABASE ANALYSIS SYSTEM!    *
    *                                                                *
    *                                                                *
    *                                                                *
    ******************************************************************
    """
    print(string)