class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4)
print(miles.speak("Woof Woof"))
print(miles.speak("Bow Wow"))
print(miles.description())


class JackRussellTerrier(Dog):
    print(miles.description())

# class Dog:
#     species = "Canis familiaris"
#
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
#
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
#
# #miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jamck", 3, "Bulldog")
# jim = Dog("Jim", 5, "Jack Russell Terrier")
# print(buddy.speak("Yap"))
# print(jim.speak("Woof"))
# print(jack.speak("Woof"))