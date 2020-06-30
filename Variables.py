# coding: utf-8

# Define global variables

GameInProgress = True

RailroadSymbol = "="
RailroadLength = 0
Railroad = []
SymbolUnderTrain = ""

GarageSymbol = "H"
GaragePosition = 0

WarehouseSymbol = "T"
WarehousePosition = 0

TrainSymbol = "X"
TrainPreviousPosition = None
TrainPosition = 0
TrainMaxEnergy = 100
TrainCurrentEnergy = TrainMaxEnergy
TrainMaxLoad = 20
TrainCurrentLoad = 0
TrainSpeed = 0.1

TrainMovements = 0
TrainActions = 0

CrateBatchNumber = 0


PossibleTrainActions = [
    ["A", True, "Le petit train avance", "Le petit train ne peut pas aller plus loin"],
    ["R", True, "Le petit train recule", "Le petit train ne peut pas aller plus loin"],
    ["C", False, "Le petit train charge {NumberOfCrates} caisses", "Il n'y a aucune caisse à charger ici"],
    ["D", False, "Le petit train décharge {NumberOfCrates} caisses", "Il faut se trouver sur l'entrepôt pour pouvoir décharger"],
    ["E", False, "Le petit train récupère {EnergyQuantity} d'énergie", "Il faut se trouver sur une station d'énergie pour pouvoir recharger"]
]

# RailroadData = [
#     ["Voie ferrée", "=", None],
#     ["Garage", "H", 0],
#     ["Entrepôt", "T", None],
#     ["Train", "X", 0]
# ]