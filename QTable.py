
#Class that encapsulates a table with quality values

class QTable:  
    def __init__(self):
        self.obs = 500 # Possible states
        self.act = 6 # Possible actions
        self.learnRate = 0.1
        self.lossRate = 0.9
        self.qtable = [[0 for col in range(self.act)] for row in range(self.obs)]
        #Access: self.qtable[state][action]

    
        
    