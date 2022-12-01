class area_rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def Rect_Calct(self):
        return self.l * self.b

area1=area_rect(6,2)
area2=area_rect(15,3)
print(area1.Rect_Calct())
print(area2.Rect_Calct())
