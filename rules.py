from expression import *
from functions import *

class Rule:
    def __init__(self, id, antecedent, consecuent):
        self.id = id
        self.antecedent = antecedent
        self.consecuent = consecuent
        
    def calculate_strength(self, inputs):
        return self.antecedent.evaluate(inputs)  

    def output_variable(self):
        return self.consecuent.variable

class MamdaniRule(Rule):
    def __repr__(self):
        return '{0}: IF {1} THEN {2}'.format(self.id, repr(self.antecedent), repr(self.consecuent))

class TSKRule(Rule):
    def __repr__(self):
        return '{0}: IF {1} THEN {2}'.format(self.id, repr(self.antecedent), self.consecuent)
    
    def output_variable(self):
        index = self.consecuent.find('=')
        return self.consecuent[0:index].strip()

    def calculate_crisp(self, inputs):
        return eval(self.consecuent, inputs)