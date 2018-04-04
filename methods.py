import math
from test.pyclbr_input import Other

class Vector2D:
    x=0.0
    y=0.0
    
    def Set(self,x,y):
        self.x= x
        self.y = y 
    
    
class Vector2D_new:

    def __init__(self,x,y):
        print("___init__")
        self.x= x
        self.y = y 
    def __add__(self,other):
        print("__add__")
        return Vector2D_new(self.x + other.x , self.y+other.y)
    def __iadd__(self,other):
        print("__iadd__")
        self.x += other.x
        self.y += other.y
        return self
    def __sub__(self,other):
        print("__sub__")
        return Vector2D_new(self.x - other.x , self.y-other.y)
    def __mul__(self,other):
        print("__mul__")
        return Vector2D_new(self.x * other.x , self.y*other.y)
    def __imul__(self,other):
        print("__imul__")
        self.x *= other.x
        self.y *= other.y
        return self
    
    def getLength(self):
        print("getLength")
        return math.sqrt(self.x**2 +self.y**2)
    def normalize(self):
        print("normalize")
        len = self.getLength()
        if len!=0:
            return Vector2D_new(self.x/len , self.y/len)
        return Vector2D_new(self)
    def getAngle(self):
        print("getAngle")
        return math.degrees(math.atan2(self.y, self.x))
    def __str__(self):
        return "x: "+str(self.x)+" y: "+str(self.y)
    
def Main():
    vecold = Vector2D()
    vecold.Set(5, 4)
    print("x: "+str(vecold.x) + " y: "+ str(vecold.y))
    vec = Vector2D_new(5,8)
    print(vec)
    vec2 = Vector2D_new(2,3)
    print(vec2)
    vec = vec+vec2
    print(vec)
    vec += vec2
    print(vec)
    vec *= vec2
    print(vec)
    vec += vec2
    print(vec.normalize())
    print(vec.getAngle())
    
if __name__=='__main__':
    Main()   