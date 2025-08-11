import gymnasium as gym
from QTable import QTable
from EGreedy import EGreedy, ActionType

# Creating environment Taxi-V3 and variables
env = gym.make("Taxi-v3", render_mode = "human") # "human" or None

qtable = QTable()
egreedy = EGreedy()

# Uncomment if you want to use a previous Q-table (csv file)
#qtable.readQTable()

numEpisodes = 1000
stepsPerEpisode = 200

curState = None # Holds the current state

# "Main" 
for episode in range(numEpisodes):
    curState = env.reset()[0]

    for step in range(stepsPerEpisode):
        action = None

        # Decides between random or conscious action
        if egreedy.setActionType() == ActionType.RANDOM:
            action = env.action_space.sample()
        else:
            action = qtable.getBestAction(curState)

        # Applies an action to the environment
        newState, reward, terminated, truncated, info = env.step(action)
        
        # Updates Q-Value
        qtable.setQValue(curState, newState, action, reward)

        if terminated or truncated:
            break

        curState = newState
        
        # Print for monitoring
        print(f'Ep: {episode + 1} | Step: {step + 1} | Action: {action} | Reward: {reward}')

    # Every 5 episodes save the Q-table
    if (episode+1) % 5 == 0:
        qtable.saveQTable()
        print('\n\nQ-Table saved at: qtable.csv\n\n')
    
env.close()