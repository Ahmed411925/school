# Course: CS 30
# Period: 1
# Date created: 21/03/11
# Date last modified: 21/03/16
# Name: Ahmed Keshta
# Description: RPG Inventory


# stats for entities
player = {'name': 'bill', 'health': 100, 'strength': 10, 'hunger': 9}
alien = {'name': 'alien', 'health': 100, 'strength': 10, 'points': 15}
spider = {'name': 'spider', 'health': 10, 'strength': 5, 'points': 5}
zombie = {'name': 'zombie', 'health': 50, 'strength': 10, 'points': 10}


# Item dictionaries
sword = {
  'name': 'Sword',
  'damage': 10,
  'description': 'Useful for close range enemies'
}


shield = {
  'name': 'Shield',
  'description': 'Reduces incoming damage when equipped'
}


bandage = {
  'name': 'Bandage',
  'description': 'Restores 10 hp to player'
}


apple = {
  'name': 'apple',
  'description': 'Restores 2 hunger points'
}


# Locations and their descriptions
locations = {
  'generator': 'This is where electricity is generated',
  'cafeteria': 'This is where you can acquire food',
  'bedroom': 'Come here to get some rest'
}


inventory = [sword, shield, bandage, apple]
enemies = [alien, spider, zombie]


# Printing of player stats
print(f'Player Stats:\n')
name = player['name'].title()
health = player['health']
strength = player['strength']
hunger = player['hunger']
print(f"\t{name}'s health is at {health}")
print(f"\t{name}'s strength is {strength}")
print(f"\t{name}'s hunger is at {hunger}/10")


# Printing of enemy stats
print(f'\n Enemy Stats: \n')
for enemy in enemies:
    name = enemy['name'].title()
    health = enemy['health']
    strength = enemy['strength']
    points = enemy['points']
    print(f"\t{name}'s health is {health}")
    print(f"\t{name}'s strength is {strength}")
    print(f"\t{name} is worth {points} points \n")


# Printing of location descriptions
generator = locations['generator']
cafeteria = locations['cafeteria']
bedroom = locations['bedroom']
print(f'Locations:\n')
print(f'\tGenerator: {generator}')
print(f'\tCafeteria: {cafeteria}')
print(f'\tBedroom: {bedroom}')


# Printing of inventory contents
print(f'\nInventory:\n')
for item in inventory:
    name = item['name']
    description = item['description']
    print(f'\t{name.title()}: {description}')
