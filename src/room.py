# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, roomName, roomDesc, keyName, loot=[]):
        self.roomName = roomName
        self.roomDesc = roomDesc
        self.keyName = keyName
        self.loot = loot
    
    def searchForLoot(self):
        if len(self.loot) == 0:
            print("You don't seem to find anything worth taking...")
        else:
            print(f"You scan around the room and find... {self.loot}")
    def lootTaken(self, item):
        self.loot.remove(item)
    def droppedItem(self, item):
        self.loot.append(item)

    def __str__(self):
        return f"You are at: {self.roomName}, Description: {self.roomDesc}"