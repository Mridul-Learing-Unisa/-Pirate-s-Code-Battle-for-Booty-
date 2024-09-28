"""
File: loot.py
Description: <This class represents a piece of Loot 
that can be moved between a Pirate's inventory and a Ship's cargo. 
Loot has a name and a description.>
Author: <Mridul Chopra>
"""

class Loot():
    def __init__(self,name,description):
        self.__name = name # giving loot a name
        self.__description = description # giving loot a Description
    
    # setterss
    def set_name(self,name):
        self.__name = name 
    
    def set_name(self,description):
        self.__description = description

    # getters
    def get_name(self):
        return self.__name
    
    def get_description(self):
        return self.__description
    
    # str function
    def __str__(self):
        return f"{self.get_name()}: {self.get_description()}"

