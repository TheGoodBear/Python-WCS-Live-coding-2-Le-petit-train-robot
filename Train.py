# coding: utf-8

# import modules
import time

# additional code
import Variables
import Initialization
import Utilities
import Train


def ShowRailroad(ClearTheConsole = True):
    """
        This function draws the railroad on the screen
    """

    # show title and rules
    Initialization.ShowTitleAndRules(ClearTheConsole)

    # show railroad data
    print("\nTableau de bord")
    print("---------------\n")
    print(f"Longueur de la voie ferrée : {len(Variables.Railroad)}")
    print(f"Nombre de stations d'énergie : {Variables.EnergyPodNumber}, énergie consommée par déplacement à vide ({Variables.EnergyConsumptionByMovement}) puis par caisse chargée ({Variables.EnergyConsumptionByMovementByLoadedCrate}), et par caisse (dé)chargée ({Variables.EnergyConsumptionByCrate})")
    print(f"Nombre de caisses : à charger ({Variables.NumberOfCratesToLoad}) - livrées ({Variables.NumberOfCratesDelivered})")
    print(f"Train - Position : {Variables.TrainPosition} (sur {Utilities.GetSymbolName(Variables.SymbolUnderTrain)} - {Variables.SymbolUnderTrain}) - Énergie : {Variables.TrainCurrentEnergy}/{Variables.TrainMaxEnergy} - Charge : {Variables.TrainCurrentLoad}/{Variables.TrainMaxLoad}")
    print(f"Activités du train : {Variables.TrainMovements} déplacements et {Variables.TrainActions} actions")
    print(f"Historique des 10 dernières actions : {', '.join(Variables.InstructionsHistory[:-11:-1])}")
    print()

    # draw railroad
    # print(f"\nVoie ferrée {len(Railroad)}\n{''.join(Railroad)}\n")
    print(''.join(Variables.Railroad))

    # check victory or defeat
    CheckVictoryOrDefeat()


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
            
            # get instruction code only (1st character) with a list slice
            InstructionCode = Instruction[:1]
            if InstructionCode == TrainAction[0]:
                # instruction is valid (in TrainAction list)
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
            if Variables.TrainPosition < len(Variables.Railroad) - 1:
                # move train and update counters
                Variables.TrainPosition += 1
                Variables.TrainCurrentEnergy -= (
                    Variables.EnergyConsumptionByMovement + (
                        Variables.EnergyConsumptionByMovementByLoadedCrate * 
                        Variables.TrainCurrentLoad))
                Variables.TrainMovements += 1
                # place on railroad
                PlaceTrainOnRailroad()
                # show message and train
                Utilities.ManageTrainMessage(Variables.PossibleTrainActions[0][2])
            else:
                # show message
                Utilities.ManageTrainMessage(Variables.PossibleTrainActions[0][3])
            # show train and make a pause between 2 movements
            Train.ShowRailroad()
            time.sleep(Variables.TrainSpeed)
            # if game already ended, go out of loop
            if not Variables.GameInProgress:
                break

    elif CurrentAction == "R":
        # train backward
        for Movement in range(0, ActionOccurences):
            if Variables.TrainPosition > 0:
                # move train and update counters
                Variables.TrainPosition -= 1
                Variables.TrainCurrentEnergy -= (
                    Variables.EnergyConsumptionByMovement + (
                        Variables.EnergyConsumptionByMovementByLoadedCrate * 
                        Variables.TrainCurrentLoad))
                Variables.TrainMovements += 1
                # place on railroad
                PlaceTrainOnRailroad()
                # show message and train
                Utilities.ManageTrainMessage(Variables.PossibleTrainActions[1][2])
            else:
                # show message
                Utilities.ManageTrainMessage(Variables.PossibleTrainActions[1][3])
            # show train and make a pause between 2 movements
            Train.ShowRailroad()
            time.sleep(Variables.TrainSpeed)
            # if game already ended, go out of loop
            if not Variables.GameInProgress:
                break

    elif CurrentAction == "C":
        # try to load crates
        if Variables.SymbolUnderTrain.isdigit():
            # there are crates at this position
            # load minimum between number of crates and max and actual train payload
            LoadedCrates = min(Variables.TrainMaxLoad - Variables.TrainCurrentLoad, int(Variables.SymbolUnderTrain))
            # add crates to train and update counters
            Variables.NumberOfCratesToLoad -= LoadedCrates
            Variables.TrainCurrentLoad += LoadedCrates
            Variables.TrainCurrentEnergy -= LoadedCrates * Variables.EnergyConsumptionByCrate
            Variables.TrainActions += 1
            # remove crates from railroad
            if int(Variables.SymbolUnderTrain) - LoadedCrates == 0:
                # no more crates here
                Variables.SymbolUnderTrain = Variables.RailroadSymbol[1]
            else:
                # still some crates here
                Variables.SymbolUnderTrain = str(int(Variables.SymbolUnderTrain) - LoadedCrates)
            # show message
            Utilities.ManageTrainMessage(Variables.PossibleTrainActions[2][2].replace("{NumberOfCrates}", str(LoadedCrates)))
        else:
            # there are no crates here
            # show message            
            Utilities.ManageTrainMessage(Variables.PossibleTrainActions[2][3])

    elif CurrentAction == "D":
        # try to unload crates
        if Variables.SymbolUnderTrain == Variables.WarehouseSymbol[1]:
            # we are on the warehouse
            # unload all crates and update counters
            UnloadedCrates = Variables.TrainCurrentLoad
            Variables.NumberOfCratesDelivered += UnloadedCrates
            Variables.TrainCurrentEnergy -= UnloadedCrates * Variables.EnergyConsumptionByCrate
            Variables.TrainCurrentLoad = 0
            Variables.TrainActions += 1
            # show message
            Utilities.ManageTrainMessage(Variables.PossibleTrainActions[3][2].replace("{NumberOfCrates}", str(UnloadedCrates)))
        else:
            # the train is not on the warehouse
            # show message            
            Utilities.ManageTrainMessage(Variables.PossibleTrainActions[3][3])

    elif CurrentAction == "E":
        # try to recharge train energy
        if Variables.SymbolUnderTrain == Variables.EnergyPodSymbol[1]:
            # we are on an energy pod
            # recharge energy
            EnergyRecharged = Variables.TrainMaxEnergy - Variables.TrainCurrentEnergy
            Variables.TrainCurrentEnergy += EnergyRecharged
            Variables.TrainActions += 1
            # show message
            Utilities.ManageTrainMessage(Variables.PossibleTrainActions[4][2].replace("{EnergyQuantity}", str(EnergyRecharged)))
        else:
            # there is no recharge pod here
            # show message            
            Utilities.ManageTrainMessage(Variables.PossibleTrainActions[4][3])

    elif CurrentAction == "Q":
        # quit game
        Utilities.ManageTrainMessage(Variables.PossibleTrainActions[5][2])
        Variables.GameInProgress = False

    # update user interface
    Train.ShowRailroad()


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


def CheckVictoryOrDefeat():
    """
        This function verifies if game ends
        either with a vistory or a defeat
    """

    # check victory
    if (Variables.SymbolUnderTrain == Variables.GarageSymbol[1]
        and Variables.NumberOfCratesToLoad == 0
        and Variables.TrainCurrentLoad == 0):
        print("\nBRAVO, vous avez rempli votre mission !\n")
        Variables.GameInProgress = False

    # check defeat
    elif Variables.TrainCurrentEnergy <= 0:
        print("\nLOUPÉ, le petit train est tombé en panne !\n")
        Variables.GameInProgress = False
