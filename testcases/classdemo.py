class dog:
    def __init__(self, dogbreed, dogcolor):
        self.breed = dogbreed
        self.color = dogcolor

    def Dog_Details(self):
        return self.breed, self.color


Tuffy = dog("german Shepherd", "Black & Tan")
print(Tuffy.Dog_Details())
