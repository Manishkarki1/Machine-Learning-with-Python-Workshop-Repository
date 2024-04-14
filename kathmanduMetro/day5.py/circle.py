import math
class Circle:
    def __init__(self,r):
        self.r=r
    
    def area(self):
        formula=round(math.pi * self.r ** 2,2)
        print(f"Area of circle is {formula}")
    def perimter(self):
        formula=round(2 * math.pi * self.r,2)
        print(f"Perimeter of circle is {formula}")

obj1=Circle(5)
obj1.area()
obj1.perimter()