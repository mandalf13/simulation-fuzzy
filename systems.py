import numpy as np
from rules import *
from deffuzifier import *

class TSK:
    def __init__(self, rules):
        self.rules = rules

    def compute(self, inputs):
        output = {}
        for rule in self.rules:
            var = rule.output_variable
            strength = rule.calculate_strength(inputs)
            crisp = rule.calculate_crisp(inputs)
            if var in output:                
                output[var]=(output[var][0] + strength*crisp, output[var][1] + strength)
            else:
                output[var]=(strength*crisp, crisp)
        result = {key : output[key][0] / output[key][1] for key in output.keys()}
        return result

class Mamdani:
    def __init__(self, rules, deffuzifier):
        self.rules = rules
        self.deffuzifier = deffuzifier

    def build_aggregations(self, inputs):
        aggrs = {}
        for rule in self.rules:
            strength = rule.calculate_strength(inputs)
            var = rule.output_variable()
            adj = rule.consecuent.membership_func
            if var in aggrs.keys():
               index = self.get_index(adj, aggrs[var])
               if np.isnan(index): 
                   aggrs[var].append((strength, adj))
               else:    
                   if aggrs[var][index][0] < strength:
                       aggrs[var][index] = (strength, adj)
            else:
                aggrs[var] = [(strength, adj)]
        return aggrs        
    
    # get the index of a membership function in an aggregation
    def get_index(self, membership_func, aggr):
        for i in range(len(aggr)):
            if aggr[i][1].name == membership_func.name: return i
        return np.nan   
    
    def compute(self, inputs):
        output = {}
        aggrs = self.build_aggregations(inputs)
        for var in aggrs.keys():
            current = Aggregation(var, aggrs[var])
            #for elem in current.aggregation:
            #    print('{0} -- {1}'.format(elem[0], elem[1].name))
            output[var]= self.deffuzifier.defuzzify(current)
        return output    

