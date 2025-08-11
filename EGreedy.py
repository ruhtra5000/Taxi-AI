from enum import Enum
import random

class ActionType(Enum):
    RANDOM = 1
    CONSCIOUS = 2

# Class responsible for policy E-Greddy
class EGreedy:
    def __init__(self):
        self.randomRate = 1.0
        self.lowerRate = 0.995

    # Defines exploration and exploitation actions
    def setActionType(self):
        randFloat = random() # 0 < n < 1
        actType = None

        if randFloat < self.randomRate:
            actType = ActionType.RANDOM
        else:
            actType = ActionType.CONSCIOUS
        
        self.randomRate *= self.lowerRate 
        return actType
