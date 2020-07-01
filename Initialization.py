# coding: utf-8

# import modules
import random

# additional code
import Variables
import Utilities
import Train


def ShowTitleAndRules(ClearTheConsole = True):
    """
        This function prints game title and rules
        after cleaning the screen (if specified)
    """

    if ClearTheConsole:
        Utilities.ClearConsole()

    print("Le petit train robot")
    print("--------------------")
    print()
    print("L'objectif du jeu est, en un minimum d'instructions, de programmer un train pour :")
    print("    - qu'il charge toutes les marchandise")
    print("    - qu'il les décharge à l'entrepôt")
    print("    - qu'il revienne à son garage")
    print()
    print("Règles particulières :")
    print("    - lorsque les objectifs ci-dessus sont remplis, la partie est gagnée")
    print("    - si le train tombe en panne d'énergie, la partie est perdue")
    print("    - les instructions doivent être séparées par un espace")
    print()
    print("Instructions comprises par le train :")
    print("    - (A)vancer de n cases (par exemple A5)")
    print("    - (R)eculer de n cases (par exemple R12)")
    print("    - (C)harger des marchandises (seulement sur un emplacement de marchandises et à concurrence de la capacité de charge maximum)")
    print("    - (D)écharger les marchandises (seulement à l'entrepôt)")
    print("    - Recharger en (E)nergie (seulement sur une station de charge, et remet la charge au niveau maximum)")
    print("    - (Q)uitter le jeu (et échouer)")


def GameInitialization():
    """
        This function gets initial data from user
    """

    print()
    
    # Define railroad
    Variables.RailroadLength = Utilities.GetData(
        "Quelle est la longueur de la voie ferrée (entre 50 et 100): ",
        50,
        100,
        -1)
    Variables.Railroad = [Variables.RailroadSymbol[1]] * Variables.RailroadLength

    # Add buildings
    Variables.Railroad[Variables.GaragePosition] = Variables.GarageSymbol[1]
    Variables.WarehousePosition = Variables.RailroadLength - 1
    Variables.Railroad[Variables.WarehousePosition] = Variables.WarehouseSymbol[1]

    # Place crates
    Variables.CrateBatchNumber = Utilities.GetData(
        "Combien de lots de caisses doit-on placer sur la voie (entre 3 et 10): ",
        3,
        10,
        -1)
    for BatchNumber in range(0, Variables.CrateBatchNumber):
        NumberOfCratesInBatch = random.randint(1, 9)
        Variables.NumberOfCratesToLoad += NumberOfCratesInBatch
        PlaceElementOnRailroad(str(NumberOfCratesInBatch))

    # Place energy pods
    Variables.EnergyPodNumber = Utilities.GetData(
        "Combien de stations d'énergie doit-on placer sur la voie (entre 1 et 5): ",
        1,
        5,
        -1)
    for PodNumber in range(0, Variables.EnergyPodNumber):
        PlaceElementOnRailroad(Variables.EnergyPodSymbol[1])

    # Ask for energy consumption
    Variables.EnergyConsumptionByMovement = Utilities.GetData(
        "Quelle quantité d'énergie consomme le train pour se déplacer à vide (entre 1 et 5): ",
        1,
        5,
        3)
    Variables.EnergyConsumptionByMovementByLoadedCrate = Utilities.GetData(
        "Quelle quantité additionnelle d'énergie consomme le train pour se déplacer pour chaque caisse chargée (entre 0 et 1): ",
        0,
        1,
        0.5)
    Variables.EnergyConsumptionByCrate = Utilities.GetData(
        "Quelle quantité d'énergie consomme le train pour (dé)charger une caisse (entre 1 et 5): ",
        1,
        5,
        1)

    # Add train
    Train.PlaceTrainOnRailroad()


def PlaceElementOnRailroad(Symbol):
    """
        This function places an element on the railroad if place is available
    """

    # draw random position
    ElementPosition = 0
    while Variables.Railroad[ElementPosition] != Variables.RailroadSymbol[1]:
        ElementPosition = random.randint(0, len(Variables.Railroad) - 1)

    # place element
    Variables.Railroad[ElementPosition] = Symbol


# if __name__ == "__main__":
#     ShowTitleAndRules()
