class Player:
    def __init__(self, currentRoom, name, inventory=[]):
        self.currentRoom = currentRoom
        self.name = name
        self.inventory = inventory
    def addItem(self, newItem):
        self.inventory.extend(newItem)
    def currentInv(self):
        print(f"What's it got in it's pockets?:  {self.inventory}")
    def __str__(self):
        return f"{self.name} is in: {self.currentRoom}"