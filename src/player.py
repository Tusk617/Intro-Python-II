# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location, inventory=['Lantern']):
        self.name = name
        self.location = location
        self.inventory = inventory
    def tryMove(self, command):
        attribute = command + "_to"

        if hasattr(self.location, attribute):
            self.location = getattr(self.location, attribute)
        else:
            print("Sorry lad, this way seems to lead nowhere.")
    def addItem(self, newItem):
        print(f"You tuck {newItem} away in your satchel!")
        self.inventory.extend(newItem)
    def dropItem(self, item):
        self.inventory.remove(item)
        print(f"You just dropped {item}!")
    def currentInv(self):
        for item in self.inventory:
            print(item)
        