from room import Room
from player import Player
from item import Item

# Declare all the rooms
all_items = {
    'candlestick': Item('Candlestick', 'A tarnished silver candlestick. Heavy.'),
    'match': Item('Match', 'Matches can start fires.'),
    'boulder': Item('Boulder', 'A rock as tall and wide as you are tall.'),
    'cobweb': Item('Cobweb', 'Yuck, does that mean there are spiders?'),
    'dubloons': Item('Dubloons', 'A large canvas sack containing one million dubloons - jackpot!')
}
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [all_items['candlestick'], all_items['match']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [all_items['boulder']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [all_items['cobweb']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [all_items['dubloons']]),
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
new_player = Player(room['outside'])
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
next_direction = 'placeholder'
while next_direction: 
    print('You are currently at the', new_player.location.name)
    print(new_player.location.description)
    print('Items in this room:')
    if new_player.location.item_list == []:
        print('No items available')
    else:
        for item in new_player.location.item_list:
            print(item.name, item.description) 
    print('Which direction would you like to go to? Or do something else? Enter one of the following: (n, s, e, w, or take/get itemname)')
    next_direction = input()
    if lower(next_direction)[0:4] == 'take' or 'get ':
        print('The player wants to take an item')
        next_direction = ''
    else:
        if next_direction == 'q':
            next_direction = ''
            print('Exiting game. Thank you for playing!')
        else:
            next_direction = next_direction + '_to'
            try: 
                x = getattr(new_player.location, next_direction)
                print('You can move this direction.')
                new_player.location = x
            except AttributeError:
                print('A pile of bricks blocks your path. Try a different direction?')
