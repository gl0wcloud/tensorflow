import gym
import random
import numpy as np
import os
# import tflearn as tf
# from tflearn.layers.core import input_data, dropout, fully_connected
# from tflearn.layers.estimator import regression
from statistics import mean, median
from collections import Counter

# os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
# os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
os.environ['DISPLAY'] = ':1'

LR = 1e-3                       # Learning rate
env = gym.make('CartPole-v0')
goal_steps = 500
initial_games = 10000

def random_games():
    for episode in range(5):
        env.reset()
        for t in range(goal_steps):
            env.render()
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            if done:
                break

random_games()

env.close()