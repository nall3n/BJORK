from game import Room, Item


knife = Item('knife', 'A pointy looking thing. Might be good att stabbing things', 3, 2)

world = {}

world['entrance'] = Room('entrance', 'You stand in the entrance of a big house. To the north is a door', ['n'], {'n':'ballroom'}, [knife] ) 
world['ballroom'] = Room('ballroom', 'You walk in to a big ballroom. In the middle of the room in the floor lies a blänkande svärd! \nThere is a door to the west, east and sout', ['s'], {'s':'entrance'}, None)



