class AreaTriangle:

    def __init__(self, h, b):
        self.h=h
        self.b=b

    def calc_area(self):
        finalarea = (self.h*self.b)/2
        return finalarea

area1=AreaTriangle(8, 5)
print(area1.calc_area())
area2=AreaTriangle(50, 20)
print(area2.calc_area())

