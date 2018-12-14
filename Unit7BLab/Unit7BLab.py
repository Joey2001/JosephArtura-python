class petClass():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def info(self):
        return("The " + self.breed +"\'s name is " + self.name + '.')

class childClass():
    def __init__(self, name):
        self.name = name
    def childInfo(self):
        return("The child's name is " + self.name + '.')

class dogClass(petClass):
    def __init__(self, name, breed, activity):
        petClass.__init__(self, name, breed)
        self.activity = activity
    def action(self):
        return("The " + self.breed +"\'s name is " + self.name + ". The dog is currently " + self.activity + ".")
myPet1 = dogClass("Rover", "Golden Retriver", "playing fetch")
print(myPet1.info())
myPet2 = dogClass("Grover", "Husky", "sleeping")
print(myPet2.action())

