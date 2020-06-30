# coding: utf-8

# import modules
import math
import time

# additional code
import Variables
import Utilities
import Train


def ShowRailroad(ClearTheConsole = True):
    """
        This function draws the railroad on the screen
    """

    if ClearTheConsole:
        Utilities.ClearConsole()

    # draw railroad
    # print(f"\nVoie ferrée {len(Railroad)}\n{''.join(Railroad)}\n")
    print(f"\nVoie ferrée {len(Variables.Railroad)}\n")
    print(''.join(Variables.Railroad))
    print()


def AskUserAction():
    """
        This function ask for a serie of instructions for the train
    """

    TrainInstructions = ""

    while TrainInstructions == "":
        # ask instructions until input is not empty
        TrainInstructions = input("\nVeuillez entrer les instructions pour le train : ").strip().upper()

    # by default, instruction has 1 occurence
    InstructionOccurences = 1

    # get a list of instructions (separated by spaces)
    InstructionList = TrainInstructions.split(" ")
    # for each instruction in list
    for Instruction in InstructionList:
        ActionIsValid = False
        # check if instruction is valid (exists in PossibleTrainActions)
        for TrainAction in Variables.PossibleTrainActions:
            
            InstructionCode = Instruction[:1]
            if InstructionCode == TrainAction[0]:
                # instruction is valid
                ActionIsValid = True
                if TrainAction[1] == True:
                    # instruction can have a number of occurences
                    if len(Instruction) > 1:
                        # if there is a specified number of occurences, extract it, else keep default value
                        InstructionOccurences = int(Instruction[1:])
                # stop browsing possible actions
                break
            
        # resolve action
        ManageTrainAction(InstructionCode, InstructionOccurences)
        # reset default value for instruction occurences
        InstructionOccurences = 1

        if not ActionIsValid:
            print(f"{Instruction} n'est pas une instruction connue.")



def ManageTrainAction(CurrentAction, ActionOccurences = 1):
    """
        This function manages the possible train actions

        Parameters :
            CurrentAction : the current action
    """

    if CurrentAction == "A":
        # train forward
        for Movement in range(0, ActionOccurences):
            if Variables.TrainPosition < len(Variables.Railroad):
                # move train
                Variables.TrainPosition += 1
                # place on railroad
                PlaceTrainOnRailroad()
                # show message and train
                print(Variables.PossibleTrainActions[0][2])
                Train.ShowRailroad()
            else:
                # show message
                print(Variables.PossibleTrainActions[0][3])
            # make a pause between 2 movements
            time.sleep(Variables.TrainSpeed)

    elif CurrentAction == "R":
        # train backward
        for Movement in range(0, ActionOccurences):
            if Variables.TrainPosition > 0:
                # move train
                Variables.TrainPosition -= 1
                # place on railroad
                PlaceTrainOnRailroad()
                # show message and train
                print(Variables.PossibleTrainActions[1][2])
                Train.ShowRailroad()
            else:
                # show message
                print(Variables.PossibleTrainActions[1][3])
            # make a pause between 2 movements
            time.sleep(Variables.TrainSpeed)

    elif CurrentAction == "C":
        # try to load crates
        if Variables.SymbolUnderTrain.isdigit():
            # there are crates at this position
            # load minimum between number of crates and max and actual train payload
            LoadedCrates = math.min(Variables.TrainMaxLoad - Variables.TrainCurrentLoad, int(Variables.SymbolUnderTrain))
            # add crates to train
            Variables.TrainCurrentLoad += LoadedCrates
            # remove crates from railroad
            if int(Variables.SymbolUnderTrain) - LoadedCrates == 0:
                # no more crates here
                Variables.Railroad[Variables.TrainPosition] = Variables.RailroadSymbol
            else:
                # still some crates here
                Variables.Railroad[Variables.TrainPosition] = str(int(Variables.SymbolUnderTrain) - LoadedCrates)
            # show message
            print(Variables.PossibleTrainActions[2][2])
        else:
            # there are no crates here
            # show message            
            print(Variables.PossibleTrainActions[2][3])



def PlaceTrainOnRailroad():
    """
        This function places the train on the railroad
        and saves the content of the railroad at its position
    """
    if not Variables.TrainPreviousPosition == None:
        # put old symbol in place at previous train position
        Variables.Railroad[Variables.TrainPreviousPosition] = Variables.SymbolUnderTrain

    # save railroad content
    Variables.SymbolUnderTrain = Variables.Railroad[Variables.TrainPosition]
    # place train
    Variables.Railroad[Variables.TrainPosition] = Variables.TrainSymbol
    # save previous train position
    Variables.TrainPreviousPosition = Variables.TrainPosition
