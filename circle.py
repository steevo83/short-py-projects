import math

class Circle:
    def __init__(self, r=1):
        self._radius = r

    def __repr__(self):
        return 'Circle(' + repr(self.radius) + ')'


    @property
    def radius(self):
        return self._radius
    
    @property
    def diameter(self):
        return self.radius*2

    @property
    def area(self):
        return math.pi*self.radius**2

    @radius.setter
    def radius(self, r):
        if (r >= 0):
            self._radius = r
        else:
            raise ValueError ("Radius cannot be negative")
    
    @diameter.setter
    def diameter(self, d):
        self.radius = d/2

    @area.setter
    def area(self, a):
        raise AttributeError ("Cannot set attribute \"area\"")

c = Circle()

print(c)

c.area = 19

print(c.radius)
print(c.diameter)
print(c.area)

c.radius = 5

print(c.radius)
print(c.diameter)
print(c.area)

c.diameter = 5

print(c.radius)
print(c.diameter)
print(c.area)

c.radius = -5

print(c.radius)
print(c.diameter)
print(c.area)