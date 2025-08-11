
# Class that encapsulates a table with quality values
class QTable:  
    def __init__(self):
        self.obs = 500 # Possible states
        self.act = 6 # Possible actions
        self.learnRate = 0.1
        self.lossRate = 0.9
        self.qtable = [[0.0 for col in range(self.act)] for row in range(self.obs)] 
        # Access: self.qtable[state][action]

    # Updates Q-Value for the last action
    def setQValue(self, curState, newState, action, reward):
        errorValue = reward + (self.lossRate * max(self.qtable[newState])) - self.qtable[curState][action]
        self.qtable[curState][action] += self.learnRate * errorValue
    
    # Returns an action with max Q-Value
    def getBestAction(self, state):
        maxQValue = -10000000.0 # Q-Value itself
        maxQIndex = 0 # Action (Q-Value index)
        
        for i in range(self.act):
            if self.qtable[state][i] > maxQValue:
                maxQValue = self.qtable[state][i]
                maxQIndex = i
        print()
        return maxQIndex
    
    # Save QTable at a csv file
    def saveQTable(self):
        with open("qtable.csv", "w") as file:
            for line in self.qtable:
                for item in line:
                    file.write(f'{item} ; ')

                file.write('\n')
    
    # Read QTable from a csv file
    def readQTable(self):
        with open("qtable.csv", "r") as file:
            line = file.readline()
            for lineIndex in range(self.obs):
                sepLine = line.split(' ; ')
                for i in range(self.act):
                    self.qtable[lineIndex][i] = float(sepLine[i])
                
                line = file.readline()
        
        
    