import numpy as np

#                   c1  c2  c3  p pub fb   s
TransitionMatrix = np.matrix([[0, 0.5, 0, 0, 0, 0,5, 0],
                    [0, 0, 0.8, 0, 0, 0, 0.2],
                    [0, 0, 0, 0.6, 0.4, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1],
                    [0.2, 0.4, 0.4, 0, 0, 0, 0],
                    [0.1, 0, 0, 0, 0, 0.9, 0],
                    [0, 0, 0, 0, 0, 0, 1]])

gamma = 1
#bellman equation
# v=R+rPssv
# (I-rPss)v = R
# v= (I-rPss)^(-1)R

Reward = np.matrix([-2, -2, -2, 10, -1, -1, 0]).transpose()

V = np.dot( (TransitionMatrix*gamma).I, Reward)
