
class Function:
    def __init__(self, name):
        self.name = name

    def membership(self, crisp_value):
        raise NotImplementedError()

    def bounds(self):
        raise NotImplementedError()

    def truncate(self, y):
        raise NotImplementedError()

class Triangle(Function):
    def __init__(self, name, a, b, c):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    def membership(self, crisp_value):
        if crisp_value < self.a or crisp_value > self.c:
            return 0
        elif crisp_value == self.b:
            return 1  
        elif crisp_value < self.b:         
            return 1 + (crisp_value - self.b) / (self.b - self.a)
        else:
            return 1 + (self.b - crisp_value) / (self.c - self.b)  
    
    def bounds(self):
        return self.a, self.c

    def truncate(self, y):
        assert y >= 0 and y <= 1
        points = []
        if self.a == self.b:
            points.append(self.a)
        else:
            points.append((y-1)*(self.b-self.a)+self.b)
        if self.b == self.c: 
            points.append(self.b)
        else:
            points.append(self.b-(y-1)*(self.c-self.b))
        return points

class Trapezoid(Function):
    def __init__(self, name, a, b, c, d):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def membership(self, crisp_value):
        if crisp_value < self.a or crisp_value > self.d:
            return 0
        elif crisp_value >= self.b and crisp_value <= self.c:
            return 1
        elif crisp_value < self.b:    
            return 1 + (crisp_value - self.b) / (self.b - self.a)
        else:
            return 1 + (self.c - crisp_value) / (self.d - self.c)  

    def bounds(self):
        return self.a, self.d

    def truncate(self, y):
        assert y >= 0 and y <= 1
        points = []
        if self.a == self.b:
            points.append(self.a)
        else:
            points.append((y-1)*(self.b-self.a)+self.b)
        if self.c == self.d: 
            points.append(self.c)
        else:
            points.append(self.c-(y-1)*(self.d-self.c))
        return points        


class Aggregation(Function):
    def __init__(self, name, aggregation): #'aggregation' is a list of tuples (t, function) where 't' is the truncating value of 'function'
        super().__init__(name)
        self.aggregation = aggregation

    def membership(self, crisp_value):
        l = []
        for elem in self.aggregation:
            membership = elem[1].membership(crisp_value)
            if membership > elem[0]: l.append(elem[0])
            else: l.append(membership)
        return max(l)

    def bounds(self):
        min, max = self.aggregation[0][1].bounds()
        for elem in self.aggregation:
            current = elem[1].bounds()
            if min > current[0]: 
                min = current[0]
            if max < current[1]:
                max = current[1]
        return min, max

    def __getitem__(self, item):
        return self.aggregation[item]

    def __len__(self):
        return len(self.aggregation)    
