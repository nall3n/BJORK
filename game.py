from inputCheck import InputCheck
from world import Room, Item, Static_Item, Key, Player, World_Builder



def main():
    p = '> '

    input_check = InputCheck()

    player = Player(2,2)

    world_build = World_Builder(5,5)

    stick = Item('Stick', 'A medium stick')
    cabinet = Static_Item('Cabinet1',
                        'En lite byrå',
                        True,
                        False,
                        [stick],
                        None
                        )

    balroom = Room('Balroom',
                    'You stand i a bigg room with a lott of stuff',
                    ['n','s'],
                    False, 
                    cabinet,
                    )

    world_build.add_room(balroom, 2,2)

    world = world_build.get_world()

    run = True
    while run:
        current_room = world[player.x][player.y]
        current_room.enter_room()
        
        user_input = input(p)
        verb = input_check.check_verb(user_input)


        if verb == 'look':
            if current_room.name in user_input:
                current_room.get_info()
            if current_room.static_items.name in user_input:
                current_room.static_items.look_att()


if __name__ == '__main__':

    main()

