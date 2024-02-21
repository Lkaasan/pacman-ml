# classifier.py
# This classifier is a ensemble of two classifiers, a Naive Bayes Classifier that I implemented myself, and a Decision Tree Classifier that I imported from scikit-learn.

# Imports
from sklearn.tree import DecisionTreeClassifier
import numpy as np

class Classifier:

    # Constructor for the Classifier Class, sets up class variables
    def __init__(self):
        #total number of data 
        self.total = 0
        
        # Dictionary that stores the frequency of moves from data
        self.moves_freq = {0 : 0,
                      1: 0,
                      2: 0,
                      3: 0}
        
        # Dictionary that stores the probability that each move occurs
        self.moves_prob = {0: 0.0,
                           1: 0.0,
                           2: 0.0,
                           3: 0.0}
        
        # Dictionaries for classes, storing a frequency table for the moves 
        self.walls = {}
        self.food = {}
        self.g1 = {}
        self.g2 = {}
        self.infront = {}
        
        # Storing all the data
        self.data = None
        
        # Stores all the target
        self.target = None
        
        # Creates a decision tree classifier
        self.clf = DecisionTreeClassifier()
        
    # Function that resets self when pacman dies
    def reset(self):
        self = None
    
    # Function that fits the input data
    # @param data, a  lsit of feature vector
    # @param target, a lsit of targets
    def fit(self, data, target):
        # Sets the total num of data
        self.total = len(data)
        
        # Calculates the frequency of each move from input data
        for t in target:
            self.moves_freq[t] += 1
                    
        # Calculate the probability of each move
        for x in self.moves_freq:
            self.moves_prob[x] = self.moves_freq[x] / self.total
                     
        counter = 0
            
        # Goes through all data, seperating it into classes, and storing 
        for d in data:
            
            # Separating data into classes
            first = tuple(d[0:4])
            second = tuple(d[4:8])
            third = tuple(d[8:16])
            fourth = tuple(d[16:24])
            fifth = d[24]
            
            # Checks if first 4 ints are in the walls dictionary
            if first not in self.walls:
                #Sets all moves to 1 for laplace smoothing (avoid division by 0)
                self.walls[first] = [1, 1, 1, 1]
            # Increment appropriate move
            self.walls[first][target[counter]] += 1
            
            # Checks if next 4 ints are in the food dictionary
            if second not in self.food:
                self.food[second] = [1, 1, 1, 1]
            self.food[second][target[counter]] += 1
                
            # Checks if next 8 ints are in g1 (ghost1) dictionary
            if third not in self.g1:
                self.g1[third] = [1, 1, 1, 1]
            self.g1[third][target[counter]] += 1
            
            # Checks if next 8 ints are in g2 (ghost2) dictionary
            if fourth not in self.g2:
                self.g2[fourth] = [1, 1, 1, 1]
            self.g2[fourth][target[counter]] += 1    
                
            # Checks if last bit is in infront dictionary
            if fifth not in self.infront:
                self.infront[fifth] = [1, 1, 1, 1]
            self.infront[fifth][target[counter]] += 1
            
            # Increment counter
            counter += 1
        
        # Sets self.data and self.target, and fits it to clf
        self.data = data
        self.target = target
        self.clf.fit(data, target)     

    # Function that creates a predicton for the move to make
    # @param data, a feature vector for current environment of pacman\
    # @return, move as integer
    def predict(self, data, legal=None): 
        
        # Separates the input featureVector into appropriate catagories
        first = tuple(data[0:4])
        second = tuple(data[4:8])
        third = tuple(data[8:16])
        fourth = tuple(data[16:24])
        fifth = data[24]
            
        # Sets highest prob and move of highest prob
        highest = 0
        move = -1
        
        # Loops though all moves, calculates naive bayes formula 
        for i in range (0, 4):
            # Sets prob to the probability of that move
            prob = self.moves_prob.get(i)
            
            # Checks if first is in the dictionary, ignores class if not
            if first in self.walls:
                # Gets appropraite data for naive bayes calculation
                value = self.walls[first][i]
                total = 0
                for x in self.walls:
                    total += self.walls.get(x)[i]
                # Multiplies prob by P(first|move)
                prob = prob * (value / total)
                
            # Checks if second is in the dictionary, ignores class if not
            if second in self.food:
                # Gets appropriate data for naive bayes calculation
                value = self.food[second][i]
                total = 0
                for x in self.food:
                    total += self.food.get(x)[i]
                # Multiplies prob by P(second|move)
                prob = prob * (value / total)
                
            # Checks if third is in the dictionary, ignores class if not 
            if third in self.g1:
                # Gets appropriate data for naive bayes calculation
                value = self.g1[third][i]
                total = 0
                for x in self.g1:
                    total += self.g1.get(x)[i]
                # Multiplies prob by P(third|move)
                prob = prob * (value / total)
                
            # Checks if fourth is in the dictionary, ignores class if not 
            if fourth in self.g2:
                # Gets appropriate data for naive bayes calculation
                value = self.g2[fourth][i]
                total = 0
                for x in self.g2:
                    total += self.g2.get(x)[i]
                # Multiplies prob by P(fourth|move)
                prob = prob * (value / total)
                
            # Checks if fifth is in the dictionary, ignores class if not
            if fifth in self.infront:
                # Gets appropriate data for naive bayes calculation
                value = self.infront[fifth][i]
                total = 0
                for x in self.infront:
                    total += self.infront.get(x)[i]
                # Multiples prob by P(fifth|move)
                prob = prob * (value / total)
            #stores current move if prob > highest
            if prob > highest:
                highest = prob
                move = i
        
        # Gets Decision Tree prediction
        prediction = self.clf.predict([data])
        
        # If naive bayes prediction and Decision tree prediction are different, returns one of them at random
        if move != prediction:
            r = np.random.rand()
            if r <= 0.5:
                return move
            else:
                return prediction
        # If they are the same, return move
        else:   
            return move