
class Player():
    def __init__(self) -> None:
        pass


class Room():
    def __init__(self,
                name :str,
                description :str,
                exits :list,
                is_special :bool,

                ) -> None:
        pass

    def get_info():
        pass

    def run_event():
        pass

    def entrence_event():
        pass

    def break_stuff():
        pass ## Dunno kan vara kul ingen aning:::

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


    def look_in(self):

        for item in self.inventory:
            print (item.name)

    def add_item(self, item):
        self.inventory.append(item)
    
    def take_item(self, item_name):

        for item in self.inventory:
            if item.name == item_name:
                self.inventory.remove(item)
                return(item)

class Item():
    def __init__(self,
                name:str,
                description:str
                ) -> None:
        self.name = name
        self.description = description

class Key(Item):
    def __init__(self, name: str, description: str, key_id: int) -> None:
        super().__init__(name, description)

        self.key_id = key_id


world_matrix = 5*[5*[Room]]

main_Room = Room()


world_matrix[0][0] = main_Room


print (world_matrix)
