# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = { 'animal': 'tiger', 'name': 'kane', 'owner': 'lodu','weight': 76,'eats': 'meat',}
pets.append(pet)

pet = {'animal': 'cat','name': 'muki','owner': 'tiya','weight': 6,'eats': 'plants',}
pets.append(pet)

pet = {'animal': 'dog','name': 'polo','owner': 'liya','weight': 56,'eats': 'bread',}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))