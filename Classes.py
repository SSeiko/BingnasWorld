import numpy as np

#contains behaviour all Organisms should have, Health, food, age, children, genes etc
class Organism():
    def __init__(self, position , timePoints, health, age, hunger):
        self.position = position
        self.timePoints = 100
        self.health = health
        self.age = age
        self.hunger = hunger

    def update_position(direction):
        position = self.position+direction
    
    def update_health(amount):
        health += amount

    def update_age(amount):
        age += amount

    def update_hunger(nhunger):
        hunger += nhunger
    
    def update_all(direction, healthamount, ageamount, hungeramount):
        update_position(direction)
        update_health(healthamount)
        update_age(ageamount)
        update_hunger(hungeramount)

#Contains behaviour all food should have, such as position, age, etc
class Food():
    def __init__(x,y,z):
        self.x = x
        self.y = y
        self.z = z

# Holds list of coordinates and entities at each coordinate
class Map():
    def __init__(x,y,z):
        self.x = x
        self.y = y
        self.z = z




def mapGen(horizontal, vertical):
    # generates a list of paired coordinates given an horizontal and vertical input
    maplist = []
    for y in range(0, vertical):
        for x in range(0, horizontal):
            maplist.append((x,y))
    return maplist

def movePosition (entity, move_direction):
    new_Position = entity.update_position(move_direction)

my_org = Organism((0, 1), 100, 1, 1, 1)

print(my_org, my_org.update_hunger())
