class Static_Item():
    def __init__(self, 
                name:str, 
                description:str,
                is_open:bool,
                is_locked:bool,
                inventory:list,
                key_id:int,
                ) -> None:
        
        self.name = name
        self.description = description
        self.is_open = is_open
        self.is_locked = is_locked
        self.inventory = inventory
        self.key_id = key_id


    def look_att(self):
        print (self.description)
        self.look_in()

    def look_in(self): # Print items in/on container 
                        # If locked/Closed say that it is 
        if self.is_locked:
            print('It\'s locked')
        if not self.is_open:
            print('It\'s colesd')
            return
        print ('contains')
        for item in self.inventory:
            print (item.name)


    def add_item(self, item):
        self.inventory.append(item)
    
    def take_item(self, item_name):

        for item in self.inventory:
            if item.name == item_name:
                self.inventory.remove(item)
                return(item)
#============================================================
class Item():
    def __init__(self,
                name:str,
                description:str
                ) -> None:
        self.name = name
        self.description = description
#============================================================
class Key(Item):
    def __init__(self, name: str, description: str, key_id: int) -> None:
        super().__init__(name, description)

        self.key_id = key_id
#============================================================
class Room():
    def __init__(self,
                name: str,
                description: str,
                exits: list,
                is_special: bool,
                static_item: Static_Item
                ) -> None:
        self.name = name
        self.description = description
        self.exits = exits
        self.is_special = is_special
        self.static_items = static_item
        self.is_enterd = False

    def enter_room(self):
        print (self.name)
        if self.is_enterd:
            return
        self.is_enterd = True
        print(self.description)
        
        # For later use maybe
        if self.is_special:
            self.run_event()


    def get_info(self):
        print (self.description)

        if self.static_items:
            self.static_items.look_att()

    def run_event():
        pass

    def entrence_event():
        pass

    def break_stuff():
        pass ## Dunno kan vara kul ingen aning:::


#============================================================
class Player():
    def __init__(self,
                start_x:int = 0,
                start_y:int = 0,
                hp: int = 50,
                speed:int = 20,
                inventory_space:int = 20,
                ) -> None:
        
        self.x = start_x
        self.y = start_y
        self.hp = hp
        self.speed = speed
        self.inventory_space = inventory_space
        self.bag = []

    def move_player(self, dir):
        pass
    
    def drop_item(self, item:Item):
        pass


class World_Builder():
    def __init__(self,
                size_X :int,
                size_Y :int,
                ) -> None:
        
        self.world_matrix = size_X*[size_Y*[Room]]

    def add_room(self,
                room:Room,
                x:int,
                y:int,
                ):
        self.world_matrix[x][y] = room
    
    def add_item(self, room: Room, item:Item):
        pass
    
    def add_Static_item(self, room:Room, static_item:Static_Item):
        pass

    def create_special_connectiosn(self, room1:Room, room2:Room):
        pass


    def get_world(self):
        return self.world_matrix
