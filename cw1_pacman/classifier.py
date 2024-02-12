# classifier.py
# Lin Li/26-dec-2021
#
# Use the skeleton below for the classifier and insert your code here.

import numpy as np

class Classifier:
    def __init__(self):
        self.total = 0
        self.moves_freq = {0 : 0,
                      1: 0,
                      2: 0,
                      3: 0}
        self.moves_prob = {0: 0.0,
                           1: 0.0,
                           2: 0.0,
                           3: 0.0}
        self.walls = {}
        self.food = {}
        self.p1 = {}
        self.p2 = {}
        self.infront = {}
        

    def reset(self):
        pass
    
    def fit(self, data, target):
        self.total = len(data)
        for t in target:
            if t == 0:
                self.moves_freq[0] += 1
            elif t == 1:
                self.moves_freq[1] += 1
            elif t == 2:
                self.moves_freq[2] += 1
            elif t == 3:
                self.moves_freq[3] += 1   
                 
        for x in self.moves_freq:
            self.moves_prob[x] = self.moves_freq[x] / self.total
            
        for d in data:
            
            
        

    def predict(self, data, legal=None): 
        return 1

