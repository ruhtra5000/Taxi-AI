from enum import Enum
import random

class ActionType(Enum):
    RANDOM = 1
    CONSCIOUS = 2

# Class responsible for policy E-Greddy
class EGreedy:
    def __init__(self):
        # Decrease randomRate if you want more conscious actions 
        # (useful if you have a Q-table from a csv file)
        self.randomRate = 0.0 # (minimum: 0.0)
        self.lowerRate = 0.99996

    # Defines exploration and exploitation actions
    def setActionType(self):
        randFloat = random.random() # 0 < n < 1
        actType = None

        if randFloat < self.randomRate:
            actType = ActionType.RANDOM
        else:
            actType = ActionType.CONSCIOUS
        
        self.randomRate *= self.lowerRate 
        return actType
