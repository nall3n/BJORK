from game import *
from world import world, items
from inputCheck import InputCheck


p='>'
#Set players start room
startPos = 'entrance'

movement = Movment(startPos)
bag = Player_bag(20)

inputCheck = InputCheck()




def move(playerPos, user_input):
    """Getts room current room connections 
    Gives them to to movement to check if its possible to move player"""
    exit, connections = world[playerPos].get_connections()
    movement.move_player(exit, connections, user_input)

def take_item(playerPos, user_input):
    """Removes item from room
    Adds it to player bag"""
    #MERG
    item = world[playerPos].remove_item(user_input)
    bag.add_item(item)

def drop_item(playerPos, user_input):
    item = bag.remove_item(user_input)
    world[playerPos].add_item(item)

def main():
    run = True
        
    world[startPos].print_room_name()
    world[startPos].look_at_room()

    while run:        
        #Get players current posision
        playerPos = movement.get_player_pos()
        
        #Print room name and info
        print()

        #Take input from user
        user_input = input(p)
        verb =inputCheck.check_verb(user_input)        

        if verb in ('n','s','e','w'):
            move(playerPos, verb) 
            playerPos = movement.get_player_pos()
            print()
            world[playerPos].print_room_name()
            world[playerPos].look_at_room()

        elif verb == 'inventory':
            print("looking att inventory:)")
            bag.show_bag_items()
        elif verb == 'take':
            take_item(playerPos, user_input)
        elif verb == 'drop':
            drop_item(playerPos, user_input)

main()
