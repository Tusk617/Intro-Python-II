from room import Room
from player import Player
from item import Item
import textwrap
# Declare all the rooms
loot3 = ["Nothing loser, lmao you thought"]
noLoot = []

lootables = {
    "Skull": Item("Skull", "A human skull, oh my God! Why is this here? Why am I touching it? Oh God!"),
}
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.\n", lootables.keys()),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.\n""", noLoot),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.\n""", noLoot),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.\n""", noLoot),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.\n""", loot3),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
playerName = input("What do they call you, O' brave adventurer...? \n")
player = Player(room["outside"], playerName)
journey_complete = False
badDirection = "There is nothing for you that way, try another direction...\n"


print(f"{playerName} is it? Fantastic! Then let us begin! \n\n\n")

while (journey_complete == False):
    print(player)
    action = input("What shall you do?  \n").split(' ')
#Specific actions for interacting with the environment
    if (action[0] == "quit"):
        print("Until next time hero...")
        journey_complete == True
        break
    if (action[0] == "inv"):
        player.currentInv()
        continue
    if (action[0] == "search"):
        if (room["outside"] == player.currentRoom):
            room["outside"].lootInRoom()
            continue
        elif (room["foyer"] == player.currentRoom):
            room["foyer"].lootInRoom()
            continue
        elif (room["overlook"] == player.currentRoom):
            room["overlook"].lootInRoom()
            continue
        elif (room["narrow"] == player.currentRoom):
            room["narrow"].lootInRoom()
            continue
        elif (room["treasure"] == player.currentRoom):
            room["treasure"].lootInRoom()
            continue
    if (action[0] == "grab"):
        if (action[1] in lootables):
            lootables.pop(action[1])
            player.inventory.extend([action[1]])
            print(f"You find a {action[1]}! You tuck it away in your satchel.")
            continue
        else:
            print("You can't seem to find that item...")
            continue
    if (action[0] == "drop"):
        player.inventory.remove(action[1])
        print(f"You dropped {action[1]}!")
        lootables.update({"Skull": "A human skull, oh my God! Why is this here? Why am I touching it? Oh God!"})
# Movement commands 
    if (player.currentRoom == room["outside"]):
        if (action[0] == "north"):
            player.currentRoom = room["outside"].n_to
            continue
        elif (action[0] != "[north]"):
            print(badDirection)
            continue
    if (player.currentRoom == room["foyer"]):
        if (action[0] == "south"):
            player.currentRoom = room["foyer"].s_to
            continue
        elif (action[0] == "north"):
            player.currentRoom = room["foyer"].n_to
            continue
        elif (action[0] == "east"):
            player.currentRoom = room["foyer"].e_to
            continue
        else:
            print(badDirection)
            continue
    if (player.currentRoom == room["overlook"]):
        if (action[0] == "south"):
            player.currentRoom = room["overlook"].s_to
            continue
        else:
            print(badDirection)
            continue
    if (player.currentRoom == room["narrow"]):
        if (action[0] == "north"):
            player.currentRoom = room["narrow"].n_to
            continue
        elif (action[0] == "west"):
            player.currentRoom = room["narrow"].w_to
        else:
            print(badDirection)
            continue
    if (player.currentRoom == room["treasure"]):
        if(action[0] == "south"):
            player.currentRoom = room["treasure"].s_to
            continue
        else:
            print(badDirection)
            continue
    
        

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.