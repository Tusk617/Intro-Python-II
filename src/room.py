# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, loot=[], n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.loot = loot
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def lootInRoom(self):
        print(f"Your eyes scan the room, and with a keen gaze you notice: {self.loot}")
        
    def __str__(self):
        return f"{self.name}; {self.description}\n"