import gymnasium as gym
from QTable import QTable

#Creating environment Taxi-V3 and variables
env = gym.make("Taxi-v3", render_mode = 'human')

qtable = QTable()

numEpisodes = 50
stepsPerEpisode = 200

curState = None # Holds the current state

for episode in range(numEpisodes):
    curState = env.reset()[0]

    for step in range(stepsPerEpisode):
        action = env.action_space.sample()

        print(f'Ep: {episode} | Step: {step} | Action: {action}')

        newState, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            break

        curState = newState

env.close()