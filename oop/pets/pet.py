# pet.py

class Pet:
    def __init__(self, pet_name, pet_species, pet_family_type, pet_owner_name):
        self.__petName = pet_name
        self.__petSpecies = pet_species
        self.__petFamilyType = pet_family_type
        self.__petOwnerName = pet_owner_name

    def set_name(self, pet_name):
        self.__petName = pet_name

    def set_species(self, pet_species):
        self.__petSpecies = pet_species

    def set_family_type(self, pet_family_type):
        self.__petFamilyType = pet_family_type

    def set_owner(self, pet_owner_name):
        self.__petOwnerName = pet_owner_name

    def bark(self):
        return "Woof! Woof!"

    def get_name(self):
        return self.__petName

    def get_species(self):
        return self.__petSpecies

    def get_family_type_capitalized(self):
        return self.__petFamilyType.capitalize()

    def get_family_type(self):
        return self.__petFamilyType

    def get_owner(self):
        return self.__petOwnerName

    def __str__(self):
        return (f"Pet Name: {self.get_name()}, Species: {self.get_species()}, "
                f"Family Type: {self.get_family_type()}, Owner: {self.get_owner()}")
