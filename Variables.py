# coding: utf-8

# Define global variables

GameInProgress = True

RailroadSymbol = ("rails", "=")
RailroadLength = 0
Railroad = []
SymbolUnderTrain = ""
InstructionNumber = 0
InstructionsHistory = []

GarageSymbol = ("garage", "H")
GaragePosition = 0

WarehouseSymbol = ("entrepôt", "T")
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

CrateSymbol = ("{NbCrates} marchandise(s)", "")
CrateBatchNumber = 0
NumberOfCratesToLoad = 0
NumberOfCratesDelivered = 0

EnergyPodSymbol = ("station d'énergie", "*")
EnergyPodNumber = 0
EnergyConsumptionByMovement = 3
EnergyConsumptionByMovementByLoadedCrate = 0.5
EnergyConsumptionByCrate = 0

PossibleTrainActions = [
    ["A", True, "Le petit train avance", "Le petit train ne peut pas aller plus loin"],
    ["R", True, "Le petit train recule", "Le petit train ne peut pas aller plus loin"],
    ["C", False, "Le petit train charge {NumberOfCrates} caisses", "Il n'y a aucune caisse à charger ici"],
    ["D", False, "Le petit train décharge {NumberOfCrates} caisses", "Il faut se trouver sur l'entrepôt pour pouvoir décharger"],
    ["E", False, "Le petit train récupère {EnergyQuantity} d'énergie", "Il faut se trouver sur une station d'énergie pour pouvoir recharger"],
    ["Q", False, "Vous abandonnez la mission", ""]
]
