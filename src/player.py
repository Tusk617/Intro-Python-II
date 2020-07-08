# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        # self.name = name
    def __str__(self):
        return f"{self.currentRoom}"