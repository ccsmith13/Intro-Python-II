from room import Room
from player import Player
from item import Item

# Declare all the rooms
all_items = {
    'candlestick': Item('candlestick', 'a tarnished silver candlestick'),
    'match': Item('match', 'matches can start fires.'),
    'boulder': Item('boulder', 'a rock as tall and wide as you are tall'),
    'cobweb': Item('cobweb', 'yuck, does that mean there are spiders?'),
    'dubloons': Item('dubloons', 'a large canvas sack containing one million dubloons - jackpot!')
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
        available_items = []
        player_available_items = []
        for item in new_player.location.item_list:
            print(item.name, item.description) 
            available_items.append(item.name)
        for item in new_player.inventory:
            player_available_items.append(item.name)
    print('Which direction would you like to go to? Or do something else? Enter one of the following: (n, s, e, w, or take/get itemname)')
    next_direction = input()
    if 'take' in next_direction or 'get' in next_direction:
        selected_item = next_direction.split(' ')
        if len(selected_item) > 2:
            print('Invalid command. Please try again.')
        else:
            selected_item = selected_item [1]
            if selected_item in available_items and new_player.location.item_list != []:
                selected_item_index = available_items.index(selected_item)
                new_player.location.item_list[selected_item_index].on_take()
                selected_item = new_player.location.item_list.pop(selected_item_index)
                new_player.inventory.append(selected_item)
            else:
                print('That item is not in this room. Would you like to go somewhere else instead? Enter one of the following: (n, s, e, w)')
    elif 'drop' in next_direction:
        selected_item = next_direction.split(' ')
        if len(selected_item) > 2:
            print('Invalid command. Please try again.')
        else:
            selected_item = selected_item [1]
            if selected_item in player_available_items and new_player.inventory != []:
                selected_item_index = player_available_items.index(selected_item)
                new_player.inventory[selected_item_index].on_take()
                selected_item = new_player.inventory.pop(selected_item_index)
                new_player.location.item_list.append(selected_item)
            else: 
                print('That item is not in this room. Would you like to go somewhere else instead? Enter one of the following: (n, s, e, w)')
    else:
        if next_direction == 'q':
            next_direction = ''
            print('Exiting game. Thank you for playing!')
        elif next_direction == 'i':
            print('Current Inventory:')
            if new_player.inventory == []:
                print('You have no items')
            else:
                for i in new_player.inventory:
                    print(i.name)
        else:
            next_direction = next_direction + '_to'
            try: 
                x = getattr(new_player.location, next_direction)
                new_player.location = x
            except AttributeError:
                print('A pile of bricks blocks your path. Try a different direction?')
