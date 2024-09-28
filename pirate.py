"""
File: pirate.py
Description: <Pirate python module A Pirate has a name and starts with an 
inventory containing one Gold Piece, in addition to possibly being able to 
buy another ship. The Pirate will be able to do a number of things like:
buying his ship, 
fixing the ship 
cannonball a ship 
and he can loot other ships>
Author: <Mridul Chopra>
"""

from loot import Loot
from ship import Ship


class Pirate():
   
    def __init__(self, name):
        self.__name = name  # givin name to pirate 
        self.__inventory = [Loot("Gold Piece","A piece of gold")] #defailt inventory one gold piece of class loot
        self.__ship = ""

    # Setterss
    def set_name(self, name):
        self.__name = name
    
    # Getters
    def get_name(self):
        return self.__name
    
    def purchase_ship(self,ship):
        # Makes it so the pirate can buy a ship 
        if isinstance(ship, Ship):# The ship object has to be an instance of the Ship class.
            for loot in self.__inventory:
                if loot.get_name() == "Gold Piece": # cheacks if a pirate has a Gold Piece in his inventory.
                    self.__inventory.remove(loot)
                    self.__ship = ship
                
            print(f"ARRRR!!!! Congratulations you just Baught: {ship.get_name()}")
        else:
            print(f"ARRRR!!!! {ship} Should be of class Ship")
            
    def __repair_ship(self):
        # private method used in repairing the ship. As far as pirate have a Gold Piece to fix it.
        if self.__cheack_ship():  # It validates whether the pirate has the ship
            for loot in self.__inventory:
                if loot.get_name() == "Gold Piece":# It take away the Gold Piece and repair the ship for the pirate.
                    self.__inventory.remove(loot)
                    self.__ship.repair_ship()

    def battle(self,enemy_ship):
        # Function to engages in a battle with an enemy ship.
        if isinstance(enemy_ship, Ship): # The enemy_ship must be an instance of the Ship class.
            if self.__cheack_ship():# The pirate must have their own ship 
                for loot in self.__inventory:
                        if loot.get_name() == "Cannonballs": #and Cannonballs in their inventory to attack.
                            self.__inventory.remove(loot)
                            enemy_ship.take_hit()
                            if enemy_ship.get_damage_counte() >= 2: # If the enemy ship is at enough damage (damage_counter >= 2), the pirate loots the ship., get_damage() to get the value of damage at ship
                                self.__loot_ship(enemy_ship)
                            break # breaks the loop at first instance connonballs otherwisse would damage ship twice in one go.
                else:
                    print("Do not have a cannonball yet")
            else:
                print(f"ARR!! Mateyyy!!!! Cannot battle without a ship!!")
        else:
            print(f"ARRRR!!!! {enemy_ship} Should be of class Ship")

    
    def __loot_ship(self,enemy_ship):
        # Private method to loot an enemy ship after the enemy_ship breaks
        if isinstance(enemy_ship, Ship):
            if self.__cheack_ship():
                for items in enemy_ship.get_cargo(): # All items from enemy ship's cargo are appeneded to the pirate's inventory, and removed from enemy_ship's cargo.
                    self.__inventory.append(items)
                enemy_ship.set_cargo([])
        else:
            print(f"ARRRR!!!! {enemy_ship} Should be of class ship")
            
    
    def __cheack_ship(self):
        # Private method to check if the pirate has a ship.
        if self.__ship == "":
            return False # Returns False if the pirate does not have a ship, otherwise returns True.
        else: 
            return True #otherwise would return True
            
    def store_cargo(self, item_name):
        # Stores an item from the pirate's inventory into the ship's cargo.
        if self.__cheack_ship(): # The pirate must have a ship
            item = self.__ship.get_item(item_name) # get_item() to cheack the name of item(funciton in loot modulw)
            if item: 
                self.__ship.get_cargo().append(item) # Appends to ship's cargo
                self.__inventory.remove(item) # Remove from pirate inventory
            else: # if there is no item
                print(f"{item_name} not in inventory")

    def store_inventory(self, item_name):
        # Stores an item from the ship's cargo to the pirate's inventory.
        if self.__cheack_ship():# The pirate must have a ship,
            item = self.__ship.get_item(item_name) # get_item() to cheack the name of item(funciton in loot modulw)
            if item:
                self.__inventory.append(item) # append to pirate inventory
                self.__ship.get_cargo().remove(item) # Remove from ship's cargo
            else:
                print(f"{item_name} not in cargo")
            
    def __str__(self):
        # Returns a string representation of the pirate, including their name, ship status, and inventory.
        if self.__cheack_ship(): # If the pirate has a ship
            inventory_items_in_str = "" # Empty string to import all the items in the list
            for item in self.__inventory:
                if self.__inventory.index(item) == len(self.__inventory)-2: 
                    inventory_items_in_str += item.get_name() + " and " # concatinating "and" as seperators if its the second last emlent
                else:
                    inventory_items_in_str += item.get_name() + ", " # concatinating "," as seperators if its not the last emlent
            return f"Pirate: {self.__name}\nShip: {self.__ship.get_name()}\nInventory: {inventory_items_in_str[:-2]}" # Retrun a string

        else: # if pirate does not have the ship it should still retunr string but without ship name and should only put one item in the inventory that is by default gold piece
            inventory_items_in_str = ""
            for item in self.__inventory:
                inventory_items_in_str += item.get_name()
            return f"!!!!!!ARRRRR!!!!!!\nPirate: {self.__name}\nShip: no ship\nInventory: {inventory_items_in_str}"
        



        
    
