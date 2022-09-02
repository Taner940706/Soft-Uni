class Vet:

    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = list()

    def register_animal(self, animal_name):
        if Vet.space:
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            Vet.space -= 1
            return f"{animal_name} registered in the clinic"
        else:
            return "Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in Vet.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            Vet.space += 1
            return f"{animal_name} unregistered successfully"
        else:
            return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"