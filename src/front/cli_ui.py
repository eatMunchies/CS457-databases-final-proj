"""
Anthony Silva
CS 457
Final Project
11/18/24
File: cli_ui.py
Description: This file is the main file for the frontend of the project. It will
"""

# imports 
import sys
import os
from front.helpers import print_welcome_message
from front.menus import main_menu, statistics_menu, predict_menu, visualize_menu, quit_menu
from back.FutureAnalyzer import FutureAnalyzer
import warnings

warnings.filterwarnings("ignore")

# main class

class UI:

    def __init__(self):
        self.fa = FutureAnalyzer()

    def main(self):
        print_welcome_message()

        menus = [main_menu, statistics_menu, predict_menu, visualize_menu, quit_menu]
        choice = 0

        while True:
            choice = menus[choice](self.fa)
            if choice == 8989:
                break
