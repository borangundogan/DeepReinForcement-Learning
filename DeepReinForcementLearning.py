import gym
import numpy as np
import random

env = gym.make("CartPole-v0")
states = env.observation_space.shape[0]
actions = env.action_space.n

episodes = 10
for _ in range(1, episodes + 1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = random.choice([0, 1])
        observation, reward, done, info = env.step(action)
        score += reward
    print("Episode: {}  Score: {}".format(_, score))   