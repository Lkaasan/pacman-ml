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
            self.moves_freq[t] += 1
                    
        for x in self.moves_freq:
            self.moves_prob[x] = self.moves_freq[x] / self.total
                
        counter = 0
            
        for d in data:
            first = tuple(d[0:4])
            second = tuple(d[4:8])
            third = tuple(d[8:16])
            fourth = tuple(d[16:24])
            fifth = d[24]
            
            if first not in self.walls:
                self.walls[first] = [0, 0, 0, 0]
            self.walls[first][target[counter]] += 1
                    
            if second not in self.food:
                self.food[second] = [0, 0, 0, 0]
            self.food[second][target[counter]] += 1
                
            if third not in self.p1:
                self.p1[third] = [0, 0, 0, 0]
            self.p1[third][target[counter]] += 1
                    
            if fourth not in self.p2:
                self.p2[fourth] = [0, 0, 0, 0]
            self.p2[fourth][target[counter]] += 1    
                
            if fifth not in self.infront:
                self.infront[fifth] = [0, 0, 0, 0]
            self.infront[fifth][target[counter]] += 1
                
            counter += 1

        for x in self.food:
            print(self.food[x])

            

    def predict(self, data, legal=None): 
        first = tuple(data[0:4])
        second = tuple(data[4:8])
        third = tuple(data[8:16])
        fourth = tuple(data[16:24])
        fifth = data[24]
        
        check_array = [True, True, True, True, True]
        
        if first not in self.walls:
            check_array[0] = False
        if second not in self.food:
            check_array[1] = False
        if third not in self.p1:
            check_array[2] = False
        if fourth not in self.p2:
            check_array[3] = False
        if fifth not in self.infront:
            check_array[4] = False
            
        highest = 0
        index = -1
        
        # print(self.food)
        
        for i in range (0, 3):
            prob = self.moves_prob.get(i)
            if check_array[0] is not False:
                
                    
                
            
                
            
        # print(first_check, second_check, third_check, fourth_check, fifth_check)
        
        

