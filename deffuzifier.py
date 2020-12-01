from functions import *

class Deffuzifier:
    def __init__(self, resolution):
        self.resolution = resolution

    def defuzzify(self, aggregation):
        raise NotImplementedError()

class Centroid(Deffuzifier):
    def __init__(self, resolution):
        super().__init__(resolution)

    def defuzzify(self, aggregation):
        min, max = aggregation.bounds()
        scale = (max - min) / self.resolution
        num = den = 0
        x = min
        while x <= max:
            fx = aggregation.membership(x)
            num += fx * x
            den += fx
            x += scale
        return round(num / den, 1)

class MOM(Deffuzifier):
    def __init__(self, resolution):
        super().__init__(resolution)

    def defuzzify(self, aggregation):
        max_truncate = aggregation[0][0]
        function = aggregation[0][1]
        for i in range(1, len(aggregation)):
            if aggregation[i][0] > max_truncate:
                max_truncate = aggregation[i][0]
                function = aggregation[i][1]
        max_points = function.truncate(max_truncate)    
        return round(sum(max_points)/len(max_points), 1)    

class Bisection(Deffuzifier):
    def defuzzify(self, aggregation): 
        xl, xr = aggregation.bounds()
        scale = (xr - xl) / self.resolution
        left = right = 0
        steps = self.resolution
        while steps > 0:
            if left <= right:
                xl += scale
                left += aggregation.membership(xl)
            else:
                xr -= scale
                right += aggregation.membership(xr)
            steps -= 1        
        return round((xl + xr) / 2, 1)


# t1 = Triangle('t1', 1, 3, 5)
# t2 = Trapezoid('t2', 4, 4, 8, 10)
# a1 = Aggregation('a1', [(0.8, t1),(0.5, t2)])

# centroid = Centroid(50)
# result = centroid.defuzzify(a1)
# print(result)

# mom = MOM(50)
# result1 = mom.defuzzify(a1)
# print(result1)

# bisector = Bisection(50)
# result2 = bisector.defuzzify(a1)
# print(result2)


