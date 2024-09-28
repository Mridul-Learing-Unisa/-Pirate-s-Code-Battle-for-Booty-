"""
File: ship.py
Description: <This class represents a Ship. A ship has a name,
a damage counter and its state that is broken or not. 
It too has a Cargo, cannonballs are stored in the cargo.>
Author: <Mridul Chopra>
"""
from loot import Loot

class Ship():
    def __init__(self,name): # givin name to ship
        self.__name  = name   
        self.__damage_counter = 0
        self.__broken = False
        self.__cargo = [Loot("Cannonballs","a cannon ball"),Loot("Cannonballs","a cannon ball")]
        
    def repair_ship(self): # repair ship: functoion
        if self.__broken == True: # checks if the ship is broken and then repairs it
            self.__broken = False
        elif self.__damage_counter > 0:  # checks if the ship is not broken and then increase the damage counter
            self.__damage_counter = 0

    def take_hit(self): # take hit: function
        self.__damage_counter += 1 # incrimenting the damage counter
        if self.__damage_counter >= 2: # if damage counter reaches 2 it makes the shop broken and resets the damage counter
            self.__broken = True
            self.__damage_counter = 0 
    
    def get_item(self,item_name): # get_item: function
        for item in self.__cargo: # loops thru the lootlist ot check the specific item_name
            if item.get_name() == item_name: #get_name function of class loot to return the name of the loot
                return item # retunr the item
        # if item is not found then it prints statement and returns item false
        print(f"No {item_name} found in the cargo.") 
        return False

    
    def check_condition(self): #check_condition: function
        condition = "Excellent" # asuming the condition is excellent
        if self.__damage_counter == 1: 
            condition = "Damaged"# if damage counter is 1 changing condtion to "Damaged"
        elif self.__damage_counter >= 2:
            condition = "Broken"
        return condition # if damage counter is > 2 changing condtion to "Broken"

    def set_name(self,name):
        self.__name = name
    
    def set_cargo(self,cargo):
        self.__cargo = cargo

    def get_name(self):
        return self.__name
    
    def get_damage_counte(self):
        return self.__damage_counter
    
    def get_cargo(self):
        return self.__cargo
    
    def __str__(self):
        itemInString = "" #empty string to import all the items in the list
        for item in self.__cargo:
            if self.__cargo.index(item) == len(self.__cargo)-2:
                itemInString += item.get_name() + " and " # concatinating "and" as seperators if its the second last emlent
            else:
                itemInString += item.get_name() + ", "# concatinating "," as seperators if its not the last emlent

        # retunning f string
        return f"Ship Name: {self.__name}\nDamage on ship: {self.__damage_counter}\nItems in cargo: {itemInString[:-2]}"
