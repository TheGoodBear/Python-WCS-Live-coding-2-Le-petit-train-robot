# coding: utf-8

# import modules
import random

# additional code
import Variables
import Initialization
import Train


def Main():
    """
        Main function
    """

    # Initialize game
    Initialization.ShowTitleAndRules()
    Initialization.GameInitialization()
    Train.ShowRailroad(False)

    # Main game loop
    while Variables.GameInProgress:
        Train.AskUserAction()



# Program main entry
if __name__ == "__main__":

    Main()
