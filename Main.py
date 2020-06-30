# coding: utf-8

# import modules
import random

# additional code
import Utilities
import Initialization

# Define global variables
RailroadLength = 0
RailroadSymbol = "="
Railroad = []


def Main(Railroad, RailroadLength):
    """
        Main function
    """

    Initialization.ShowTitleAndRules()
    Railroad = GameInitialization(Railroad, RailroadLength)
    ShowRailroad(Railroad)


    return RailroadLength



def GameInitialization(Railroad, RailroadLength):
    """
        This function gets initial data from user
    """
    print()
    
    RailroadLength = Utilities.GetData(
        "Quelle est la longueur de la voie ferrée (entre 50 et 100): ",
        50,
        100,
        -1)
    Railroad = [RailroadSymbol] * RailroadLength

    return Railroad


def ShowRailroad(Railroad):
    """
        This function draws the railroad on the screen
    """

    # print(f"\nVoie ferrée {len(Railroad)}\n{''.join(Railroad)}\n")
    print(f"\nVoie ferrée {len(Railroad)}\n")
    print(''.join(Railroad))
    print()




# Program main entry
if __name__ == "__main__":

    Main(Railroad, RailroadLength)
