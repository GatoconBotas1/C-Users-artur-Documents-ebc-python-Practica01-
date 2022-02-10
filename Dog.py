class Dog :
    def __init__(self, name, size, color, race):
        self.name = name
        self.size = size
        self.color = color
        self.race = race

    def printInfo(self):
        print(self.name, self.size, self.color, self.race)

dog = Dog("Firulais", 12, "Black", "Labrador")

dog.printInfo()
