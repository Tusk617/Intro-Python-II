from room import Room
from player import Player
from items import Items

# Declare all the rooms

roomLoot = {
    "torch": Items("Torch", "A wooden branch, with an oily rag wrapped around it's top."),
    "skull": Items("Skull", "A skull... it looks human! Keep it if you want, i'm not your mom."),
    "sword": Items("Sword", "A blunted, rusted iron sword. Not in the best shape, but it will help in a pinch!")
}


# Getting the rooms to be able to be accessed by the player is a little encumbersome
#due to the fact that I need the keynames for each room to access loot. So to remedy this
# I decided to add a 'keyName' value for the Room class, which just holds the key name
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", "outside"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "foyer", [roomLoot["torch"].Iname, roomLoot['sword'].Iname]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "overlook"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "narrow"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "treasure"),
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

#intializing player and other variables
playerName = input("What do they call you? ")
playerInv = []
player = Player(playerName, room['outside'])
movementOptions = ['n', 'e', 's', 'w']
journeyComplete = False


# print(room[player.location.keyName])

# print(player.location.keyName)

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
while journeyComplete == False:
    currentLocation = room[player.location.keyName]
    print(player.location)
    command = input("What would you like to do?  ").split()

    if command[0] == 'end':
        print(f"See you next time, {playerName}!")
        journeyComplete = True
    if command[0] in movementOptions:
        player.tryMove(command[0])
    #inventory commands
    if command[0] == 'search':
        currentLocation.searchForLoot()
    if command[0] == 'inv':
        player.currentInv()
    if command[0] == 'grab':
        for item in currentLocation.loot:
            if command[1] == f'{item.lower()}':
                player.addItem([item])
                currentLocation.lootTaken(item)
            else:
                print(f"You can't seem to find {item}")
    if command[0] == 'drop':
        player.dropItem(command[1])
        currentLocation.droppedItem(command[1])
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
