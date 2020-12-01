from functions import *

class Expression:
    def evaluate(self, inputs):
        raise NotImplementedError()

class UnaryExpression(Expression):
    def __init__(self, variable, membership_func):
        self.variable = variable
        self.membership_func = membership_func
        
class Not(UnaryExpression):
    def evaluate(self, inputs):
        return 1 - self.membership_func.membership(inputs[self.variable])
     
    def __repr__(self):
        return '{0} is NOT {1}'.format(self.variable, self.membership_func.name)
 
class Predicate(UnaryExpression):
    def evaluate(self, inputs):
        return self.membership_func.membership(inputs[self.variable])
    def __repr__(self):
        return '{0} is {1}'.format(self.variable, self.membership_func.name)

class BinaryExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class And(BinaryExpression):
    def evaluate(self, inputs):
        return min(self.left.evaluate(inputs), self.right.evaluate(inputs))

    def __repr__(self):
        return '{0} AND {1}'.format(repr(self.left), repr(self.right))    

class Or(BinaryExpression):
    def evaluate(self, inputs):
        return max(self.left.evaluate(inputs), self.right.evaluate(inputs))

    def __repr__(self):
        return '{0} OR {1}'.format(repr(self.left), repr(self.right))  