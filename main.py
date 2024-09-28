"""
File: main.py
Description: <module where i test code.>
Author: <Mridul Chopra>
"""
from loot import Loot
from ship import Ship
from pirate import Pirate


#Test_Case 1
p1 = Pirate("Jack Sparrow")
s1 = Ship("The Black Pearl")
es = Ship("Dying Gull")

# Testing Pirate Methods
p1.battle(es) #does not run because does not have a ship yet
p1.purchase_ship(s1)
p1.battle(es) #cannot fight because does not have a cannonball in inventory
p1.store_inventory("Cannonballs")
p1.battle(es) #can fight because now have a cannonball in inventory from ship
print()

##Testing Ship Methods
print(s1) # have only one cannon ball now
print()
print(es) # have one damage
print(es.check_condition()) #ship is damaged
print()

#now we battle again so that we can break the ship
p1.store_inventory("Cannonballs")
p1.battle(es)
print(es) # have two damage
print(es.check_condition()) #ship is broken
print()

#now we cheack pirate inventory
print(p1) # pirate inventory has all the loot in enemy ship

