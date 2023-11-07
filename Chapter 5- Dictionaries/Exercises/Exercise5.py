#Pets
pets = []

pet = {
    'animal type': 'cat',
    'name': 'Tabby',
    'owner': 'Elwynn',
    'weight': 35,
    'eats': 'chicken',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'Dixie',
    'owner': 'Ben',
    'weight': 15,
    'eats': 'biscuits',
}
pets.append(pet)

pet = {
    'animal type': 'fish',
    'name': 'Gertude',
    'owner': 'Clinto',
    'weight': 27,
    'eats': 'flakes',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))