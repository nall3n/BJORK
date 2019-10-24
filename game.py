class Player:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

class Player_bag:
    def __init__(self, invSpace):
        self.bag = []
        self.space = invSpace
        
    def show_bag_items(self):
        if not self.bag:
            print("Bag is empty")

        else:
            for item in self.bag:
                print(item.name)
            


    def add_item(self, item):
        self.bag.append(item)
   
    def remove_item(self, user_input):
        """Check if userinput is == to a item in the inventory"""

        for item in self.bag:
            if item.name in user_input:
                self.bag.remove(item)
                print("You droped the %s" %item.name)
                return item

        print("Sorry i there is no item with that name in your inventory")




#______________________________________________________________
class Item:
    def __init__(self, name, info, dmg, space):
        self.name = name
        self.info = info
        self.dmg = dmg
        self.space = space

    def item_info(self):
        print(self.name)
        print(self.info)

#______________________________________________________________
class Room:
    """Create new Room.
    'name'=(str)name of room
    'info'=(str)Info about room
    'exits'=(list)Directions of room exits 'n','s','e','w'
    'con'=(dict){'n': 'roomName'} Specifies the room each exit goes to
    items=(List of objects) Of items in the room"""
    def __init__(self, name, info, exits, con, items):
        self.name = name
        self.info = info
        self.exits = exits
        self.connections = con
        self.items = []
        if items:
            for item in items:
                self.items.append(item)
        

#--------------------------------------------------------------
    def print_room_name(self):
        """Prints the name of the room"""
        print(self.name)

#--------------------------------------------------------------
    def look_at_room(self):
        """Prints the rooms info
        and if there is items in the room pint them"""
        print(self.info)
        # If there are items in the room run .item_info for each item
        if self.items:
            if len(self.items) == 1:
                print("There is a item in the room")
                self.items[0].item_info()
            else:
                print("There are a couple of items in the room")
                for item in self.items:
                    item.item_info()

#--------------------------------------------------------------
    def get_connections(self):
        """Returns the room exits and connections"""
        return self.exits, self.connections

#--------------------------------------------------------------
    def add_item(self, item):
        self.items.append(item)

#--------------------------------------------------------------
    def remove_item(self, user_input):
        """Check if userinput is == to a item in the Room"""

        for item in self.items:
            if item.name in user_input:
                self.items.remove(item)
                print("You tok the %s" %item.name)
                return item

        print("Sorry i there is no item with that name in the room")








#______________________________________________________________
class Movment:
    """Class to move player
    'startPos'=(str)Name of the room the player will start in"""
    def __init__(self, startPos):
        self.pos = startPos

#--------------------------------------------------------------
    def get_player_pos(self):
        return self.pos

#--------------------------------------------------------------
    def move_player(self, exits, connections, p):
        """Moves the player if the direction is a exit
        'exits'=(list)The rooms exits
        'connections'=(dict)The connections to other rooms"""
        if p in exits:
            #print("Moving player to %r" % connections[p])
            self.pos = connections[p]
        else:
            print("Cant go that way")

