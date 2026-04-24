# main.py

"""
Description: Project 3 Classes and Objects -     

    This project demonstrates the use of classes and objects in Python. 
    It involves the creation of a `Pet` class and utilizes various 
    object-oriented programming techniques to read pet data from a file,
    organize it into objects, and process it to display information 
    about pets and their owners based on specific criteria.

Author: Keith Thomson

Files: pet.py (class def) main.py (program) pet_data.txt (data) main.html (pydoc)

"""



from pet import Pet

def read_pet_data(file_path):

    """
    Reads pet data from a given file and creates a list of Pet objects.

    Args:
        file_path (str): The path to the file containing pet data.

    Returns:
        list: A list of Pet objects.
    """

    pets = []
    with open(file_path, 'r') as file:
        for line in file:
            pet_data = line.strip().split(' ')
            pet = Pet(pet_data[0], pet_data[1], pet_data[2], pet_data[3])
            pets.append(pet)

    return pets




def display_pets(pets):
    """
    Prints details of all pets in the list.
    
    Params: pets: list of Pet objects.
    """
    for pet in pets:
        print(pet)



def find_owners_by_family_type(pets, family_type):
    """
    Finds owners of pets that belong to a specific family type.

    Args:
        pets (list): A list of Pet objects.
        family_type (str): The family type to search for (e.g., 'dog', 'snake').

    Returns:
        list: A list of tuples containing the owner's name and pet's name.
    """


    owners = []
    for pet in pets:
        if pet.get_family_type().lower() == family_type.lower():
            owners.append((pet.get_owner(), pet.get_name()))

    return owners





if __name__ == "__main__":
    
    """
    Description: The main funcion reads the filepath and uses class function read_pet_data to read the filepath.
    It then outputs snake_owners insect_owners and dog_owners. It creates a dictionary with owners: dogs. 
    """

    file_path = '/home/whaler/data_structures/project_3/pet_data.txt'
    pets = read_pet_data(file_path)

    print("All Pets:")
    display_pets(pets)


    snake_owners = find_owners_by_family_type(pets, 'snake')
    insect_owners = find_owners_by_family_type(pets, 'insect')

    snake_owners = {owner: pet_name for owner, pet_name in find_owners_by_family_type(pets, 'snake')}
    insect_owners = {owner: pet_name for owner, pet_name in find_owners_by_family_type(pets, 'insect')}

    print("Owners \t\t Pet Name")
    print(snake_owners)
    print(insect_owners)


    dog_owners = find_owners_by_family_type(pets, 'dog')
    dog_owners = {owner: pet_name for owner, pet_name in find_owners_by_family_type(pets, 'dog')}
    
    print("Dogs and their owners in {owner: dog} format")
    print(dog_owners)
