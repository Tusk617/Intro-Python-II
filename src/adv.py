from room import Room
from player import Player
import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.\n"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.\n"""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.\n"""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.\n"""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.\n"""),
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
player = Player(room["outside"])
# currentRoom = player
journey_complete = False
badDirection = "There is nothing for you that way, try another direction...\n"
# print(Player(room["outside"]))
# print(player.currentRoom)
# print(room["outside"])

while (journey_complete == False):
    print(player)
    movement = input("Where would you like to go next?  \n")
    if (movement == "quit"):
        print("Until next time hero...")
        journey_complete == True
        break
    if (player.currentRoom == room["outside"]):
        if (movement == "north"):
            player = Player(room["outside"].n_to)
            continue
        elif (movement != "north"):
            print(badDirection)
            continue
    if (player.currentRoom == room["foyer"]):
        if (movement == "south"):
            player = Player(room["foyer"].s_to)
            continue
        elif (movement == "north"):
            player = Player(room["foyer"].n_to)
            continue
        elif (movement == "east"):
            player = Player(room["foyer"].e_to)
            continue
        else:
            print(badDirection)
            continue
    if (player.currentRoom == room["overlook"]):
        if (movement == "south"):
            player = Player(room["overlook"].s_to)
            continue
        else:
            print(badDirection)
            continue
    if (player.currentRoom == room["narrow"]):
        if (movement == "north"):
            player = Player(room["narrow"].n_to)
            continue
        elif (movement == "west"):
            player = Player(room["narrow"].w_to)
        else:
            print(badDirection)
            continue
    if (player.currentRoom == room["treasure"]):
        if(movement == "south"):
            player = Player(room["treasure"].s_to)
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
