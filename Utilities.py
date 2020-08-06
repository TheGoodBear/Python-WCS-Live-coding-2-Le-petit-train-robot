# coding: utf-8

# import modules
import random
import os
import sys

# additional code
import Variables


def GetData(Message, MinimumValue = 0, MaximumValue = 0, DefaultValue = None):
    """
        This function gets an entry from the user
        Entry must be integer

        Parameters :
            Message : the message to show to the user
            MinimumValue : the minimum acceptable value 
            MaximumValue : the maximum acceptable value 
            DefaultValue : 
                - if None : there is no default value
                - if positive gets the default value
                - if -1 draw a random number between MinimumValue and MaximumValue
    """
    DataOK = False

    # Do until user entry is valid
    while not DataOK:
        MyData = input(Message)
        if not MyData.isdigit() or int(MyData) < MinimumValue or int(MyData) > MaximumValue:
            # user entry is not an expected value
            if DefaultValue == None:
                # no default value specified, so ask again
                print(f"Merci de rentrer une valeur comprise entre {MinimumValue} et {MaximumValue}")
            elif DefaultValue != -1 :
                # get specified default value
                MyData = DefaultValue
                DataOK = True
            else:
                # draw an random number between Min and Max
                MyData = random.randint(MinimumValue, MaximumValue)
                DataOK = True
        else:
            # user entry is valid
            DataOK = True

    # return user entry
    return int(MyData)


def ClearConsole():
    """
        This function clears the console depending on OS
    """

    if "win" in sys.platform.lower():
        # for windows
        os.system("cls")
    elif "linux" in sys.platform.lower():
        # for linux
        os.system("clear")


def ManageTrainMessage(Message):
    """
        This function shows a message for the train action
        and save it to action history
        
        Parameters :
            Message : the message to show
    """

    print(Message)
    Variables.InstructionNumber += 1
    # add new instruction to history
    Variables.InstructionsHistory.append("(" + str(Variables.InstructionNumber) + ") " + Message)      


def GetSymbolName(Symbol):
    """
        This function retrieve the name matching the symbol
    """
    ReturnValue = ""

    # check for each possible symbol
    # should be done in a better way (dictionary ?)
    if Symbol == Variables.RailroadSymbol[1]:
        ReturnValue = Variables.RailroadSymbol[0]
    elif Symbol == Variables.GarageSymbol[1]:
        ReturnValue = Variables.GarageSymbol[0]
    elif Symbol == Variables.WarehouseSymbol[1]:
        ReturnValue = Variables.WarehouseSymbol[0]
    elif Symbol.isdigit():
        ReturnValue = Variables.CrateSymbol[0].replace("{NbCrates}", Symbol)
    elif Symbol == Variables.EnergyPodSymbol[1]:
        ReturnValue = Variables.EnergyPodSymbol[0]

    return ReturnValue


# file main entry (for example to check the functions)
if __name__ == "__main__":
    ClearConsole()
    print("Bonjour")
